# Lors du scrap, certaines exceptions n'ont pas vu leurs talents leurs formes correctement scrapés ou  (env. 49 sur 1051)
# Ce script sert à les insérer à la main

import sqlite3, pandas as pd

df = pd.read_csv('../../B___Data/CSV/pokemons.csv')

#Correction des url d'images pour raccourcir des éléments facultative comme aperçu et nombre de pixel
df.url_image = df.url_image.apply(lambda x: '/images'+x.split('/thumb')[1].split('png/')[0]+'png' if '/thumb' in x else x.split('png/')[0]+'png')#


#
##
### N.58 CANINOS
df.loc[df.nom_pkmn == 'Caninos', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Intimidation', 'Torche', 'Cœur Noble'
    ]


#
##
### N.75 Gravalanch
df.loc[df.nom_pkmn == 'Gravalanch', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Tête de Roc', 'Fermeté', 'Voile Sable'
    ]


#
##
### N.128 Tauros
#Ajout Race Combattive
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Tauros'].assign(
    nom_pkmn='Tauros de Paldéa (Race Combattive)', nom_pkmn_us='Paldean Tauros (Combat Breed)')
df.loc[len(df)-1, ['url_image', 'type_1', 'taille_m', 'poids_kg', 'talent_cache', 'points_exp', 'attaque', 'defense', 'attaque_speciale', 'vitesse']] = [
    'Tauros de Paldéa (Forme Combattive)', 'Paldean Tauros (Combat Breed)',
    '/images/9/9a/Tauros_de_Paldea_%28Race_Combative%29-EV.png',
    'Combat',
    1.4, 11.0,
    'Ruminant', '172 exp.',
    110, 105, 30, 100
    ]
#Ajout Race Flamboyante
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Tauros (Race Combattive)'].assign(
    nom_pkmn='Tauros de Paldéa (Race Flamboyante)', nom_pkmn_us='Paldean Tauros (Blaze Breed)')
df.loc[len(df)-1, ['url_image', 'type_2', 'poids_kg']] = [
    '/images/5/55/Tauros_de_Paldea_%28Race_Flamboyante%29-EV.png',
    'Feu',
    85
]
#Ajout Race Aquatique
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Tauros de Paldéa (Race Combattive)'].assign(
    nom_pkmn='Tauros de Paldéa (Race Aquatique)', nom_pkmn_us='Paldean Tauros (Aqua Breed)')
df.loc[len(df)-1, ['url_image', 'type_2', 'poids_kg']] = [
    '/images/2/28/Tauros_de_Paldea_%28Race_Aquatique%29-EV.png',
    'Eau',
    85
]


#
##
### N.75 Gravalanch
df.loc[df.nom_pkmn == 'Gravalanch', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Tête de Roc', 'Fermeté', 'Voile Sable'
    ]


#
##
### N.275 Tengalice
df.loc[df.nom_pkmn == 'Tengalice', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Chlorophylle', 'Matinal (gen :8) / Aéroporté (gen 9:)', 'Pickpocket'
    ]


#
##
### N.351 Morphéo
df.loc[df.nom_pkmn == 'Morphéo', ['nom_pkmn', 'nom_pkmn_us', 'type_1']] = [
    'Morphéo (Normale)', 'Castform (Normal)', 'Normal']
#Ajout forme solaire
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Morphéo (Normale)'].assign(
    nom_pkmn='Morphéo (Solaire)', nom_pkmn_us='Castform (Sunny)')
df.loc[len(df)-1, ['url_image', 'type_1']] = [
    '/images/f/fa/Morphéo_%28Forme_Solaire%29-USUL.png', 
    'Feu']
#Ajout forme Eau de Pluie
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Morphéo (Normale)'].assign(
    nom_pkmn='Morphéo (Eau de Pluie)', nom_pkmn_us='Castform (Rainy)')
df.loc[len(df)-1, ['url_image', 'type_1']] = [
    '/images/b/b7/Morphéo_%28Forme_Eau_de_Pluie%29-USUL.png', 
    'Eau']
#Ajout forme Blizzard
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Morphéo (Normale)'].assign(
    nom_pkmn='Morphéo (Blizzard)', nom_pkmn_us='Castform (Snowy)')
df.loc[len(df)-1, ['url_image', 'type_1']] = [
    '/images/0/08/Morphéo_%28Forme_Blizzard%29-USUL.png', 
    'Glace']


#
##
### N.386 Deoxys
df.loc[df.nom_pkmn == 'Deoxys', ['nom_pkmn', 'nom_pkmn_us',]] = [
    'Deoxys (Normale)', 'Deoxys (Normal)']
#Ajout forme Attaque
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Deoxys (Normale)'].assign(
    nom_pkmn='Deoxys (Attaque)',nom_pkmn_us='Deoxys (Attack)')
df.loc[len(df)-1, ['url_image', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale']] = [
    '/images/f/fc/Deoxys_%28Forme_Attaque%29-RFVF.png',
    180, 20, 180, 20
]
#Ajout forme Defense
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Deoxys (Normale)'].assign(
    nom_pkmn='Deoxys (Defense)',nom_pkmn_us='Deoxys (Defense)')
df.loc[len(df)-1, ['url_image', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale']] = [
    '/images/7/7c/Deoxys_%28Forme_Défense%29-RFVF.png',
    70, 160, 70, 160
]
#Ajout forme Vitesse
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Deoxys (Normale)'].assign(
    nom_pkmn='Deoxys (Vitesse)',nom_pkmn_us='Deoxys (Speed)')
