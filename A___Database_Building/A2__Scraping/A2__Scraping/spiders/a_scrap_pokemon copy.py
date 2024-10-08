import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import pokemonItem

class PokemonSpider(CrawlSpider):
    
    name = "PokemonSpider"
    allowed_domains = ["www.pokepedia.fr"]
    
    
###🔽 Prends la page web la liste des monstres    
    def start_requests(self):
        """❓
        _summary_
            Démarre les requêtes pour scraper la page.
        Yields:
            scrapy.Request: Lance la fonction pour parcourir les liens
        """
        
        url = 'https://www.pokepedia.fr/Liste_des_Pokémon_dans_l%27ordre_du_Pokédex_National'
        yield scrapy.Request(url=url, callback=self.parse_links)
        
 
###🔽 Sélectionne le lien sur le nom de chaque élément de la liste 
#                 ▼    
# 0144 | 🐦 | Artikodin | Articuno | Arktos | フリーザーFurīzā | Freezer | Glace Vol        
    def parse_links(self, response: scrapy.http.response):
        """ ❓
        _summary_
        Extrait les liens des pages de détails depuis la liste et suit ces liens.
        
        Args:
            response (scrapy.http.response): La reponse HTTP de la fonction start_requests

        Yields:
            response.follow: Lance la fonction pour extraire les informations sur chaque page.
        """
        
        links = response.css('tr td[id] > a::attr(href)').getall()
        for link in links: ###### 🚨🚨🚨 Retirer/Mettre [-:-] pour tout tester le scrap ou lancer le tout
            yield response.follow(link, callback=self.parse_pokemon)
            
            
            
    def parse_pokemon(self, response: scrapy.http.response):
        """❓
        _summary_
        Extrait toutes les informations et les attributs à l'item scrapy pour gérer l'enregistrement sur le pipeline.
        Args:
            response: La reponse HTTP de la fonction parse_links

        Yields:
            pokemon: l'objet scrapy contenant toutes les informations scrapées
        """
##################        
### Extraction ###
##################       
######🔽 À chaque page de monstre, récupère chaque information précise et les stocks dans des variables
        nom_pkmn = response.css("th.entêtesection::text").get()
        nom_pkmn_us = response.css('th:contains("Nom anglais") + td::text').get()
        num_pokedex = response.css('span.explain[title="Numérotation nationale"]::text').get() #.re(r'№ (\d+)')[0].zfill(4)
        url_image = response.css('.mw-parser-output .illustration a img::attr(src)').get()
        url_cri = response.css('audio::attr(src)').get()
        type1 = response.css('tr > td[colspan="3"] > span[typeof="mw:File"]:nth-child(1) > a::attr(title)').get()
            #retourne 'Nomdutype (type)'
        type1 = type1.split()[0]
        try:
            type2 = response.css('tr > td[colspan="3"] > span[typeof="mw:File"]:nth-child(2) > a::attr(title)').get() 
            type2 = type2.split()[0]
        except:
            type2 = None    
        taille_m = response.css('th:contains("Taille") + td::text').get()
        try:
            taille_m = taille_m.split(' ')
            taille_m = [x for x in taille_m if x[0].isdigit()][0]
        except:
            taille_m = None
        poids_kg = response.css('th:contains("Poids") + td::text').get().strip()
        talents = response.css('th:contains("Talent") + td a::text').getall()
        sexe = response.css('th:contains("Sexe") + td::text').get().replace('\xa0', ' ').replace('\u202f', '')
        try:
            taux_de_capture = response.css('th:contains("Taux de capture") + td::text').get() 
            cycle_eclosion = response.css('th:contains("closion") + td::text').get().strip()
            groupes_oeufs = response.css('th:contains("Groupe") + td a::text').getall()
            points_effort = response.css('th:contains("effort") + td::text').get()
            point_exp = response.css('th:contains("exp.") + td::text').get()
            exp_niv100 = response.css('th:contains("niveau 100") + td::text').get()
        except:
            taux_de_capture, cycle_eclosion, groupes_oeufs, points_effort, point_exp, exp_niv100 = None, None, None, None, None, None
        try:
            pv = response.css('td:contains("PV") + td::text').get().strip()
            attaque = response.css('td:contains("Attaque") + td::text').get().strip()
            defense = response.css('td:contains("Défense") + td::text').get().strip()
            attaque_speciale = response.css('td:contains("Défense") + td::text').get().strip()
            defense_speciale = response.css('td:contains("Défense Spéciale") + td::text').get().strip()
            vitesse = response.css('td:contains("Vitesse") + td::text').get().strip()
        except:
            pv, attaque, defense, attaque_speciale, defense_speciale, vitesse = None, None, None, None, None, None
     
     
###################        
### Attribution ###
###################   
        pokemon = pokemonItem()
######🔽 Attribut chaque information à la caractéristique de l'item 
        pokemon['nom_pkmn'] = nom_pkmn
        pokemon['nom_pkmn_us'] = nom_pkmn_us
        pokemon['num_pokedex'] = num_pokedex[-4:] if num_pokedex else None #f"{int(num_pokedex):04d}" 
        pokemon['url_image'] = url_image
        pokemon['url_cri'] = url_cri[18:]
        pokemon['type_1'] = type1
        pokemon['type_2'] = type2
        pokemon['taille_m'] = taille_m 
        pokemon['poids_kg'] = poids_kg.split(" ")[0] 
        
        if 'talent caché' in talents:
            if len(talents) == 3:
                pokemon['talent_1'] = talents[0]
                pokemon['talent_cache'] = talents[1]
            elif len(talents) == 4:
                pokemon['talent_1'] = talents[0]
                pokemon['talent_2'] = talents[1]
                pokemon['talent_cache'] = talents[-2]
        else:
            if len(talents) == 1:
                pokemon['talent_1'] = talents[0]
            if len(talents) == 2:
                pokemon['talent_1'] = talents[0]
                pokemon['talent_2'] = talents[1]
        
        pokemon['sexe'] = sexe
        pokemon['taux_de_capture'] = taux_de_capture
        pokemon['cycle_eclosion'] = cycle_eclosion
        try:
            pokemon['groupe_oeuf_1'] = groupes_oeufs[0]
        except:
            pass    
        try:
            pokemon['groupe_oeuf_2'] = groupes_oeufs[1]
        except:
            pass
        pokemon['points_effort'] = points_effort
        pokemon['points_exp'] = point_exp
        pokemon['exp_niv100'] = exp_niv100
        pokemon['pv'] = pv
        pokemon['attaque'] = attaque
        pokemon['defense'] = defense
        pokemon['attaque_speciale'] = attaque_speciale
        pokemon['defense_speciale'] = defense_speciale
        pokemon['vitesse'] = vitesse

        yield pokemon