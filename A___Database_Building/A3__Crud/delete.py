import sqlite3

path_to_database = '../../../B___Data/pkmn.db'

def delete_pokemon(nom_pkmn):
    connection = sqlite3.connect(path_to_database)
    cursor = connection.cursor()
    query = f"""
    DELETE FROM Pokemons
    WHERE nom_pkmn=?
    """
    cursor.execute(query, (nom_pkmn,))
    connection.commit()
    connection.close()
    