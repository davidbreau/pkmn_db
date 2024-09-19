import sqlite3

def get_database_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(os.path.dirname(os.path.dirname(current_dir)), 'B___Data', 'pkmn.db')

def create_pokemon(
    nom_pkmn:str, nom_pkmn_us:str, num_pokedex:int,
    url_image:str, url_cri:str,
    type_1:str, type_2:str,
    taille_m:float, poids_kg:float,
    talent_1:str, talent_2:str, talent_cache:str,
    sexe:str, taux_de_capture:int, cycle_eclosion:int, groupe_oeuf_1:str, groupe_oeuf_2:str, points_effort:str, points_exp:str, exp_niv100:str,
    pv: int, attaque:int, attaque_speciale:int, defense:int, defense_speciale:int, vitesse:int,
    GO_attaque:int=None, GO_defense:int=None,
    GO_resistance:int=None,
    GO_Buddy_Distance_Km:int =None
    ):
    connection = get_database_path()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO Pokemons (
            nom_pkmn, nom_pkmn_us, num_pokedex, 
            url_image, url_cri, 
            type_1, type_2, 
            taille_m, poids_kg, 
            talent_1, talent_2, talent_cache, 
            sexe, taux_de_capture, cycle_eclosion, groupe_oeuf_1, groupe_oeuf_2, points_effort, points_exp, exp_niv100, 
            pv, attaque, attaque_speciale, defense, defense_speciale, vitesse, 
            GO_attaque, GO_defense, GO_resistance, GO_Buddy_Distance_Km
        ) VALUES (
            ?, ?, ?, 
            ?, ?, 
            ?, ?, 
            ?, ?, 
            ?, ?, ?, 
            ?, ?, ?, ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?
        )
    ''', (
        nom_pkmn, nom_pkmn_us, num_pokedex, url_image, url_cri, 
        type_1, type_2, taille_m, poids_kg, talent_1, 
        talent_2, talent_cache, sexe, taux_de_capture, cycle_eclosion, 
        groupe_oeuf_1, groupe_oeuf_2, points_effort, points_exp, exp_niv100, 
        pv, attaque, attaque_speciale, defense, defense_speciale, vitesse, 
        GO_attaque, GO_defense, GO_resistance, GO_Buddy_Distance_Km
    ))
    connection.commit()
    connection.close()
    