df.loc[len(df)-1, ['url_image', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale']] = [
    '/images/6/63/Deoxys_%28Forme_Vitesse%29-E.png',
    95, 90, 95, 90
]


#
##
### N.393 Tiplouf
df.loc[df.nom_pkmn == 'Tiplouf', ['talent_1', 'talent_cache']] = [
    'Torrent', 'Acharné (gen :8)/ Battant (gen 9:)']

### N.394 Prinplouf
df.loc[df.nom_pkmn == 'Prinplouf', ['talent_1', 'talent_cache']] = [
    'Torrent', 'Acharné (gen :8)/ Battant (gen 9:)']

### N.395 Pingoléon
df.loc[df.nom_pkmn == 'Pingoléon', ['talent_1', 'talent_cache']] = [
    'Torrent', 'Acharné (gen :8)/ Battant (gen 9:)']


#
##
### N.413 Cheniti
df.loc[df.nom_pkmn == 'Cheniti', ['nom_pkmn', 'nom_pkmn_us']] = [
    'Cheniti (Cape Plante)', 'Cheniti (Plant Coak)']
#Ajout Cape Sable
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Cheniti (Cape Plante)'].assign(
    nom_pkmn='Cheniti (Cape Sable)', nom_pkmn_us='Burmy (Sandy Cloak)')
df.loc[len(df)-1, 'url_image'] = '/images/9/9f/Cheniti_%28Cape_Sable%29-DP.png'
#Ajout Cape Déchet
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Cheniti (Cape Plante)'].assign(
    nom_pkmn='Cheniti (Cape Déchet)', nom_pkmn_us='Burmy (Trash Cloak)')
df.loc[len(df)-1, 'url_image'] = '/images/b/bf/Cheniti_%28Cape_Déchet%29-DP.png'

### N.414 Cheniselle
df.loc[df.nom_pkmn == 'Cheniselle', ['nom_pkmn', 'nom_pkmn_us', 'type_1', 'type_2', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale']] = [
    'Cheniselle (Cape Sable)', 'Wormadam (Sandy Cloak)', 
    'Insecte', 'Sol',
    79, 105, 59, 85]
#Ajout Cape Plante
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Cheniselle (Cape Sable)'].assign(
    nom_pkmn='Cheniselle (Cape Plante)',nom_pkmn_us='Wormadam (Plant Cloak)')
df.loc[len(df)-1, ['url_image', 'type_2', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale']] = [
    '/images/4/44/Cheniselle_%28Cape_Plante%29-DP.png',
    'Plante',
    79, 105, 59, 85
]
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Cheniselle (Cape Sable)'].assign(
    nom_pkmn='Cheniselle (Cape Déchet)',nom_pkmn_us='Wormadam (Trash Cloak)')
df.loc[len(df)-1, ['url_image', 'type_2' 'attaque', 'defense', 'attaque_speciale', 'defense_speciale']] = [
    '/images/7/78/Cheniselle_%28Cape_Déchet%29-DP.png',
    69, 95, 69, 95
]


#
##
### N.479 Motisma
df.loc[df.nom_pkmn == 'Motisma', ['nom_pkmn', 'nom_pkmn_us', 'type_1', 'type_2']] = ['Motisma (Normale)', 'Rotom (Normal)', 'Électrik', 'Spectre']
#Ajout forme chaleur
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Motisma (Normale)'].assign(
    nom_pkmn='Motisma (Chaleur)', nom_pkmn_us='Rotom (Heat)')
df.loc[len(df)-1, ['url_image', 'type_2', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
    '/images/3/34/Motisma_%28Chaleur%29-Pt.png',
    'Feu',
    65, 107, 105, 107, 86
    ]
#Ajout forme Froid (Frost)
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Motisma (Chaleur)'].assign(
    nom_pkmn='Motisma (Froid)', nom_pkmn_us='Rotom (Frost)')
df.loc[len(df)-1, ['url_image', 'type_2']] = [
    '/images/0/06/Motisma_%28Froid%29-Pt.png',
    'Glace'
]
#Ajout forme Hélice (Fan)
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Motisma (Froid)'].assign(
    nom_pkmn='Motisma (Hélice)', nom_pkmn_us='Rotom (Fan)')
df.loc[len(df)-1, ['url_image', 'type_2']] = [
    '/images/6/6b/Motisma_%28Hélice%29-Pt.png',
    'Vol'
]
#Ajout forme Lavage (Wash)
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Motisma (Hélice)'].assign(
    nom_pkmn='Motisma (Lavage)', nom_pkmn_us='Rotom (Wash)')
df.loc[len(df)-1, ['url_image', 'type_2']] = [
    '/images/a/a8/Motisma_%28Lavage%29-Pt.png',
    'Eau'
]
#Ajout forme Tonte (Mow)
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Motisma (Lavage)'].assign(
    nom_pkmn='Motisma (Tonte)', nom_pkmn_us='Rotom (Mow)')
df.loc[len(df)-1, ['url_image', 'type_2']] = [
    '/images/8/81/Motisma_%28Tonte%29-Pt.png',
    'Plante'
]


#
##
### N.483 Dialga
# Ajout forme Normale
df.loc[len(df)] = [
    'Dialga (Normale)', 'Dialga (Normal)', 483, 
    '/images/e/e4/Dialga-DEPS.png', 
    '/images/0/0d/Cri_0483_HOME.ogg', 
    'Acier', 'Dragon', 
    5.4, 683.0, 
    'Pression', None, 'Télépathe', 
    'Asexué', 3, 120, 'Inconnu', None, '+3 Att. Spé', '220 Exp.', '1 250 000 exp', 
    100, 100, 120, 150, 120, 90
    ]
# Ajout forme Originelle
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Dialga (Normale)'].assign(
    nom_pkmn='Dialga (Originelle)', nom_pkmn_us='Dialga (Origin)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg', 'attaque', 'defense_speciale']] = [
    '/images/5/55/Dialga_%28Forme_Originelle%29-LPA.png',
    7.0, 850.0, 
    100, 120
]


#
##
### N.484 Palkia
# Ajout forme Normale
df.loc[len(df)] = [
    'Palkia (Normale)', 'Palkia (Normal)', 484, 
    '/images/c/c7/Palkia-DEPS.png', '/images/e/ef/Cri_0484_HOME.ogg', 
    'Acier', 'Eau', 
    4.2, 336.0, 
    'Pression', None, 'Télépathe', 
    'Asexué', 3, 120, 'Inconnu', None, '+3 Att. Spé', '220 Exp.', '1 250 000 exp', 
    90, 120, 100, 150, 120, 100
    ]
