import sqlite3

path_to_database = '../../../B___Data/pkmn.db'

def update_pokemon(
    nom_pkmn:str, nom_pkmn_us:str=None, num_pokedex:int=None,
    url_image:str=None, url_cri:str=None,
    type_1:str=None, type_2:str=None,
    taille_m:float=None, poids_kg:float=None,
    talent_1:str=None, talent_2:str=None, talent_cache:str=None,
    sexe:str=None, taux_de_capture:int=None, cycle_eclosion:int=None, groupe_oeuf_1:str=None, groupe_oeuf_2:str=None, points_effort:str=None, points_exp:str=None, exp_niv100:str=None,
    pv: int=None, attaque:int=None, attaque_speciale:int=None, defense:int=None, defense_speciale:int=None, vitesse:int=None,
    GO_attaque:int=None, GO_defense:int=None,
    GO_resistance:int=None,
    GO_Buddy_Distance_Km:int=None
    ):
    connection = sqlite3.connect(path_to_database)
    cursor = connection.cursor()

    # Dictionnaire des colonnes à mettre à jour si la valeur n'est pas None
    arguments = locals()
    del arguments['connection'], arguments['cursor']
    for colonne, valeur in arguments.items():
        if colonne != 'nom_pkmn' != 'connection' != 'cursor' and valeur is not None:
            query = f'UPDATE Pokemons SET {colonne} = ? WHERE nom_pkmn = ?'
            cursor.execute(query, (valeur, nom_pkmn))

    connection.commit()
    cursor.close()
    connection.close()

    