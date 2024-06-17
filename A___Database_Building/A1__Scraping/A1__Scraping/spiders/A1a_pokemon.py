import scrapy
from ..items import pokemonItem

class PokemonSpider(scrapy.CrawlSpider):
    name = "Pokemonscraper"
    allowed_domains = ["pokepedia.com"]
    
    def start_requests(self):
        url = 'https://www.pokepedia.fr/Liste_des_Pokémon_dans_l%27ordre_du_Pokédex_National'
        yield scrapy.Request(url=url, callback=self.parse_links)
        
    def parse_links(self, response):
        
#           selectionne ce lien        
#                 ▼    
# 0144 | 🐦 | Artikodin | Articuno | Arktos | フリーザーFurīzā | Freezer | Glace Vol
        links = response.css('td[height="50px"] > a::attr(href)').getall()
        
        
        for link in links:
            yield response.follow(link, callback=self.parse_pokemon)
            
    def parse_pokemon(self, response):
        pass