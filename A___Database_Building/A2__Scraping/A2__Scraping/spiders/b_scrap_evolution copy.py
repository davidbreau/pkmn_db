import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import pokemonItem


 

import scrapy
import csv

class PokemonEvolutionSpider(scrapy.Spider):
    name = "EvolutionSpider"
    start_urls = ['https://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_par_niveau_d%27%C3%A9volution']
    
    custom_settings = {
        'ITEM_PIPELINES': {
            'A2__Scraping.pipelines.EvolutionPipeline': 300,  # Activer uniquement EvolutionPipeline
        }
    }

    def open_spider(self, spider):
        # Ouvre un fichier CSV pour écrire les résultats
        self.csv_file = open('evolutions.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)
        # Écrit l'en-tête du fichier CSV
        self.csv_writer.writerow(['pokemon_evoluant', 'pokemon_evolue', 'condition'])

    def close_spider(self, spider):
        # Ferme le fichier CSV une fois le scrap terminé
        self.csv_file.close()

    def parse(self, response):
        evolutions_rows = response.css('tr')

        for row in evolutions_rows:
            pokemon_evoluant = row.css('td:nth-child(1) a::text').get()
            pokemon_evolue = row.css('td:nth-child(3) a::text').get()
            condition = row.css('td:nth-child(2)::text').get()

            if pokemon_evoluant and pokemon_evolue and condition:
                # Écrit les données dans le fichier CSV
                self.csv_writer.writerow([pokemon_evoluant, pokemon_evolue, condition.strip()])

                # Tu peux aussi utiliser yield si tu veux voir les résultats dans la console
                yield {
                    'pokemon_evoluant': pokemon_evoluant,
                    'pokemon_evolue': pokemon_evolue,
                    'condition': condition.strip()
                }
