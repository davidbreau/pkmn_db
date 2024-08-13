# Afficher le répertoire actuel pour le débogage

source venv_pkmn/bin/activate

echo "Après cd vers le répertoire du script : $(pwd)"

# Entrer dans le sous-dossier correct
cd A___Database_Building/A2__Scraping/A2__Scraping
echo "$(pwd)"

scrapy crawl PokemonSpider

cd ../../..