import os, sqlite3

class Pkmn_Database:
    def __init__(self, db_name='pkmn.db'):
        self.db_path = os.path.join(os.path.dirname(__file__), db_name)
        
    def connect(self):
        # Connexion à la base de données
        return sqlite3.connect(self.db_path)
    
    
class Test_Database:
    def __init__(self, db_name='test_pkmn.db'):
        self.db_path = os.path.join(os.path.dirname(__file__), db_name)
        
    def connect(self):
        # Connexion à la base de données
        return sqlite3.connect(self.db_path)