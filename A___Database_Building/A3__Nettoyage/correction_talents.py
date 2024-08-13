# Lors du scrap, certaines exceptions n'ont pas vu leurs talents scrapés (env. 24 sur 1051)
# Ce script sert à les insérer à la main

import sqlite3, pandas as pd

df = pd.read_csv('../../B___Data/CSV.pokemons.csv')