# Ajout forme Originelle
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Palkia (Normale)'].assign(
    nom_pkmn='Palkia (Originelle)', nom_pkmn_us='Palkia (Origin)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg', 'attaque', 'vitesse']] = [
    '/images/7/7f/Palkia_%28Forme_Originelle%29-LPA.png',
    7.0, 850.0, 
    100, 120
]


#
##
### N.487 Giratina
# Ajout forme Alternative
df.loc[len(df)] = [
    'Giratina (Alternative)', 'Giratina (Altered)', 487, 
    '/images/2/2d/Giratina_%28Forme_Alternative%29-DEPS.png', '/images/d/d6/Cri_0487_HOME.ogg', 
    'Spectre', 'Dragon', 
    4.5, 750.0, 
    'Pression', None, 'Télépathe', 
    'Asexué', 3, 120, 'Inconnu', None, '+3 PV', '220 Exp.', '1 250 000 exp', 
    150, 120, 100, 120, 100, 90
    ]
# Ajout forme Originelle
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Giratina (Alternative)'].assign(
    nom_pkmn='Giratina (Originelle)', nom_pkmn_us='Giratina (Origin))')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale']] = [
    '/images/f/f1/Giratina_%28Forme_Originelle%29-Pt.png',
    6.9, 650.0, 
    120, 100, 120, 100
]


#
##
### N. 492 Shaymin
# Ajout forme Terrestre
df.loc[len(df)] = [
    'Shaymin (Terrestre)', 'Shaymin (Land)', 492, 
    '/images/3/3d/Shaymin_%28Forme_Terrestre%29-DEPS.png', '/images/7/7a/Cri_0492_HOME.ogg', 
    'Plante', None, 0.2, 2.1, 'Médic Nature', None, None, 'Asexué', 45, 120, 'Inconnu', '+3 PV', '1 059 860 exp.', 
    100, 100, 100, 100, 100, 100
    ]
# Ajout forme Céleste
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Shaymin (Terrestre)'].assign(
    nom_pkmn='Shaymin (Céleste)',nom_pkmn_us='Shaymin (Sky)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'type_2', 'talent_1', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
    '/images/d/db/Shaymin_%28Forme_Céleste%29-Pt.png',
    '/images/7/76/Cri_0492_C%C3%A9leste_HOME.ogg',
    'Vol',
    'Sérénité',
    103, 75, 120, 75, 127
]


#
##
### N.524 Nodulithe
df.loc[df.nom_pkmn == 'Nodulithe', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Fermeté', 'Armurouillée (gen :7)', 'Force Sable']


#
##
### N.524 Brutapode
df.loc[df.nom_pkmn == 'Brutapode', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Point Poison', 'Essaim', 'Pied Véloce (gen 5) / Turbo (gen 6:)']



#
##
### N.545 Bargantua
# Mise à jour de Bargantua Motif Blanc
df.loc[df.nom_pkmn == 'Bargantua', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_2', 'talent_cache']] = [
    'Bargantua (Motif Blanc)', 'Basculin (White-Striped)', 
    'Phobique', 'Adaptabilité', 'Brise Moule'
]

# Ajout de Bargantua Motif Rouge
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Bargantua (Motif Blanc)'].assign(
    nom_pkmn='Bargantua (Motif Rouge)', nom_pkmn_us='Basculin (Red-Striped)')
df.loc[len(df)-1, ['url_image', 'talent_1']] = [
    '/images/5/52/Bargantua_%28Motif_Rouge%29-NB.png', 
    'Téméraire'
]

# Ajout de Bargantua Motif Bleu
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Bargantua (Motif Blanc)'].assign(
    nom_pkmn='Bargantua (Motif Bleu)', nom_pkmn_us='Basculin (Blue-Striped)')
df.loc[len(df)-1, ['url_image', 'talent_1']] = [
    '/images/7/7c/Bargantua_%28Motif_Bleu%29-NB.png', 
    'Tête de Roc'
]


#
##
### N.609 Lugulabre
df.loc[df.nom_pkmn == 'Lugulabre', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Torche', 'Corps Ardent', 'Marque Ombre (gen 5) / Infiltration (gen 6:)'
]


#
##
### N.641 Boréas
df.loc[df.nom_pkmn == 'Boréas', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_cache', 'taille_m']] = [
    'Boréas (Avatar)', 'Tornadus (Incarnate)', 'Farceur', 'Acharné', 1.5]
# Ajout Forme Totémique
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Boréas (Avatar)'].assign(
    nom_pkmn='Boréas (Totémique)', nom_pkmn_us='Tornadus (Therian)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'taille_m', 'talent_1', 'talent_cache', 'attaque', 'défense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
    '/images/a/a1/Boréas_%28Forme_Totémique%29-N2B2.png', '/images/1/1b/Cri_0641_Tot%C3%A9mique_HOME.ogg',
    1.4,
    'Régé-Force', None,
    100, 80, 110, 90, 121
]


#
##
### N.642 Fulguris
df.loc[df.nom_pkmn == 'Fulguris', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_cache', 'taille_m']] = [
    'Fulguris (Avatar)', 'Thundurus (Incarnate)', 'Farceur', 'Acharné', 1.5]

# Ajout Forme Totémique
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Fulguris (Avatar)'].assign(
    nom_pkmn='Fulguris (Totémique)', nom_pkmn_us='Thundurus (Therian)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'taille_m', 'talent_1', 'talent_cache', 'attaque', 'attaque_speciale', 'vitesse']] = [
    '/images/d/d8/Fulguris_%28Forme_Totémique%29-N2B2.png', '/images/e/ec/Cri_0642_Tot%C3%A9mique_HOME.ogg',
    3.0,
    'Absorbe-Volt', None,
    105, 145, 101
]


