from itemadapter import ItemAdapter
import csv, os, sqlite3

# class PkmnPipeline:
#     def __init__(self):
#         if os.path.exists('poketest.csv'):
#             os.remove('poketest.csv')
        
#         self.csvfile = open('poketest.csv', mode='w', newline='', encoding='utf-8')
#         self.fieldnames = [
#             'nom_pkmn',
#             'nom_pkmn_us',
#             'num_pokedex',
#             'url_image',
#             'type_1', 
#             'type_2',
#             'taille_m',
#             'poids_kg',
#             'talent_1', 
#             'talent_2', 
#             'talent_cache', 
#             'sexe',
#             'taux_de_capture', 
#             'cycle_eclosion', 
#             'groupe_oeuf_1', 
#             'groupe_oeuf_2',
#             'points_effort', 
#             'points_exp', 
#             'exp_niv100', 
#             'pv', 
#             'attaque', 
#             'attaque_speciale',
#             'defense', 
#             'defense_speciale', 
#             'vitesse'
#         ]
        
#         # Create a CSV DictWriter and write the header
#         self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
#         self.writer.writeheader()
    
#     def close_spider(self, spider):
#         # Close the CSV file
#         self.csvfile.close()
    
#     def process_item(self, item, spider):
#         # Write item to CSV
#         self.writer.writerow(item)
#         return item

class PkmnPipeline:
    def __init__(self):
        self.data_dir = '../../../B___Data'        
        self.fieldnames_map = {
            'PokemonSpider': [
                'nom_pkmn', 'nom_pkmn_us', 'num_pokedex', 'url_image', 'type_1', 
                'type_2', 'taille_m', 'poids_kg', 'talent_1', 'talent_2', 
                'talent_cache', 'sexe', 'taux_de_capture', 'cycle_eclosion', 
                'groupe_oeuf_1', 'groupe_oeuf_2', 'points_effort', 'points_exp', 
                'exp_niv100', 'pv', 'attaque', 'attaque_speciale', 'defense', 
                'defense_speciale', 'vitesse'
            ]}
    
        # self.conn = sqlite3.connect(os.path.join(self.data_dir, 'pkmn.db'))
        # self.cursor = self.conn.cursor()   
        
    def open_spider(self, spider):
        spider_name = spider.name.lower()
        csv_filepath = os.path.join(self.data_dir, f"{spider_name[:-5]}.csv")
        self.fieldnames = self.fieldnames_map.get(spider.name, [])
        
        # Supprime le fichier s'il existe avant d'ouvrir un nouveau fichier
        if os.path.exists(csv_filepath):
            os.remove(csv_filepath)
            
        self.csvfile = open(csv_filepath, mode='w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def close_spider(self, spider):
        self.csvfile.close()
        # self.conn.commit()
        # self.conn.close()

    def process_item(self, item, spider):
        # if spider.name == 'PokemonSpider':
        #     self.process_pokemon(item)

        # Écrit les données dans le fichier CSV
        self.writer.writerow(item)
        
        return item
 
    # def process_pokemon(self, item):
    #     self.cursor.execute('''
    #         INSERT INTO Pokemons (
    #             nom_pkmn, nom_pkmn_us, num_pokedex, url_image, type_1, 
    #             type_2, taille_m, poids_kg, talent_1, talent_2, 
    #             talent_cache, sexe, taux_de_capture, cycle_eclosion, 
    #             groupe_oeuf_1, groupe_oeuf_2, points_effort, points_exp, 
    #             exp_niv100, pv, attaque, attaque_speciale, defense, 
    #             defense_speciale, vitesse
    #         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    #     ''', (
    #         item.get('nom_pkmn'), item.get('nom_pkmn_us'), item.get('num_pokedex'),
    #         item.get('url_image'), item.get('type_1'), item.get('type_2'),
    #         item.get('taille_m'), item.get('poids_kg'), item.get('talent_1'),
    #         item.get('talent_2'), item.get('talent_cache'), item.get('sexe'),
    #         item.get('taux_de_capture'), item.get('cycle_eclosion'),
    #         item.get('groupe_oeuf_1'), item.get('groupe_oeuf_2'),
    #         item.get('points_effort'), item.get('points_exp'), item.get('exp_niv100'),
    #         item.get('pv'), item.get('attaque'), item.get('attaque_speciale'),
    #         item.get('defense'), item.get('defense_speciale'), item.get('vitesse')
    #     ))

    #     return item
