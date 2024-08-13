#!/bin/bash

# Chemin vers la base de données SQLite
DB_PATH="B___Data/pkmn.db"

# Vérifiez si le fichier de base de données existe
if [ ! -f "$DB_PATH" ]; then
    echo "La base de données SQLite n'existe pas à l'emplacement spécifié : $DB_PATH"
    exit 1
fi

# Commande SQL pour vider la table Pokemons
SQL_COMMAND="DELETE FROM Pokemons;"

# Exécuter la commande SQL sur la base de données SQLite
sqlite3 "$DB_PATH" "$SQL_COMMAND"

echo "La table Pokemons a été vidée."