#
##
### N.645 Démétéros
df.loc[df.nom_pkmn == 'Démétéros', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_cache', 'taille_m']] = [
    'Démétéros (Avatar)','Landorus (Incarnate)', 'Force Sable', 'Sans Limite', 1.5]

# Ajout Forme Totémique
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Démétéros (Avatar)'].assign(nom_pkmn='Démétéros (Totémique)', nom_pkmn_us='Landorus (Therian)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'taille_m', 'talent_1', 'talent_cache', 'attaque', 'attaque_speciale', 'vitesse']] = [
    '/images/e/eb/Démétéros_%28Forme_Totémique%29-N2B2.png', '/images/a/aa/Cri_0645_Tot%C3%A9mique_HOME.ogg',
    1.3,
    'Intimidation', None,
    145, 105, 91
]


#
##
### N.658 Amphinobi
# Amphinobi Forme Normale
df.loc[df.nom_pkmn == 'Amphinobi', ['talent_1', 'talent_cache']] = [
    'Torrent', 'Protéen']
# Ajout Forme Sacha
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Amphinobi'].assign(nom_pkmn='Amphinobi (Sacha)', nom_pkmn_us='Greninja (Ash)')
df.loc[len(df)-1, ['url_image', 'talent_1', 'talent_cache', 'attaque', 'attaque_speciale', 'vitesse']] = [
    '/images/5/5c/Amphinobi_%28Forme_Sacha%29-SL.png',
    'Synergie',
    None,
    145, 153, 132
]


#
##
### N.678 Mistigrix
# Mistigrix (♂)
df.loc[df.nom_pkmn == 'Mistigrix', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_2', 'talent_cache']] = [
    'Mistigrix (♂)', 'Meowstic (♂)', 
    'Regard Vif', 'Infiltration', 'Farceur']

# Ajout Mistigrix (♀)
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Mistigrix (♂)'].assign(nom_pkmn='Mistigrix (♀)', nom_pkmn_us='Meowstic (♀)')
df.loc[len(df)-1, ['url_image', 'talent_cache']] = [
    '/images/5/57/Mistigrix_%28Femelle%29-XY.png',
    'Battant'
]


#
##
### N.710 Pitrouille
#Ajout forme Mini
df.loc[len(df)] = ['Pitrouille (Mini)', 'Pumpkaboo (Small)', 710, 
    '/images/b/b7/Sprite_0710_Mini_HOME.png', '/images/5/59/Cri_0710_HOME.ogg', 
    'Spectre', 'Plante', 
    0.3, 3.5, 
    'Ramassage', 'Fouille', 'Insomnia', 
    '50 % femelle ; 50 % mâle', 190, 20, 'Amorphe', None, '+1 Défense', '67 exp.', '1 000 000 exp.', 
    44, 66, 55, 44, 55, 56
]
# Ajout forme Normale       
df.loc[len(df)] = [df.nom_pkmn == 'Pitrouille (Mini)'].assign(
    nom_pkmn='Pitrouille (Normale)',nom_pkmn_us='Pumpkaboo (Average)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg', 'pv', 'vitesse']] = [
    '/images/b/ba/Sprite_0710_Normale_HOME.png',
    0.4, 5.0,
    49, 51
] 
#Ajout forme Maxi
df.loc[len(df)] = [df.nom_pkmn == 'Pitrouille (Mini)'].assign(
    nom_pkmn='Pitrouille (Maxi)',nom_pkmn_us='Pumpkaboo (Large)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg', 'pv', 'vitesse']] = [
    '/images/9/98/Sprite_0710_Maxi_HOME.png',
    0.5, 7.5,
    54, 46,
] 
# Ajout forme Ultra
df.loc[len(df)] = [df.nom_pkmn == 'Pitrouille (Mini)'].assign(
    nom_pkmn='Pitrouille (Ultra)',nom_pkmn_us='Pumpkaboo (Super)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'taille_m', 'poids_kg', 'pv', 'vitesse']] = [
    '/images/9/98/Sprite_0710_Maxi_HOME.png', 
    '/images/b/bf/Cri_0710_Ultra_HOME.ogg',
    0.8, 15,
    59, 41,
] 


#
##
### N.711 Banshitrouye
#Ajout forme Mini
df.loc[len(df)] = ['Banshitrouye (Mini)', 'Pumpjin (Small)', 711, 
    '/images/2/23/Sprite_0711_Mini_HOME.png', '/images/4/46/Cri_0711_HOME.ogg', 
    'Spectre', 'Plante', 
    0.7, 9.5, 
    'Ramassage', 'Fouille', 'Insomnia', 
    '50 % femelle ; 50 % mâle', 190, 20, 'Amorphe', None, '+2 Défense', '173 exp.', '1 000 000 exp.', 
    55, 85, 122, 58, 75, 99
]
# Ajout forme Normale       
df.loc[len(df)] = [df.nom_pkmn == 'Banshitrouye (Mini)'].assign(
    nom_pkmn='Banshitrouye (Normale)',nom_pkmn_us='Pumpkjin (Average)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg', 'pv', 'attaque', 'vitesse']] = [
    '/images/8/84/Sprite_0711_Normale_HOME.png',
    0.9, 12.5,
    65, 90, 84
] 
#Ajout forme Maxi
df.loc[len(df)] = [df.nom_pkmn == 'Banshitrouye (Mini)'].assign(
    nom_pkmn='Banshitrouye (Maxi)',nom_pkmn_us='Pumpjin (Large)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg', 'pv', 'attaque', 'vitesse']] = [
    '/images/c/c5/Sprite_0711_Maxi_HOME.png',
    1.1, 14.0,
    75, 95, 69
] 
# Ajout forme Ultra
df.loc[len(df)] = [df.nom_pkmn == 'Banshitrouye (Mini)'].assign(
    nom_pkmn='Banshitrouye (Ultra)',nom_pkmn_us='Pumpjin (Super)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'taille_m', 'poids_kg', 'pv', 'attaque', 'vitesse']] = [
    '/images/5/51/Sprite_0711_Ultra_HOME.png', 
    '/images/4/41/Cri_0711_Ultra_HOME.ogg',
    1.7, 39.0,
    85, 100, 54
] 


