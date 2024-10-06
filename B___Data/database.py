import sqlite3

class Database:
    def __init__(self, db_path):
        """Initialise la connexion à la base de données SQLite."""
        self.db_path = db_path  # Stocke le chemin de la base de données
        self.connection = None
        self.cursor = None
        self.connect()  # Établit la connexion lors de l'initialisation

    def connect(self):
        """Établit la connexion à la base de données si elle n'est pas déjà ouverte."""
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()

    def close(self):
        """Ferme la connexion à la base de données."""
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None  # Réinitialise le curseur

    def count(self, table_name):
        """Compte le nombre de lignes dans une table spécifique."""
        self.connect()  # Assurez-vous que la connexion est ouverte
        self.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = self.cursor.fetchone()[0]
        return count
    
    
    
    
