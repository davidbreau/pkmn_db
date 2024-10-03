from connectors import Test_Database as Pkmn_Database
import sqlite3, pygame, requests
from typing import List; from io import BytesIO; from PIL import Image; from IPython.display import display

class Pokemon:
    """
    A class representing a Pokémon and managing associated CRUD operations.
    """

    def __init__(self, nom_pkmn: str):
        """
        Initialize a Pokémon object and load its data from the database.

        Args:
            nom_pkmn (str): The name of the Pokémon, serving as a unique identifier.
        """
        self.nom_pkmn = nom_pkmn
        self.db = Pkmn_Database()
        self._load_data()

    def _load_data(self):
        """Load the Pokémon's data from the database and set attributes."""
        connection = self.db.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Pokemons WHERE nom_pkmn = ?", (self.nom_pkmn,))
            data = cursor.fetchone()
            if data:
                columns = [description[0] for description in cursor.description]
                self._data = dict(zip(columns, data))
                for key, value in self._data.items():
                    setattr(self, key, value)
            else:
                raise ValueError(f"No Pokémon found with the name {self.nom_pkmn}")
        finally:
            connection.close()

    def read(self):
        """Read the Pokémon's data from the database."""
        return self._data

    @classmethod
    def create(cls, nom_pkmn: str, **kwargs):
        """Create a new Pokémon in the database."""
        db = Pkmn_Database()
        connection = db.connect()
        try:
            cursor = connection.cursor()
            kwargs['nom_pkmn'] = nom_pkmn
            columns = ', '.join(kwargs.keys())
            placeholders = ', '.join(['?' for _ in kwargs])
            values = tuple(kwargs.values())
            cursor.execute(f"INSERT INTO Pokemons ({columns}) VALUES ({placeholders})", values)
            connection.commit()
            return cls(nom_pkmn)
        finally:
            connection.close()

    def update(self, **kwargs):
        """Update the Pokémon's attributes in the database."""
        connection = self.db.connect()
        try:
            cursor = connection.cursor()
            for key, value in kwargs.items():
                cursor.execute(f"UPDATE Pokemons SET {key} = ? WHERE nom_pkmn = ?", (value, self.nom_pkmn))
                setattr(self, key, value)  # Update the attribute in the instance
                self._data[key] = value  # Update the _data dictionary
            connection.commit()
        finally:
            connection.close()

    def delete(self):
        """Delete the Pokémon from the database."""
        connection = self.db.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Pokemons WHERE nom_pkmn = ?", (self.nom_pkmn,))
            connection.commit()
        finally:
            connection.close()

    def add_new_form(self, new_form_name: str, **modifications):
        """Add a new form of the current Pokemon to the database."""
        data = self.read()
        data['nom_pkmn'] = new_form_name
        data.update(modifications)
        return self.create(**data)

    @classmethod
    def read_all(cls) -> List[str]:
        """Retrieve all Pokémon names from the database."""
        db = Pkmn_Database()
        connection = db.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT nom_pkmn FROM Pokemons")
            result = cursor.fetchall()
            return [row[0] for row in result]  # Return a list of Pokémon names
        finally:
            connection.close()
            
            
    def display_image(self):
        """
        Affiche l'image du Pokémon dans le notebook.
        """
        base_url = "https://www.pokepedia.fr/"
        if hasattr(self, 'url_image'):
            image_url = f"{base_url}{self.url_image}"
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            display(img)  # Affiche l'image dans le notebook
        else:
            raise ValueError("L'URL de l'image n'est pas disponible.")

    def play_sound(self):
        """
        Joue le son du cri du Pokémon.
        """
        base_url = "https://www.pokepedia.fr/"
        if hasattr(self, 'url_cri'):
            sound_url = f"{base_url}{self.url_cri}"
            response = requests.get(sound_url)
            sound_file = BytesIO(response.content)

            # Initialiser pygame mixer
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Attendre que le son se termine
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        else:
            raise ValueError("L'URL du cri n'est pas disponible.")

    @classmethod
    def count_all(cls) -> int:
        """Count the number of Pokémon in the database."""
        db = Pkmn_Database()
        connection = db.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM Pokemons")
            result = cursor.fetchone()[0]
            return result
        finally:
            connection.close()

def main():
    """Main function to demonstrate functionality."""
    total_pokemons = Pokemon.count_all()
    print(f"Total Pokémon: {total_pokemons}")

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly






# from B___Data.connectors import Test_Database as Pkmn_Database
# import sqlite3

# class Pokemon:
#     """
#     A class representing a Pokémon and managing associated CRUD operations.
    
#     This class uses a database connection for each operation,
#     ensuring that no connection remains open between calls.
#     """

#     def __init__(self, nom_pkmn):
#         """
#         Initialize a Pokémon object and load its data from the database.

#         Args:
#             nom_pkmn (str): The name of the Pokémon, serving as a unique identifier.
#         """
#         self.nom_pkmn = nom_pkmn
#         self.db = Pkmn_Database()
#         self._load_data()