#
##
### N.718 Zygarde
#Ajout forme 10%
df.loc[len(df)] = [
    'Zygarde (10%)', 'Zygarde (10%)', 718, 
    '/images/6/63/Zygarde_%28Forme_10_%25%29-SL.png', 
    '/images/7/75/Cri_0718_10_%25_HOME.ogg',
    'Dragon', 'Sol', 
    1.2, 33.5, 
    'Aura Inversée', 'Rassemblement', None, 
    'Asexué', 3, 120, 'Inconnu', None, '+3 PV', '306 exp.', '1 250 000 exp.', 
    54, 100, 71, 61, 85, 115]
#Ajout forme 50%
df.loc[len(df)] = [df.nom_pkmn == 'Zygarde (10%)'].assign(
    nom_pkmn='Zygarde (50%)',nom_pkmn_us='Zygarde (50%)')
df.loc[len(df)-1, ["url_image", "url_cri", "taille_m", "poids_kg", "pv", "defense", "attaque_speciale", "defense_speciale", "vitesse"]] = [
    '/images/0/0b/Zygarde_%28Forme_50_%25%29-XY.png', 
    '/images/0/00/Cri_0718_50_%25_HOME.ogg',
    108, 121, 81, 95, 95
] 
#Ajout forme Parfaite
df.loc[len(df)] = [df.nom_pkmn == 'Zygarde (10%)'].assign(
    nom_pkmn='Zygarde (Complete)',nom_pkmn_us='Zygarde (Complete)')
df.loc[len(df)-1, ["url_image", "url_cri", "taille_m", "poids_kg", "pv", "defense", "attaque_speciale", "defense_speciale", "vitesse"]] = [
    '/images/5/5f/Zygarde_%28Forme_Parfaite%29-SL.png', 
    '/images/a/ae/Cri_0718_Parfaite_HOME.ogg',
    216, 121, 91, 95, 85
] 


#
##
### N.720 Hoopa
#Ajout forme Hoopa Enchaîné
df.loc[len(df)] = [
    'Hoopa (Enchaîné)', 'Hoopa (Confined)', 720, 
    '/images/0/04/Hoopa_%28Enchaîné%29-ROSA.png', '/images/4/4c/Cri_0720_HOME.ogg',
    'Psy', 'Spectre', 
    0.5, 9.0,
    'Maigicien', None, None, 
    'Asexué', 3, 120,
    'Inconnu', None, '+3 Attaque Spéciale', '270 exp.', '1 250 000 exp.', 
    80, 110, 60, 150, 130, 70
]
#Ajout forme Hoopa Déchaîné      
df.loc[len(df)] = [df.nom_pkmn == 'Hoopa (Enchaîné)'].assign(
    nom_pkmn='Hoopa (Déchaîné)',nom_pkmn_us='Hoopa (Confined)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'type_2', 'attaque', 'attaque_speciale', 'vitesse']] = [
    '/images/7/78/Hoopa_%28Déchaîné%29-ROSA.png', '/images/2/21/Cri_0720_D%C3%A9cha%C3%AEn%C3%A9_HOME.ogg',
    'Ténèbres',
    160, 150, 80
] 



#
##
### N.744 Rocabot
df.loc[df.nom_pkmn == 'Rocabot', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Regard Vif / Tempo Perso (Spécial)',  # Spécial
    'Esprit Vital',
    'Impassible'
]


#
##
### N.745 Lougaroc (Diurne)
df.loc[df.nom_pkmn == 'Lougaroc',['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_2', 'talent_cache']] = [
    'Lougaroc (Diurne)', 'Lycanroc (Midday)', 'Regard Vif', 'Esprit Vital', 'Annule Garde']
# Ajout Forme Nocturne
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Lougaroc (Diurne)'].assign(
    nom_pkmn='Lougaroc (Nocturne)', nom_pkmn_us='Lycanroc (Midnight)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'talent_1', 'talent_2', 'talent_cache', 'pv', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
    '/images/a/a4/Lougaroc_%28Forme_Nocturne%29-SL.png', 
    '/images/2/2d/Cri_0745_Nocturne_HOME.ogg',
    'Regard Vif', 'Esprit Vital', 'Annule Garde',
    85, 115, 75, 55, 75, 82
]
# Ajout Forme Crépusculaire
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Lougaroc (Diurne)'].assign(
    nom_pkmn='Lougaroc (Crépusculaire)', nom_pkmn_us='Lycanroc (Dusk)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'talent_1', 'talent_2', 'talent_cache' 'pv', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
    '/images/f/ff/Lougaroc_%28Forme_Crépusculaire%29-USUL.png', 
    '/images/f/f2/Cri_0745_Cr%C3%A9pusculaire_HOME.ogg',
    'Griffe Dure', None, None,
    75, 117, 65, 55, 65, 110
]


#
##
### N.746 Froussardine
df.loc[len(df)] = [
    'Froussardine (Solitaire)', 'Wishiwashi (Solo)', 746, 
    '/images/8/8b/Froussardine_%28Forme_Solitaire%29-SL.png', '/images/0/0a/Cri_0746_Solitaire_HOME.ogg',
    'Eau', None, 0.2, 0.3, 'Banc', None, None,
    '50 % femelle ; 50 % mâle', 60, 15, 'Aquatique 2', None, '+1 PV', '61 exp.', '800 000 epx.', 
    45, 20, 20, 25, 25, 40
    ]
       
