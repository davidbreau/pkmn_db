import sqlite3

path_to_database = '../../../B___Data/pkmn.db'

class Pokemon:
    
    def __init__(self, nom):
        self.nom = nom
        data = self.read_pokemon()
        self.nom_pkmn = data['nom_pkmn']
        self.nom_pkmn_us = data['nom_pkmn_us']
        self.num_pokedex = data['num_pokedex']
        self.url_image = data['url_image']
        self.url_cri = data['url_cri']
        self.type_1 = data['type_1']
        self.type_2 = data['type_2']
        self.taille_m = data['taille_m']
        self.poids_kg = data['poids_kg']
        self.talent_1 = data['talent_1']
        self.talent_2 = data['talent_2']
        self.talent_cache = data['talent_cache']
        self.sexe = data['sexe']
        self.taux_de_capture = data['taux_de_capture']
        self.cycle_eclosion = data['cycle_eclosion']
        self.groupe_oeuf_1 = data['groupe_oeuf_1']
        self.groupe_oeuf_2 = data['groupe_oeuf_2']
        self.points_effort = data['points_effort']
        self.points_exp = data['points_exp']
        self.exp_niv100 = data['exp_niv100']
        self.pv = data['pv']
        self.attaque = data['attaque']
        self.attaque_speciale = data['attaque_speciale']
        self.defense = data['defense']
        self.defense_speciale = data['defense_speciale']
        self.vitesse = data['vitesse']
        self.GO_attaque = data['GO_attaque']
        self.GO_defense = data['GO_defense']
        self.GO_resistance = data['GO_resistance']
        self.GO_Buddy_Distance_Km = data['GO_Buddy_Distance_Km']
        
    def read_pokemon(self):
        connection = sqlite3.connect(path_to_database)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        query = f"""
        SELECT * 
        FROM Pokemons 
        WHERE nom_pkmn=?
        """
        cursor.execute(query, (self.nom,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return dict(result)