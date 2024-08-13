# Lors du scrap, certaines exceptions n'ont pas vu leurs talents scrapés (env. 24 sur 1051)
# Ce script sert à les insérer à la main

import sqlite3, pandas as pd

df = pd.read_csv('../../B___Data/CSV.pokemons.csv')

### N.58 Caninos
df.loc[df.nom_pkmn == 'Caninos','talent_1'] = 'Intimidation'
df.loc[df.nom_pkmn == 'Caninos','talent_2'] = 'Torche'
df.loc[df.nom_pkmn == 'Caninos','talent_caché'] = 'Cœur Noble'

### N.75 Gravalanch
df.loc[df.nom_pkmn == 'Gravalanch','talent_1'] = 'Tête de Roc'
df.loc[df.nom_pkmn == 'Gravalanch','talent_2'] = 'Fermeté'
df.loc[df.nom_pkmn == 'Gravalanch','talent_1'] = 'Voile Sable'

### N.275 Tengalice
df.loc[df.nom_pkmn == 'Tengalice','talent_1'] = 'Chlorophylle'
df.loc[df.nom_pkmn == 'Tengalice','talent_2'] = 'Matinal'
df.loc[df.nom_pkmn == 'Tengalice','talent_1'] = 'Aéroporté / Pickpocket'

### 
df.loc[df.nom_pkmn == 'NAME','talent_1'] = 'talent1'
df.loc[df.nom_pkmn == 'NAME','talent_2'] = 'talent2'
df.loc[df.nom_pkmn == 'NAME','talent_1'] = 'talentC'