#     def _load_data(self):
#         """
#         Load the Pokémon's data from the database and set attributes.
#         """
#         connection = self.db.connect()
#         try:
#             cursor = connection.cursor()
#             cursor.execute("SELECT * FROM Pokemons WHERE nom_pkmn = ?", (self.nom_pkmn,))
#             data = cursor.fetchone()
#             if data:
#                 columns = [description[0] for description in cursor.description]
#                 self._data = dict(zip(columns, data))
#                 for key, value in self._data.items():
#                     setattr(self, key, value)
#             else:
#                 raise ValueError(f"No Pokémon found with the name {self.nom_pkmn}")
#         finally:
#             connection.close()

#     def read(self):
#         """
#         Read the Pokémon's data from the database.

#         Returns:
#             dict: A dictionary containing all the Pokémon's data.

#         Raises:
#             ValueError: If no Pokémon is found with the specified name.
#         """
#         return self._data

#     @classmethod
#     def create(cls, nom_pkmn, **kwargs):
#         """
#         Create a new Pokémon in the database.

#         Args:
#             nom_pkmn (str): The name of the Pokémon to create.
#             **kwargs: Additional attributes of the Pokémon.

#         Returns:
#             Pokemon: An instance of the Pokémon class representing the created Pokémon.

#         Raises:
#             sqlite3.Error: If an error occurs during database insertion.
#         """
#         db = Pkmn_Database()
#         connection = db.connect()
#         try:
#             cursor = connection.cursor()
            
#             kwargs['nom_pkmn'] = nom_pkmn
#             columns = ', '.join(kwargs.keys())
#             placeholders = ', '.join(['?' for _ in kwargs])
#             values = tuple(kwargs.values())
            
#             cursor.execute(f"INSERT INTO Pokemons ({columns}) VALUES ({placeholders})", values)
#             connection.commit()
#             return cls(nom_pkmn)
#         finally:
#             connection.close()

#     def update(self, **kwargs):
#         """
#         Update the Pokémon's attributes in the database.

#         Args:
#             **kwargs: The attributes to update and their new values.

#         Raises:
#             sqlite3.Error: If an error occurs during database update.
#         """
#         connection = self.db.connect()
#         try:
#             cursor = connection.cursor()
#             for key, value in kwargs.items():
#                 cursor.execute(f"UPDATE Pokemons SET {key} = ? WHERE nom_pkmn = ?", (value, self.nom_pkmn))
#                 setattr(self, key, value)  # Update the attribute in the instance
#                 self._data[key] = value  # Update the _data dictionary
#             connection.commit()
#         finally:
#             connection.close()
            
#     def delete(self):
#         """
#         Delete the Pokémon from the database.

#         Raises:
#             sqlite3.Error: If an error occurs during database deletion.
#         """
#         connection = self.db.connect()
#         try:
#             cursor = connection.cursor()
#             cursor.execute("DELETE FROM Pokemons WHERE nom_pkmn = ?", (self.nom_pkmn,))
#             connection.commit()
#         finally:
#             connection.close()
            
#     def add_new_form(self, new_form_name, **modifications):
#         """
#         Add a new form of the current Pokemon to the database.

#         This method creates a new Pokemon entry in the database representing a different
#         form of the current Pokemon. It copies all attributes of the current Pokemon
#         and applies the specified modifications to create the new form.

#         Args:
#             new_form_name (str): The name of the new Pokemon form.
#             **modifications: Keyword arguments representing the attributes to modify or add
#                             in the new Pokemon form.

#         Returns:
#             Pokemon: A new Pokemon instance representing the created form.

#         Raises:
#             sqlite3.Error: If there's an error during database operations.
#         """
#         data = self.read()
#         data['nom_pkmn'] = new_form_name
#         data.update(modifications)
#         return self.create(**data)
    
    
#     def read_all(self):
#         """
#         Récupère les noms et les URL des images de tous les Pokémon de la base de données.
#         """
#         with self.connection.cursor() as cursor:
#             cursor.execute("SELECT nom_pkmn, url_image FROM Pokemons")  # Sélectionne uniquement les colonnes souhaitées
#             result = cursor.fetchall()
#             self.connection.close()# Récupère tous les enregistrements
#             return result
        
#     def count_all(self):
#         """
#         Compte le nombre de Pokémon dans la base de données.
#         """
#         with self.connection.cursor() as cursor:
#             cursor.execute("SELECT COUNT(*) FROM Pokemons")
#             result = cursor.fetchone()[0]
#             self.connection.close()
#             return result
        
#     def main():
#         # Instanciation de la classe sans arguments
#         db = Pkmn_Database()  # Utilise les valeurs par défaut définies dans __init__
    
#     # Compter le nombre total de Pokémon
#         total_pokemons = db.count_all()
    
#     # Fermer la connexion
#         db.close()
        
#         return total_pokemons

#     if __name__ == "__main__":
#         main()  # Appel de la fonction main si le script est exécuté directement