df.loc[len(df)] = [df.nom_pkmn == 'Froussardine (Solitaire)'].assign(
    nom_pkmn='Froussardine (Banc)',nom_pkmn_us='Wishiwashi (School)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'taille_m', 'poids_kg', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
    '/images/d/d5/Froussardine_%28Forme_Banc%29-SL.png', '/images/3/36/Cri_0746_Banc_HOME.ogg',
    8.2, 78.6,
    140, 130, 140, 135, 30
] 


#
##
### N.774 Météno
df.loc[len(df)] = [
    'Météno (Météore)', 'Minior (Meteor)', 774, 
    '/images/1/1c/Météno_%28Forme_Météore%29-SL.png', '/images/0/05/Cri_0774_HOME.ogg',
    'Roche', 'Vol', 
    0.3, 40.0, 
    'Bouclier-Carcan', None, None,
    'Asexué', 30, 25, 'Minéral', None, '+1 Défense; +1 Défense Spéciale', '154 exp.', '1 059 860 exp.', 
    60, 60, 100, 60, 100, 60]      
df.loc[len(df)] = [df.nom_pkmn == 'Météno (Météore)'].assign(nom_pkmn='Météno (Noyau)',nom_pkmn_us='Minior (Core)')
df.loc[len(df)-1, ['url_image', 'poids_kg', 'points_effort', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
    '/images/c/c2/Météno_%28Noyau_Rouge%29-SL.png',
    0.3, '+1 Att.', '+1 Att. Spé',
    100, 60, 100, 60, 120
] 


#
##
### N.849 Salarsen
df.loc[df.nom_pkmn == 'Salarsen', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_2', 'talent_cache']] = [
    'Salarsen (Aïgue)', 'Toxtricity (Amped)', 
    'Punk Rock', 'Plus', 'Technicien']
#Ajout Forme Grave
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Salarsen (Aïgue)'].assign(
    nom_pkmn='Salarsen (Grave)', nom_pkmn_us='Toxtricity (Low Key)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'talent_2']] = [
    '/images8/8f/Salarsen_%28Forme_Grave%29-EB.png', '/images/6/6f/Cri_0849_Grave_HOME.ogg',
    'Moins']
#Forme Gigamax
df.loc[df.nom_pkmn == 'Salarsen Gigamax', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Punk Rock', 'Plus (forme Aïgue) / Moins (forme Grave)', 'Technicien'
]


#
##
### N.876 Wimessir
df.loc[df.nom_pkmn == 'Wimessir', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_2', 'talent_cache']] = [
    'Wimessir (♂)', 'Indeedee (♂)',
    'Tempo Perso', 'Synchro', 'Créa-Psy'
]
# Femelle
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Wimessir (♂)'].assign(nom_pkmn='Wimessir (Femelle)', nom_pkmn_us='Indeedee (♀)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'talent_1', 'pv', 'attaque', 'défense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
    '/images/1/1c/Wimessir_%28Femelle%29-EB.png', '/images/6/63/Cri_0876_%E2%99%80_HOME.ogg',
    'Attention',
    70, 55, 65, 95, 105, 85
]



#
##
### N.888 Zacian
df.loc[len(df)] = ['Zacian (Héros Aguerri)', 'Zacian (Hero of Many Battles)', 888, 
    '/images/d/dc/Zacian_%28Héros_Aguerri%29-EB.png', 
    '/images/b/b8/Cri_0888_H%C3%A9ros_Aguerri_HOME.ogg',
    'Fée', None, 
    2.8, 110.0, 
    'Lame Indomptable', None, None, 
    'Asexué', 10, 120, 'Inconnu', None, '+3 Vit.', '335 exp.', '1 250 000 exp.', 
    92, 130, 115, 80, 115, 138]
       
df.loc[len(df)] = [df.nom_pkmn == 'Zacian (Héros Aguerri)'].assign(
    nom_pkmn='Zacian (Épée Suprême)',nom_pkmn_us='Zacian (Crowned Sword)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'type_2', 'poids_kg', 'attaque', 'vitesse', ]] = [
    '/images/5/52/Zacian_%28Épée_Suprême%29-EB.png',
    '/images/5/5d/Cri_0888_%C3%89p%C3%A9e_Supr%C3%AAme_HOME.ogg', 
    'Acier',
    355.0,
    170, 148
] 



#
##
### N.889 Zamazenta
df.loc[len(df)] = ['Zamazenta (Héros Aguerri)', 'Zamazenta (Hero of Many Battles)', 889, 
    '/images/5/5a/Zamazenta_%28Héros_Aguerri%29-EB.png', 
    '/images/5/50/Cri_0889_H%C3%A9ros_Aguerri_HOME.ogg',
    'Combat', None, 
    2.9, 210.0, 
    'Égide Inflexible', None, None, 
    'Asexué', 10, 120, 'Inconnu', None, '+3 Vit.', '225 exp.', '1 250 000 exp.', 
    92, 130, 115, 80, 115, 138]
       
df.loc[len(df)] = [df.nom_pkmn == 'Zamazenta (Héros Aguerri)'].assign(nom_pkmn='Zamazenta (Bouclier Suprême)',nom_pkmn_us='Zamazenta (Crowned Shield)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'type_2', 'defense', 'defense_speciale', 'vitesse']] = [
    '/images/c/cf/Zamazenta_%28Bouclier_Suprême%29-EB.png',
    '/images/e/e9/Cri_0889_Bouclier_Supr%C3%AAme_HOME.ogg',
    'Acier',
    785.0,
    145, 145, 128
] 


#
##
### N.901 Ursaking
df.loc[len(df)] = [
    'Ursaking (Normale)', 'Ursaluna (Normal)', 901, 
    '/images/2/28/Ursaking-LPA.png', 
    '/images/2/28/Cri_0901_HOME.ogg',
    'Sol', 'Normal', 
    2.4, 290, 
    'Cran', 'Pare-Balles', 'Tension'
    '50 % femelle ; 50 % mâle', 20, 20,
    'Terrestre', None, '+3 Att.', '275 exp.', '1 000 000 exp.', 
    130, 140, 105, 45, 80, 50]
       
