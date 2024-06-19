from itemadapter import ItemAdapter
import csv, os

class A1ScrapingPipeline:
    def __init__(self):
        if os.path.exists('poketest.csv'):
            os.remove('poketest.csv')
        
        self.csvfile = open('poketest.csv', mode='w', newline='', encoding='utf-8')
        self.fieldnames = [
            'nom_pkmn',
            'num_pokedex',
            'url_image',
            'type_1', 
            'type_2',
            'taille_m',
            'poids_kg',
            'talent_1', 
            'talent_2', 
            'talent_cache', 
            'sexe',
            'taux_de_capture', 
            'cycle_eclosion', 
            'groupe_oeuf_1', 
            'groupe_oeuf_2',
            'points_effort', 
            'point_exp', 
            'exp_niv100', 
            'pv', 
            'attaque', 
            'attaque_speciale',
            'defense', 
            'defense_speciale', 
            'vitesse'
        ]
        
        # Create a CSV DictWriter and write the header
        self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
        self.writer.writeheader()
    
    def close_spider(self, spider):
        # Close the CSV file
        self.csvfile.close()
    
    def process_item(self, item, spider):
        # Write item to CSV
        self.writer.writerow(item)
        return item

