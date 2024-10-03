import os, sqlite3

class Pkmn_Database:
    def __init__(self, db_name='pkmn.db'):
        """Initialise la connexion à la base de données SQLite."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        
    def connect(self):
        """Renvoie la connexion à la base de données."""
        return self.connection

    def close(self):
        """Ferme la connexion à la base de données."""
        self.connection.close()

    def commit(self):
        """Valide les changements dans la base de données."""
        self.connection.commit()

    def count(self):
        """Compte le nombre total de Pokémon dans la base de données."""
        self.cursor.execute("SELECT COUNT(*) FROM Pokemons")  # Assurez-vous que la table existe
        count = self.cursor.fetchone()[0]
        return count

class Test_Database(Pkmn_Database):
    def __init__(self, db_name='tests_pkmn.db'):
        """Initialise la connexion à la base de données SQLite pour les tests."""
        super().__init__(db_name)  # Appelle le constructeur de la classe parente

# Exemple d'utilisation
if __name__ == "__main__":
    # Utilisation de Pkmn_Database
    db = Pkmn_Database()
    print(f"Total Pokémon dans la base de données principale: {db.count_all()}")
    db.close()

    # Utilisation de Test_Database
    test_db = Test_Database()
    print(f"Total Pokémon dans la base de données de test: {test_db.count_all()}")
    test_db.close()
    
