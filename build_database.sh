#!/bin/bash

      #  🔽 Charge les variables d'environnement de la base de données Pokemon dans le fichier .env
export $(grep -E '^(DB_USER|DB_PASSWORD)=' .env | xargs)

echo "User: $PKMN_DB_USER"
echo "Password: $PKMN_DB_PASSWORD"


# Définir les chemins
SCRIPT_DIR="A___Database_Building/A1__Pkmn_Bdd/SQL"
DB_FILE="B___Data/pkmn.db"

touch "$DB_FILE"

# Exécuter chaque script SQL
for sql_file in "$SCRIPT_DIR"/*.sql; do
    echo "Exécution de $sql_file..."
    sqlite3 "$DB_FILE" < "$sql_file" 2>&1
    if [ $? -ne 0 ]; then
        echo "Erreur lors de l'exécution de $sql_file"
    fi
done

echo "Base de données construite dans $DB_FILE."
