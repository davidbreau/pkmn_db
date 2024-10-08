from typing import List; from io import BytesIO; from PIL import Image; from IPython.display import display 
import requests, os, sqlite3; 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True"; import pygame

class Pokemon:
    """
    A class representing a Pokémon and managing associated CRUD operations.
    """

    def __init__(self, db, nom_pkmn: str):
        """
        Initialize a Pokémon object and load its data from the database.

        Args:
            db (Database): An instance of the Database class.
            nom_pkmn (str): The name of the Pokémon, serving as a unique identifier.
        """
        self.nom_pkmn = nom_pkmn
        self.db = db  # Stocke l'instance de Database
        self._load_data()



    def _load_data(self):
        """Load the Pokémon's data from the database and set attributes."""
        self.db.connect()  # Établir la connexion
        try:
            cursor = self.db.connection.cursor()
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
            self.db.close()  # Fermer la connexion

    def read(self):
        """Read the Pokémon's data from the database."""
        return self._data

    @classmethod
    def create(cls, db, nom_pkmn: str, **kwargs):
        """Create a new Pokémon in the database."""
        db.connect()  # Établir la connexion
        try:
            cursor = db.connection.cursor()
            kwargs['nom_pkmn'] = nom_pkmn
            columns = ', '.join(kwargs.keys())
            placeholders = ', '.join(['?' for _ in kwargs])
            values = tuple(kwargs.values())
            cursor.execute(f"INSERT INTO Pokemons ({columns}) VALUES ({placeholders})", values)
            db.connection.commit()
            return cls(db, nom_pkmn)
        finally:
            db.close()  # Fermer la connexion

    def update(self, **kwargs):
        """Update the Pokémon's attributes in the database."""
        self.db.connect()  # Établir la connexion
        try:
            cursor = self.db.connection.cursor()
            for key, value in kwargs.items():
                cursor.execute(f"UPDATE Pokemons SET {key} = ? WHERE nom_pkmn = ?", (value, self.nom_pkmn))
                setattr(self, key, value)  # Update the attribute in the instance
                self._data[key] = value  # Update the _data dictionary
            self.db.connection.commit()
        finally:
            self.db.close()  # Fermer la connexion

    def delete(self):
        """Delete the Pokémon from the database."""
        self._connect()  # Établir la connexion
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("DELETE FROM Pokemons WHERE nom_pkmn = ?", (self.nom_pkmn,))
            self.db.connection.commit()
        finally:
            self.db.close()  # Fermer la connexion

    def add_new_form(self, new_form_name: str, **modifications):
        """Add a new form of the current Pokemon to the database."""
        data = self.read()
        data['nom_pkmn'] = new_form_name
        data.update(modifications)
        return self.create(self.db, **data)

    @classmethod
    def read_all(cls, db) -> List[str]:
        """Retrieve all Pokémon names from the database."""
        db.connect()  # Établir la connexion
        try:
            cursor = db.connection.cursor()
            cursor.execute("SELECT nom_pkmn FROM Pokemons")
            result = cursor.fetchall()
            return [row[0] for row in result]  # Return a list of Pokémon names
        finally:
            db.close()  # Fermer la connexion
            
    def display_image(self):
        """
        Affiche l'image du Pokémon dans le notebook.
        """
        base_url = "https://www.pokepedia.fr/"
        if hasattr(self, 'url_image'):
            image_url = f"{base_url}{self.url_image}"
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            display(img)  # Affiche l'image
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
    def count_all(cls, db) -> int:
        """Count the number of Pokémon in the database."""
        db.connect()  # Établir la connexion
        try:
            cursor = db.connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM Pokemons")
            result = cursor.fetchone()[0]
            return result
        finally:
            db.close()  # Fermer la connexion

def main():
    """Main function to demonstrate functionality."""
    db = sqlite3.connect('tests_pkmn.db')  # Créez l'instance de Database
    total_pokemons = Pokemon.count_all(db)
    print(f"Total Pokémon: {total_pokemons}")

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly