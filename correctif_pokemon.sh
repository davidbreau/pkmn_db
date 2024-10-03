#!/bin/bash
source venv/bin/activate
# Nom du fichier : correctif_pokemon.sh
# À placer à la racine du projet
# Chemin vers le répertoire des scripts Python
SCRIPT_DIR="A___Database_Building/A3__Nettoyage"

# Chemin vers le fichier CSV
CSV_FILE="B___Data/CSV/pokedex.csv"

# Chemin vers le fichier pokemons-v2
POKEMONS_V2_FILE="B___Data/CSV/pokemons_v2.csv"


# Exécuter un script Python en ligne pour compter les Pokémon
TOTAL_POKEMONS=$(python3 -c "
import sys
sys.path.append('B___Data')  # Ajoutez le chemin vers B___Data
from pokemon import Pokemon
print(Pokemon.count_all())
")  # Exécutez le code Python et récupérez le total

# Vérifiez si le nombre total de Pokémon est égal à 1150
if [ "$TOTAL_POKEMONS" -eq 1150 ]; then
    echo "Le nombre de Pokémon est égal à 1150. Exécution du script SQL..."
    # Placez ici le code que vous souhaitez exécuter
    python3 correctif_pokemon_sql.py  # Exécutez votre script SQL
else
    echo "Le nombre de Pokémon n'est pas égal à 1150. Aucune action effectuée."
fi


echo "Total Pokémon: $TOTAL_POKEMONS"

# Exécuter le script seulement si le total est égal à 1150
if [ "$TOTAL_POKEMONS" -eq 1150 ]; then
    echo "Le nombre de Pokémon est égal à 1150. Exécution du script..."
    # Placez ici le code que vous souhaitez exécuter
    cd $SCRIPT_DIR
    python3 correctif_pokemon_sql.py  # Exécutez votre script Python
else
    echo "Le nombre de Pokémon n'est pas égal à 1150. Aucune action effectuée."
fi


# Vérification de l'existence du fichier pokemons-v2
if [ ! -f "$POKEMONS_V2_FILE" ]; then
    echo "Le fichier pokemons-v2 n'existe pas. Exécution de correctif_pokemon_csv.py..."
    cd $SCRIPT_DIR
    python3 correctif_pokemon_csv.py
    cd -
else
    echo "Le fichier pokemons-v2 existe. Pas besoin d'exécuter correctif_pokemon_csv.py."
fi

echo "Exécution terminée."

deactivate