df.loc[len(df)] = [df.nom_pkmn == 'Ursaking (Normale)'].assign(
    nom_pkmn='Ursaking (Lune Vermeille)',nom_pkmn_us='Ursaluna  (Bloodmoon)')
df.loc[len(df)-1, [
    'url_image', 'url_cri', 'taille_m', 'poids_kg', 
    'talent_1', 'talent_2', 'talent_cache', 'sexe', 'points_effort', 
    'pv', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
    '/images/f/fb/Ursaking_%28Lune_Vermeille%29-EV.png',
    '/images/f/f6/Cri_0901_Lune_Vermeille_HOME.ogg',
    2.7, 333,
    'Œil Révélateur', None, None,
    '0 % femelle ; 100 % mâle', '+3 Att. Spé.',
    113, 70, 120, 135, 65, 52
] 


#
##
### N.905 Amovénus 
df.loc[df.nom_pkmn == 'Amovénus', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_cache', 'taille_m']] = [
    'Amovénus (Avatar)', 'Enamorus (Incarnate)'
    'Joli Sourire', 'Contestation',
    1.6
]
# Ajout forme totémique
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Amovénus (Avatar)'].assign(nom_pkmn='Amovénus (Totémique)', nom_pkmn_us='Enamorus (Therian)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'taille_m', 'talent_1', 'talent_cache', 'défense', 'défense_speciale', 'vitesse']] = [
    '/images/9/99/Amov%C3%A9nus_%28Forme_Tot%C3%A9mique%29-LPA.png', '/images/0/0b/Cri_0905_Tot%C3%A9mique_HOME.ogg',
    1.6,
    'Envelocape',
    None,
    110, 100, 46
]


#
##
### N.916 Fragrouin
# Fragrouin (♂)
df.loc[df.nom_pkmn == 'Fragrouin', ['nom_pkmn', 'nom_pkmn_us', 'url_image', 'talent_1', 'talent_2', 'talent_cache']] = [
    'Fragrouin (♂)', 'Oinkologne (♂)', 
    '/images/b/b7/Fragroin_%28M%C3%A2le%29-EV.png', 
    'Aroma-Voile', 'Gloutonnerie', 'Isograisse']
# Ajout Fragrouin (♀)
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Fragrouin (♂)'].assign(nom_pkmn='Fragrouin (♀)', nom_pkmn_us='Oinkologne (♀)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'talent_1', 'pv', 'attaque', 'défense', 'défense_speciale']] = [
    '/images/a/a0/Fragroin_%28Femelle%29-EV.png', '/images/0/0f/Cri_0916_%E2%99%80_HOME.ogg',
    'Aroma-Voile',
    115, 90, 70, 90
]


#
##
### N.925 Famignol
df.loc[len(df)] = [
    'Famignol (Famille de Trois)', 'Maushold (Family of Three)', 925, 
    '/images/5/5a/Sprite_0925_Trois_EV.png', 
    '/images/7/77/Cri_0925_Trois_HOME.ogg',
    'Normal', None, 
    0.3, 2.3, 
    'Garde-Ami', 'Bajoues', 'Technicien', 
    'Asexué', 75, 10,
    'Terrestre', 'Féerique', '+2 Vitesse', '165 exp.', '800 000 exp.', 
    74, 75, 70, 65, 75, 111]
       
df.loc[len(df)] = [df.nom_pkmn == 'Famignol (Famille de Trois)'].assign(
    nom_pkmn='Famignol (Famille de Quatre)',nom_pkmn_us='Maushold (Family of Four)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'poids_kg']] = [
    '/images/4/46/Sprite_0925_Quatre_EV.png',
    '/images/5/58/Cri_0925_Quatre_HOME.ogg',
    2.8
] 


#
##
### N.931 Tapatoès 
df.loc[df.nom_pkmn == 'Tapatoès', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Agitation', 'Intimidation', 'Cran (Plumages Vert et Bleu) / Sans Limite (Plumages Jaune et Blanc)']


#
##
### N.964 Superdofin
df.loc[len(df)] = ['Superdofin (Ordinaire)', 'Palafin (Zero)', 964, 
       '/images/b/b7/Superdofin_%28Forme_Ordinaire%29-EV.png', 
       '/images/f/f0/Cri_0963_HOME.ogg',
       'Eau', None, 
       1.3, 60.2, 
       'Supermutation', None, None, 
       '50 % femelle ; 50 % mâle', 45, 40,
       'Terrestre', 'Aquatique 2', '+2 PV', '160 Exp.', '1 250 000 exp.', 
       100, 70, 72, 53, 62, 100]
       
df.loc[len(df)] = [df.nom_pkmn == 'Superdofin (Ordinaire)'].assign(
       nom_pkmn='Superdofin (Super)',nom_pkmn_us='Palafin (Hero)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'taille_m', 'poids_kg', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale']] = [
       '/images/9/90/Superdofin_%28Forme_Super%29-EV.png',
       '/images/5/52/Cri_0964_Super_HOME.ogg',
       1.8, 97.4, 
       160, 97, 106, 87
] 


#
##
### N.982 Deusolourdo
df.loc[len(df)] = ['Deusolourdo (Double)', 'Dudunsparce (Two-Semgent)', 982, 
       '/images/c/c4/Sprite_0982_Double_HOME.png', 
       '/images/5/5a/Cri_0982_HOME.ogg',
       'Normal', None, 
       3.6, 39.2, 
       'Sérénité', 'Fuite', 'Phobique',
       '50 % femelle ; 50 % mâle', 45, 20,
       'Terrestre', None, '+2 PV', '182 exp.', '1 000 000', 
       'pv', 'attaque', 'attaque_speciale', 'defense', 'defense_speciale', 'vitesse']
       
