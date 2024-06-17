from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from A1__Scraping.items import Pokemon

class PokedexSpider(CrawlSpider):
    name = 'pokedex_spider'
    allowed_domains = ['pokepedia.fr']
    start_urls = ['https://www.pokepedia.fr/Liste_des_Pokémon_dans_l%27ordre_du_Pokédex_National']

    rules = (
        Rule(LinkExtractor(restrict_css='table > tbody > tr > td:nth-child(3) > a'), callback='parse_pokemon'),
    )

    def parse_pokemon(self, response):
        pokemon = Pokemon()
        pokemon['number'] = response.css('table.infobox > tbody > tr:nth-child(2) > td > b::text').get().strip()
        pokemon['name'] = response.css('h1::text').get().strip()

        return pokemon
