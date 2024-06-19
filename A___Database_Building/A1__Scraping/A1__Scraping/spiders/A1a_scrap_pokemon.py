import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import pokemonItem

class PokemonSpider(CrawlSpider):
    name = "PokemonSpider"
    allowed_domains = ["www.pokepedia.fr"]
    
    def start_requests(self):
        url = 'https://www.pokepedia.fr/Liste_des_Pokémon_dans_l%27ordre_du_Pokédex_National'
        yield scrapy.Request(url=url, callback=self.parse_links)
        
    def parse_links(self, response):
        
        # sur chaque ligne de la liste
#           selectionne ce lien         
#                 ▼    
# 0144 | 🐦 | Artikodin | Articuno | Arktos | フリーザーFurīzā | Freezer | Glace Vol
        links = response.css('td[height="50px"] > a::attr(href)').getall()
        
        
        for link in links[:9]: ###### 🚨🚨🚨 Retirer [:5] pour tout scraper
            
            yield response.follow(link, callback=self.parse_pokemon)
            
    def parse_pokemon(self, response):
        
        nom_pokemon = response.css("th.entêtesection::text").get()
        num_pokedex = response.css('span.explain[title="Numérotation nationale"]::text').re(r'№ (\d+)')[0].zfill(4)
        url_image = response.css('.mw-parser-output .illustration a img::attr(src)').get()
        type1 = response.css('tr > td[colspan="3"] > span[typeof="mw:File"]:nth-child(1) > a::attr(title)').get()
            #retourne 'Nomdutype (type)'
        type1 = type1.split()[0]
        try:
            type2 = response.css('tr > td[colspan="3"] > span[typeof="mw:File"]:nth-child(2) > a::attr(title)').get() 
            type2 = type2.split()[0]
        except:
            type2 = None
        taille_m = response.css('th:contains("Taille") + td::text').get().strip()
        
        
        
        pokemon = pokemonItem()
        
        pokemon['nom_pkmn'] = nom_pokemon
        pokemon['num_pokedex'] = f"{int(num_pokedex):04d}" 
        pokemon['url_image'] = url_image
        pokemon['type_1'] = type1
        pokemon['type_2'] = type2
        # taille_M = scrapy.Field()
        # poids_kg = scrapy.Field()
        # talent_1 = scrapy.Field()
        # talent_2 = scrapy.Field()
        # talent_cache = scrapy.Field()
        # sexe = scrapy.Field()
        # taux_de_capture = scrapy.Field()
        # cycle_eclosion = scrapy.Field()
        # groupe_oeuf_1 = scrapy.Field()
        # groupe_oeuf_2 = scrapy.Field()
        # points_effort = scrapy.Field()
        # point_exp = scrapy.Field()
        # exp_niv100 = scrapy.Field()
        # pv = scrapy.Field()
        # attaque = scrapy.Field()
        # attaque_speciale = scrapy.Field()
        # defense = scrapy.Field()
        # defense_speciale = scrapy.Field()
        # vitesse = scrapy.Field()
        yield pokemon