df.loc[len(df)] = [df.nom_pkmn == 'Deusolourdo (Double)'].assign(
       nom_pkmn='Deusolourdo (Triple)',nom_pkmn_us='Dudunsparce (Three-Segment)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg']] = [
       '/images/7/71/Sprite_0982_Triple_HOME.png',
       4.5, 47.4,
] 


#
##
### N.982 Deusolourdo
df.loc[len(df)] = ['Deusolourdo (Double)', 'Dudunsparce (Two-Semgent)', 982, 
       '/images/c/c4/Sprite_0982_Double_HOME.png', 
       '/images/5/5a/Cri_0982_HOME.ogg',
       'Normal', None, 
       3.6, 39.2, 
       'Sérénité', 'Fuite', 'Phobique',
       '50 % femelle ; 50 % mâle', 45, 20,
       'Terrestre', None, '+2 PV', '182 exp.', '1 000 000', 
       'pv', 'attaque', 'attaque_speciale', 'defense', 'defense_speciale', 'vitesse']
       
df.loc[len(df)] = [df.nom_pkmn == 'Deusolourdo (Double)'].assign(
       nom_pkmn='Deusolourdo (Triple)',nom_pkmn_us='Dudunsparce (Three-Segment)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg']] = [
       '/images/7/71/Sprite_0982_Triple_HOME.png',
       4.5, 47.4,
] 


#
##
### N.999 Mordudor
df.loc[len(df)] = [
       'Mordudor (Coffre)', 'Gimmighoul (Chest)', 999, 
       '/images/b/b2/Mordudor_%28Forme_Coffre%29-EV.png', 
       '/images/0/0d/Cri_0999_Coffre_HOME.ogg',
       'Spectre', None, 
       0.3, 5.0, 
       'Phobique', None, None, 
       'Asexué', 45, 50,
       'Inconnu', None, '+1 Att. Spé', '60 exp.', '1 250 000 exp.', 
       45, 30, 25, 75, 45, 80]
       
df.loc[len(df)] = [df.nom_pkmn == 'Mordudor (Coffre)'].assign(
       nom_pkmn='Mordudor (March)',nom_pkmn_us='Gimmighoul (Roaming)')
df.loc[len(df)-1, ['url_image', 'url_cri', 'taille_m', 'poids_kg']] = [
       '/images/3/33/Mordudor_%28Forme_Marche%29-EV.png',
       '/images/8/8f/Cri_0999_Marche_HOME.ogg',
       0.1, 0.1
] 


#
##
### N.1017 Ogerpon
df.loc[df.nom_pkmn == 'Ogerpon', ['nom_pkmn', 'nom_pkmn_us', 'url_image', 'talent_1', 'talent_2']] = [
    'Ogerpon (Masque Turquoise)', 'Ogerpon (Teal Mask)',  
    '/images/8/8d/Ogerpon_%28Masque_Turquoise%29-EV.png', 
    'Acharné', 'Force Mémorielle (sous forme téracristallisée)']
# Ajout masque du puits
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Ogerpon (Masque Turquoise)'].assign(
    nom_pkmn='Ogerpon (Masque du Puits)', nom_pkmn_us='Ogerpon (Wellspring Mask)')
df.loc[len(df)-1, ['url_image', 'talent_1']] = [
    '/images/1/1d/Ogerpon_%28Masque_du_Puits%29-EV.png', 
    'Absorb-Eau']
# Ajout masque du fourneau
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Ogerpon (Masque Turquoise)'].assign(
    nom_pkmn='Ogerpon (Masque du Fourneau)', nom_pkmn_us='Ogerpon (Hearthflame Mask)')
df.loc[len(df)-1, ['url_image', 'talent_1']] = [
    '/images/2/26/Ogerpon_%28Masque_du_Fourneau%29-EV.png', 
    'Brise-Moule']
#Ajout masque de la pierre
df.loc[len(df)] = df.loc[df.nom_pkmn == 'Ogerpon (Masque Turquoise)'].assign(
    nom_pkmn='Ogerpon (Masque de la Pierre)', nom_pkmn_us='Ogerpon (Cornerstone Mask)')
df.loc[len(df)-1, ['url_image', 'talent_1']] = [
    '/images/5/54/Ogerpon_%28Masque_de_la_Pierre%29-EV.png', 'Fermeté']


#
##
### N.1024 Terapagos
#Forme Normal
df.loc[len(df)] = [
       'Terapagos (Normale)', 'Terapagos (Normal)', 1024,
       '/images/1/15/Terapagos_%28Forme_Normale%29-EV.png', 
       '/images/9/90/Cri_1024_HOME.ogg',
       'Normal', None, 
       0.2, 6.5, 
       'Téramorphose', None, None,
       '50 % femelle ; 50 % mâle', 255, None,
       'Inconnu', None, '+1 Défense', None, '1 250 000 exp.', 
       90, 65, 85, 65, 85, 60]
#Forme Téracristal
df.loc[len(df)] = [df.nom_pkmn == 'Terapagos (Normale)'].assign(nom_pkmn='Terapagos (Téracristal)',nom_pkmn_us='Terapagos (Terastal)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg', 'talent_1',
       'pv', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
       '/images/d/d4/Terapagos_%28Forme_Téracristal%29-EV.png',
       0.3, 16.0,
       'Téra-carapace',
       95, 95, 110, 105, 110, 85
] 
#Forme Stellaire
df.loc[len(df)] = [df.nom_pkmn == 'Terapagos (Normale)'].assign(nom_pkmn='Terapagos (Stellaire)',nom_pkmn_us='Terapagos (Stellar)')
df.loc[len(df)-1, ['url_image', 'taille_m', 'poids_kg', 'talent_1',
       'pv', 'attaque', 'defense', 'attaque_speciale', 'defense_speciale', 'vitesse']] = [
       '/images/3/37/Sprite_1024_Stellaire_HOME.png',
       1.7, 77.0,
       'Téraformation 0',
       160, 105, 110, 130, 110, 85
       ]
       
       
df.to_csv('../../B___Data/CSV/pokemons-v2.csv')