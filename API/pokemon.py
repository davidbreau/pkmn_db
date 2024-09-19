from B___Data.connectors import Pkmn_Database
import sqlite3

class Pokemon:
    """
    A class representing a Pokémon and managing associated CRUD operations.
    
    This class uses a database connection for each operation,
    ensuring that no connection remains open between calls.
    """

    def __init__(self, nom_pkmn):
        """
        Initialize a Pokémon object.

        Args:
            nom_pkmn (str): The name of the Pokémon, serving as a unique identifier.
        """
        self.nom_pkmn = nom_pkmn
        self.db = Pkmn_Database()

    @classmethod
    def create(cls, nom_pkmn, **kwargs):
        """
        Create a new Pokémon in the database.

        Args:
            nom_pkmn (str): The name of the Pokémon to create.
            **kwargs: Additional attributes of the Pokémon.

        Returns:
            Pokemon: An instance of the Pokémon class representing the created Pokémon.

        Raises:
            sqlite3.Error: If an error occurs during database insertion.
        """
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

    def read(self):
        """
        Read the Pokémon's data from the database.

        Returns:
            dict: A dictionary containing all the Pokémon's data.

        Raises:
            ValueError: If no Pokémon is found with the specified name.
            sqlite3.Error: If an error occurs during database reading.
        """
        connection = self.db.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Pokemons WHERE nom_pkmn = ?", (self.nom_pkmn,))
            data = cursor.fetchone()
            if data:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, data))
            else:
                raise ValueError(f"No Pokémon found with the name {self.nom_pkmn}")
        finally:
            connection.close()

    def update(self, **kwargs):
        """
        Update the Pokémon's attributes in the database.

        Args:
            **kwargs: The attributes to update and their new values.

        Raises:
            sqlite3.Error: If an error occurs during database update.
        """
        connection = self.db.connect()
        try:
            cursor = connection.cursor()
            for key, value in kwargs.items():
                cursor.execute(f"UPDATE Pokemons SET {key} = ? WHERE nom_pkmn = ?", (value, self.nom_pkmn))
            connection.commit()
        finally:
            connection.close()
            
    def delete(self):
        """
        Delete the Pokémon from the database.

        Raises:
            sqlite3.Error: If an error occurs during database deletion.
        """
        connection = self.db.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Pokemons WHERE nom_pkmn = ?", (self.nom_pkmn,))
            connection.commit()
        finally:
            connection.close()

