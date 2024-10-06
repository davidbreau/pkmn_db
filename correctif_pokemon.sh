#!/bin/bash

source venv/bin/activate
# Nom du fichier : correctif_pokemon.sh
# À placer à la racine du projet

CSV_FILE="B___Data/CSV/pokedex.csv"

# Chemin vers le fichier pokemons-v2
POKEMONS_V2_FILE="B___Data/CSV/pokemons_v2.csv"



# Changer de répertoire vers B___Data
cd B___Data || exit 1  # Quitte le script si le changement de répertoire échoue

# Exécuter un script Python en ligne pour compter les Pokémon
TOTAL_POKEMONS=$(python3 -c "
from pokemon import Pokemon
print(Pokemon.count_all())
" | tr -d '[:space:]')  # Supprime les espaces et les nouvelles lignes

# Revenir au répertoire d'origine
cd .. || exit 1  # Quitte le script si le changement de répertoire échoue


echo "Total Pokémon: $TOTAL_POKEMONS"
# Vérifiez si le nombre total de Pokémon est égal à 1150
if [ "$TOTAL_POKEMONS" -lt 1155 ]; then
    echo "Exécution du script SQL..."
    # Placez ici le code que vous souhaitez exécuter
    python3 A___Database_Building/A3__Nettoyage/correctif_pokemon_sql.py  # Exécutez votre script SQL
else
    echo "Aucune action effectuée."
fi



# Vérification de l'existence du fichier pokemons-v2
if [ ! -f "$POKEMONS_V2_FILE" ]; then
    echo "Le fichier pokemons-v2 n'existe pas. Exécution de correctif_pokemon_csv.py..."
    python3 A___Database_Building/A3__Nettoyage/correctif_pokemon_csv.py

else
    echo "Le fichier pokemons-v2 existe. Pas besoin d'exécuter correctif_pokemon_csv.py."
fi

echo "Exécution terminée."

deactivate