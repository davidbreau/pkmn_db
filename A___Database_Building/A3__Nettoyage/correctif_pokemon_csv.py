# Lors du scrap, certaines exceptions n'ont pas vu leurs talents leurs formes correctement scrapés ou  (env. 100 sur 1051)
# Ce script sert à les insérer à la main

import pandas as pd, sys
if '../..' not in sys.path:
    sys.path.append('../..')

df = pd.read_csv('../../B___Data/CSV/pokemons.csv')

#Correction des url d'images pour raccourcir des éléments facultative comme aperçu et nombre de pixel
df.url_image = df.url_image.apply(lambda x: '/images'+x.split('/thumb')[1].split('png/')[0]+'png' if '/thumb' in x else x.split('png/')[0]+'png')


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
tauros_race_combattive = df.loc[df.nom_pkmn == 'Tauros'].assign(
    nom_pkmn='Tauros de Paldéa (Race Combattive)', nom_pkmn_us='Paldean Tauros (Combat Breed)',
    url_image='/images/9/9a/Tauros_de_Paldea_%28Race_Combative%29-EV.png',
    type_1='Combat',
    taille_m= 1.4, poids_kg=11.0,
    talent_cache='Ruminant', points_exp='172 exp.',
    attaque=110, defense=105, attaque_speciale=30, vitesse=100
)
tauros_race_flamboyante = tauros_race_combattive.assign(
    nom_pkmn='Tauros de Paldéa (Race Flamboyante)', nom_pkmn_us='Paldean Tauros (Blaze Breed)',
    url_image='/images/5/55/Tauros_de_Paldea_%28Race_Flamboyante%29-EV.png',
    type_2='Feu',
    poids_kg=85
)
tauros_race_aquatique = tauros_race_combattive.assign(
    nom_pkmn='Tauros de Paldéa (Race Aquatique)', nom_pkmn_us='Paldean Tauros (Aqua Breed)',
    url_image='/images/2/28/Tauros_de_Paldea_%28Race_Aquatique%29-EV.png',
    type_2='Eau',
    poids_kg=85
)


#
##
### N.150 Mewtwo
mewtwo_blinde = df.loc[df.nom_pkmn == 'Mewtwo'].assign(
    nom_pkmn='Mewtwo (Blindé)', nom_pkmn_us='Mewtwo (Armored)',
    url_image='/images/e/ea/Sprite_0150_Armure_GO.png',
    talent_1 = None, talent_2 = None, talent_cache = None,
    taux_de_capture = None, points_effort = None, points_exp = None, exp_niv100 = None,
    attaque=None, defense=None, attaque_speciale=None, defense_speciale=None, vitesse=None
)


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
morpheo_solaire = df.loc[df.nom_pkmn == 'Morphéo (Normale)'].assign(
    nom_pkmn='Morphéo (Solaire)', nom_pkmn_us='Castform (Sunny)',
    url_image = '/images/f/fa/Morphéo_%28Forme_Solaire%29-USUL.png', 
    type_1 = 'Feu'
    )
#Ajout forme Eau de Pluie
morpheo_eau_de_pluie = df.loc[df.nom_pkmn == 'Morphéo (Normale)'].assign(
    nom_pkmn='Morphéo (Eau de Pluie)', nom_pkmn_us='Castform (Rainy)',
    url_image = '/images/b/b7/Morphéo_%28Forme_Eau_de_Pluie%29-USUL.png',
    type_1 = 'Eau'
    )
#Ajout forme Blizzard
morpheo_blizzard = df.loc[df.nom_pkmn == 'Morphéo (Normale)'].assign(
    nom_pkmn='Morphéo (Blizzard)', nom_pkmn_us='Castform (Snowy)',
    url_image = '/images/0/08/Morphéo_%28Forme_Blizzard%29-USUL.png', 
    type_2 = 'Glace'
    )



#
##
### N.386 Deoxys
df.loc[df.nom_pkmn == 'Deoxys', ['nom_pkmn', 'nom_pkmn_us',]] = [
    'Deoxys (Normale)', 'Deoxys (Normal)']
#Ajout forme Attaque
deoxys_attaque = df.loc[df.nom_pkmn == 'Deoxys (Normale)'].assign(
    nom_pkmn='Deoxys (Attaque)', nom_pkmn_us='Deoxys (Attack)',
    url_image='/images/f/fc/Deoxys_%28Forme_Attaque%29-RFVF.png',
    attaque=180, defense=20, attaque_speciale=180, defense_speciale=20
)
#Ajout forme Defense
deoxys_defense = df.loc[df.nom_pkmn == 'Deoxys (Normale)'].assign(
    nom_pkmn='Deoxys (Defense)', nom_pkmn_us='Deoxys (Defense)',
    url_image='/images/7/7c/Deoxys_%28Forme_Défense%29-RFVF.png',
    attaque=70, defense=160, attaque_speciale=70, defense_speciale=160
)
#Ajout forme Vitesse
deoxys_vitesse = df.loc[df.nom_pkmn == 'Deoxys (Normale)'].assign(
    nom_pkmn='Deoxys (Vitesse)', nom_pkmn_us='Deoxys (Speed)',
    url_image='/images/6/63/Deoxys_%28Forme_Vitesse%29-E.png',
    attaque=95, defense=90, attaque_speciale=95, defense_speciale=90
)


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
cheniti_cape_sable = df.loc[df.nom_pkmn == 'Cheniti (Cape Plante)'].assign(
    nom_pkmn='Cheniti (Cape Sable)', nom_pkmn_us='Burmy (Sandy Cloak)',
    url_image='/images/9/9f/Cheniti_%28Cape_Sable%29-DP.png'
)
#Ajout Cape Déchet
cheniti_cape_dechet = df.loc[df.nom_pkmn == 'Cheniti (Cape Plante)'].assign(
    nom_pkmn='Cheniti (Cape Déchet)', 
    nom_pkmn_us='Burmy (Trash Cloak)',
    url_image='/images/b/bf/Cheniti_%28Cape_Déchet%29-DP.png'
)

### N.414 Cheniselle
df.loc[df.nom_pkmn == 'Cheniselle', [
    'nom_pkmn', 'nom_pkmn_us', 
    'type_1', 'type_2', 
    'attaque', 'defense', 'attaque_speciale', 'defense_speciale']] = [
    'Cheniselle (Cape Sable)', 'Wormadam (Sandy Cloak)', 
    'Insecte', 'Sol',
    79, 105, 59, 85]
#Ajout Cape Plante
cheniselle_cape_plante = df.loc[df.nom_pkmn == 'Cheniselle (Cape Sable)'].assign(
    nom_pkmn='Cheniselle (Cape Plante)', 
    nom_pkmn_us='Wormadam (Plant Cloak)',
    url_image='/images/4/44/Cheniselle_%28Cape_Plante%29-DP.png',
    type_2='Plante',
    attaque=79, defense=105, attaque_speciale=59, defense_speciale=85
)
#Ajout Cape Déchet
cheniselle_cape_dechet = df.loc[df.nom_pkmn == 'Cheniselle (Cape Sable)'].assign(
    nom_pkmn='Cheniselle (Cape Déchet)', 
    nom_pkmn_us='Wormadam (Trash Cloak)',
    url_image='/images/7/78/Cheniselle_%28Cape_Déchet%29-DP.png',
    type_2='Acier',
    attaque=69, defense=95, attaque_speciale=69, defense_speciale=95
)


#
##
### N.479 Motisma
df.loc[df.nom_pkmn == 'Motisma', ['nom_pkmn', 'nom_pkmn_us', 'type_1', 'type_2']] = ['Motisma (Normale)', 'Rotom (Normal)', 'Électrik', 'Spectre']
# Ajout forme Chaleur
motisma_chaleur = df.loc[df.nom_pkmn == 'Motisma (Normale)'].assign(
    nom_pkmn='Motisma (Chaleur)', nom_pkmn_us='Rotom (Heat)',
    url_image='/images/3/34/Motisma_%28Chaleur%29-Pt.png',
    type_2='Feu', attaque=65, defense=107, attaque_speciale=105, defense_speciale=107, vitesse=86
)

# Ajout forme Froid (Frost)
motisma_froid = motisma_chaleur.assign(
    nom_pkmn='Motisma (Froid)', nom_pkmn_us='Rotom (Frost)',
    url_image='/images/0/06/Motisma_%28Froid%29-Pt.png',
    type_2='Glace'
)

# Ajout forme Hélice (Fan)
motisma_helice = motisma_froid.assign(
    nom_pkmn='Motisma (Hélice)', nom_pkmn_us='Rotom (Fan)',
    url_image='/images/6/6b/Motisma_%28Hélice%29-Pt.png',
    type_2='Vol'
)

# Ajout forme Lavage (Wash)
motisma_lavage = motisma_helice.assign(
    nom_pkmn='Motisma (Lavage)', nom_pkmn_us='Rotom (Wash)',
    url_image='/images/a/a8/Motisma_%28Lavage%29-Pt.png',
    type_2='Eau'
)

# Ajout forme Tonte (Mow)
motisma_tonte = motisma_lavage.assign(
    nom_pkmn='Motisma (Tonte)', nom_pkmn_us='Rotom (Mow)',
    url_image='/images/8/81/Motisma_%28Tonte%29-Pt.png',
    type_2='Plante'
)


#
##
### N.483 Dialga
# Ajout forme Normale
dialga_normale = pd.DataFrame([[
    'Dialga (Normale)', 'Dialga (Normal)', 483, 
    '/images/e/e4/Dialga-DEPS.png', 
    '/images/0/0d/Cri_0483_HOME.ogg', 
    'Acier', 'Dragon', 
    5.4, 683.0, 
    'Pression', None, 'Télépathe', 
    'Asexué', 3, 120, 'Inconnu', None, '+3 Att. Spé', '220 Exp.', '1 250 000 exp', 
    100, 100, 120, 150, 120, 90
    ]], columns=df.columns)
# Ajout forme Originelle
dialga_originelle = dialga_normale.assign(
    nom_pkmn='Dialga (Originelle)', nom_pkmn_us='Dialga (Origin)',
    url_image='/images/5/55/Dialga_%28Forme_Originelle%29-LPA.png',
    taille_m=7.0, poids_kg=850.0, 
    attaque=100, defense_speciale=120
)
#
##
### N.484 Palkia
# Ajout forme Normale
palkia_normale = pd.DataFrame([[
    'Palkia (Normale)', 'Palkia (Normal)', 484, 
    '/images/c/c7/Palkia-DEPS.png', '/images/e/ef/Cri_0484_HOME.ogg', 
    'Acier', 'Eau', 
    4.2, 336.0, 
    'Pression', None, 'Télépathe', 
    'Asexué', 3, 120, 'Inconnu', None, '+3 Att. Spé', '220 Exp.', '1 250 000 exp', 
    90, 120, 100, 150, 120, 100
    ]], columns=df.columns)
# Ajout forme Originelle
palkia_originelle = palkia_normale.assign(
    nom_pkmn='Palkia (Originelle)', 
    nom_pkmn_us='Palkia (Origin)',
    url_image='/images/7/7f/Palkia_%28Forme_Originelle%29-LPA.png',
    taille_m=7.0, poids_kg=850.0, 
    attaque=100, vitesse=120
)


#
##
### N.487 Giratina
# Ajout forme Alternative
giratina_alternative = pd.DataFrame([[
    'Giratina (Alternative)', 'Giratina (Altered)', 487, 
    '/images/2/2d/Giratina_%28Forme_Alternative%29-DEPS.png', '/images/d/d6/Cri_0487_HOME.ogg', 
    'Spectre', 'Dragon', 
    4.5, 750.0, 
    'Pression', None, 'Télépathe', 
    'Asexué', 3, 120, 'Inconnu', None, '+3 PV', '220 Exp.', '1 250 000 exp', 
    150, 120, 100, 120, 100, 90
    ]], columns=df.columns)
# Ajout forme Originelle
giratina_originelle = giratina_alternative.assign(
    nom_pkmn='Giratina (Originelle)', nom_pkmn_us='Giratina (Origin))',
    url_image='/images/f/f1/Giratina_%28Forme_Originelle%29-Pt.png',
    taille_m=6.9, poids_kg=650.0, 
    attaque=120, defense=100, attaque_speciale=120, defense_speciale=100
)


#
##
### N. 492 Shaymin
# Ajout forme Terrestre
shaymin_terrestre = pd.DataFrame([[
    'Shaymin (Terrestre)', 'Shaymin (Land)', 492, 
    '/images/3/3d/Shaymin_%28Forme_Terrestre%29-DEPS.png', '/images/7/7a/Cri_0492_HOME.ogg', 
    'Plante', None, 
    0.2, 2.1, 
    'Médic Nature', None, None, 
    'Asexué', 45, 120, 'Inconnu', None, '+3 PV', None,'1 059 860 exp.', 
    100, 100, 100, 100, 100, 100
    ]], columns=df.columns)
# Ajout forme Céleste
shaymin_celeste = shaymin_terrestre.assign(
    nom_pkmn='Shaymin (Céleste)', nom_pkmn_us='Shaymin (Sky)',
    url_image='/images/d/db/Shaymin_%28Forme_Céleste%29-Pt.png',
    url_cri='/images/7/76/Cri_0492_C%C3%A9leste_HOME.ogg',
    type_2='Vol',
    talent_1='Sérénité',
    attaque=103, defense=75, attaque_speciale=120, defense_speciale=75, vitesse=127
)


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
bargantua_motif_rouge = df.loc[df.nom_pkmn == 'Bargantua (Motif Blanc)'].assign(
    nom_pkmn='Bargantua (Motif Rouge)', nom_pkmn_us='Basculin (Red-Striped)',
    url_image='/images/5/52/Bargantua_%28Motif_Rouge%29-NB.png',
    talent_1='Téméraire'
)

# Ajout de Bargantua Motif Bleu
bargantua_motif_bleu = df.loc[df.nom_pkmn == 'Bargantua (Motif Blanc)'].assign(
    nom_pkmn='Bargantua (Motif Bleu)', nom_pkmn_us='Basculin (Blue-Striped)',
    url_image='/images/7/7c/Bargantua_%28Motif_Bleu%29-NB.png',
    talent_1='Tête de Roc'
)


#
##
### N.555 Darumacho
# Modification des formes existantes en Mode Normal
df.loc[df.nom_pkmn == 'Darumacho', ['nom_pkmn', 'nom_pkmn_us']] = ['Darumacho (Normale)', 'Darmanitan (Standard)']
# Ajout de la forme Mode Transe
darumacho_transe = df.loc[df.nom_pkmn == 'Darumacho (Normale)'].assign(
    nom_pkmn='Darumacho (Transe)',
    nom_pkmn_us='Darmanitan (Zen)',
    type_2='Psy',
    url_image='/images/0/0a/Sprite_0555_Transe_HOME.png',
    attaque=30,
    defense=105,
    attaque_speciale=140,
    defense_speciale=105,
    vitesse=55
)

# Ajout de la forme Mode Transe de Galar
df.loc[df.nom_pkmn == 'Darumacho de Galar', ['nom_pkmn', 'nom_pkmn_us']] = ['Darumacho de Galar (Normale)', 'Galarian Darmanitan (Standard)']
darumacho_galar_transe = df.loc[df.nom_pkmn == 'Darumacho de Galar (Normale)'].assign(
    nom_pkmn='Darumacho de Galar (Transe)',
    nom_pkmn_us='Galarian Darmanitan (Zen)',
    type_2='Feu',
    url_image='/images/a/a6/Sprite_0555_Galar_Transe_HOME.png',
    attaque=160,
    vitesse=135
)


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
boreas_totemique = df.loc[df.nom_pkmn == 'Boréas (Avatar)'].assign(
    nom_pkmn='Boréas (Totémique)', nom_pkmn_us='Tornadus (Therian)',
    url_image='/images/a/a1/Boréas_%28Forme_Totémique%29-N2B2.png',
    url_cri='/images/1/1b/Cri_0641_Tot%C3%A9mique_HOME.ogg',
    taille_m=1.4,
    talent_1='Régé-Force', talent_cache=None,
    attaque=100, defense=80, attaque_speciale=110, defense_speciale=90, vitesse=121
)


#
##
### N.642 Fulguris
df.loc[df.nom_pkmn == 'Fulguris', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_cache', 'taille_m']] = [
    'Fulguris (Avatar)', 'Thundurus (Incarnate)', 'Farceur', 'Acharné', 1.5]

# Ajout Forme Totémique
fulguris_totemique = df.loc[df.nom_pkmn == 'Fulguris (Avatar)'].assign(
    nom_pkmn='Fulguris (Totémique)', nom_pkmn_us='Thundurus (Therian)',
    url_image='/images/d/d8/Fulguris_%28Forme_Totémique%29-N2B2.png',
    url_cri='/images/e/ec/Cri_0642_Tot%C3%A9mique_HOME.ogg',
    taille_m=3.0,
    talent_1='Absorbe-Volt', talent_cache=None,
    attaque=105, attaque_speciale=145, vitesse=101
)


#
##
### N.645 Démétéros
df.loc[df.nom_pkmn == 'Démétéros', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_cache', 'taille_m']] = [
    'Démétéros (Avatar)','Landorus (Incarnate)', 'Force Sable', 'Sans Limite', 1.5]

# Ajout Forme Totémique
demeteros_totemique = df.loc[df.nom_pkmn == 'Démétéros (Avatar)'].assign(
    nom_pkmn='Démétéros (Totémique)', nom_pkmn_us='Landorus (Therian)',
    url_image='/images/e/eb/Démétéros_%28Forme_Totémique%29-N2B2.png',
    url_cri='/images/a/aa/Cri_0645_Tot%C3%A9mique_HOME.ogg',
    taille_m=1.3,
    talent_1='Intimidation', talent_cache=None,
    attaque=145, attaque_speciale=105, vitesse=91
)



#
##
### N.648 Meloetta
# Modification de la forme existante en Forme Chant
df.loc[df.nom_pkmn == 'Meloetta', ['nom_pkmn', 'nom_pkmn_us']] = [
    'Meloetta (Forme Chant)', 'Meloetta (Aria Forme)']

# Ajout de la Forme Danse
meloetta_danse = df.loc[df.nom_pkmn == 'Meloetta (Chant)'].assign(
    nom_pkmn='Meloetta (Danse)',
    nom_pkmn_us='Meloetta (Pirouette)',
    url_image='/images/3/3a/Meloetta_%28Forme_Danse%29-N2B2.png',
    type_1='Normal', type_2='Combat',
    attaque=128, defense=90, attaque_speciale=77, defense_speciale=77, vitesse=128
)


#
##
### N.658 Amphinobi
# Amphinobi Forme Normale
df.loc[df.nom_pkmn == 'Amphinobi', ['talent_1', 'talent_cache']] = [
    'Torrent', 'Protéen']
# Ajout Forme Sacha
amphinobi_sacha = df.loc[df.nom_pkmn == 'Amphinobi'].assign(
    nom_pkmn='Amphinobi (Sacha)', nom_pkmn_us='Greninja (Ash)',
    url_image='/images/5/5c/Amphinobi_%28Forme_Sacha%29-SL.png',
    talent_1='Synergie', talent_cache=None,
    attaque=145, attaque_speciale=153, vitesse=132
)


#
##
### N.678 Mistigrix
# Mistigrix (♂)
df.loc[df.nom_pkmn == 'Mistigrix', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_2', 'talent_cache']] = [
    'Mistigrix (♂)', 'Meowstic (♂)', 
    'Regard Vif', 'Infiltration', 'Farceur']

# Ajout Mistigrix (♀)
mistigrix_femelle = df.loc[df.nom_pkmn == 'Mistigrix (♂)'].assign(
    nom_pkmn='Mistigrix (♀)', nom_pkmn_us='Meowstic (♀)',
    url_image='/images/5/57/Mistigrix_%28Femelle%29-XY.png',
    talent_cache='Battant'
)


#
##
### N.682 Exagide
# Modification de la forme existante en Forme Parade
df.loc[df.nom_pkmn == 'Exagide', ['nom_pkmn', 'nom_pkmn_us', 'defense', 'defense_speciale']] = [
    'Exagide (Parade)', 'Aegislash (Shield)', 140, 140]

# Ajout de la Forme Assaut
exagide_assaut = df.loc[df.nom_pkmn == 'Exagide (Parade)'].assign(
    nom_pkmn='Exagide (Assaut)', nom_pkmn_us='Aegislash (Blade)',
    url_image='/images/4/44/Exagide_%28Forme_Assaut%29-XY.png',
    attaque=140, defense=50, attaque_speciale=140, defense_speciale=50
)
#
##
### N.710 Pitrouille
# Ajout forme Mini
pitrouille_mini = pd.DataFrame([[
    'Pitrouille (Mini)', 'Pumpkaboo (Small)', 710, 
    '/images/b/b7/Sprite_0710_Mini_HOME.png', '/images/5/59/Cri_0710_HOME.ogg', 
    'Spectre', 'Plante', 
    0.3, 3.5, 
    'Ramassage', 'Fouille', 'Insomnia', 
    '50 % femelle ; 50 % mâle', 190, 20, 'Amorphe', None, '+1 Défense', '67 exp.', '1 000 000 exp.', 
    44, 66, 55, 44, 55, 56
]], columns=df.columns)

# Ajout forme Normale
pitrouille_normale = pitrouille_mini.assign(
    nom_pkmn='Pitrouille (Normale)', nom_pkmn_us='Pumpkaboo (Average)',
    url_image='/images/b/ba/Sprite_0710_Normale_HOME.png',
    taille_m=0.4, poids_kg=5.0,
    pv=49, vitesse=51
)

# Ajout forme Maxi
pitrouille_maxi = pitrouille_mini.assign(
    nom_pkmn='Pitrouille (Maxi)', nom_pkmn_us='Pumpkaboo (Large)',
    url_image='/images/9/98/Sprite_0710_Maxi_HOME.png',
    taille_m=0.5, poids_kg=7.5,
    pv=54, vitesse=46
)

# Ajout forme Ultra
pitrouille_ultra = pitrouille_mini.assign(
    nom_pkmn='Pitrouille (Ultra)', nom_pkmn_us='Pumpkaboo (Super)',
    url_image='/images/9/98/Sprite_0710_Maxi_HOME.png',
    url_cri='/images/b/bf/Cri_0710_Ultra_HOME.ogg',
    taille_m=0.8, poids_kg=15,
    pv=59, vitesse=41
)


#
##
### N.711 Banshitrouye
# Ajout forme Mini
banshitrouye_mini = pd.DataFrame([[
    'Banshitrouye (Mini)', 'Pumpjin (Small)', 711, 
    '/images/2/23/Sprite_0711_Mini_HOME.png', '/images/4/46/Cri_0711_HOME.ogg', 
    'Spectre', 'Plante', 
    0.7, 9.5, 
    'Ramassage', 'Fouille', 'Insomnia', 
    '50 % femelle ; 50 % mâle', 190, 20, 'Amorphe', None, '+2 Défense', '173 exp.', '1 000 000 exp.', 
    55, 85, 122, 58, 75, 99
]], columns=df.columns)

# Ajout forme Normale
banshitrouye_normale = banshitrouye_mini.assign(
    nom_pkmn='Banshitrouye (Normale)', nom_pkmn_us='Pumpkjin (Average)',
    url_image='/images/8/84/Sprite_0711_Normale_HOME.png',
    taille_m=0.9, poids_kg=12.5,
    pv=65, attaque=90, vitesse=84
)

# Ajout forme Maxi
banshitrouye_maxi = banshitrouye_mini.assign(
    nom_pkmn='Banshitrouye (Maxi)', nom_pkmn_us='Pumpjin (Large)',
    url_image='/images/c/c5/Sprite_0711_Maxi_HOME.png',
    taille_m=1.1, poids_kg=14.0,
    pv=75, attaque=95, vitesse=69
)

# Ajout forme Ultra
banshitrouye_ultra = banshitrouye_mini.assign(
    nom_pkmn='Banshitrouye (Ultra)', nom_pkmn_us='Pumpjin (Super)',
    url_image='/images/5/51/Sprite_0711_Ultra_HOME.png',
    url_cri='/images/4/41/Cri_0711_Ultra_HOME.ogg',
    taille_m=1.7, poids_kg=39.0,
    pv=85, attaque=100, vitesse=54
)


#
##
### N.718 Zygarde
# Ajout forme 10%
zygarde_10 = pd.DataFrame([[
    'Zygarde (10%)', 'Zygarde (10%)', 718, 
    '/images/6/63/Zygarde_%28Forme_10_%25%29-SL.png', 
    '/images/7/75/Cri_0718_10_%25_HOME.ogg',
    'Dragon', 'Sol', 
    1.2, 33.5, 
    'Aura Inversée', 'Rassemblement', None, 
    'Asexué', 3, 120, 'Inconnu', None, '+3 PV', '306 exp.', '1 250 000 exp.', 
    54, 100, 71, 61, 85, 115
]], columns=df.columns)

# Ajout forme 50%
zygarde_50 = zygarde_10.assign(
    nom_pkmn='Zygarde (50%)', nom_pkmn_us='Zygarde (50%)',
    url_image='/images/0/0b/Zygarde_%28Forme_50_%25%29-XY.png', 
    url_cri='/images/0/00/Cri_0718_50_%25_HOME.ogg',
    taille_m=108, poids_kg=121,
    pv=81, defense=95, attaque_speciale=95, defense_speciale=95, vitesse=95
)

# Ajout forme Parfaite
zygarde_parfaite = zygarde_10.assign(
    nom_pkmn='Zygarde (Complete)', nom_pkmn_us='Zygarde (Complete)',
    url_image='/images/5/5f/Zygarde_%28Forme_Parfaite%29-SL.png', 
    url_cri='/images/a/ae/Cri_0718_Parfaite_HOME.ogg',
    taille_m=216, poids_kg=121,
    pv=91, defense=95, attaque_speciale=85, defense_speciale=95, vitesse=85
)


#
##
### N.720 Hoopa
# Ajout forme Hoopa Enchaîné
hoopa_enchaine = pd.DataFrame([[
    'Hoopa (Enchaîné)', 'Hoopa (Confined)', 720, 
    '/images/0/04/Hoopa_%28Enchaîné%29-ROSA.png', '/images/4/4c/Cri_0720_HOME.ogg',
    'Psy', 'Spectre', 
    0.5, 9.0,
    'Maigicien', None, None, 
    'Asexué', 3, 120,
    'Inconnu', None, '+3 Attaque Spéciale', '270 exp.', '1 250 000 exp.', 
    80, 110, 60, 150, 130, 70
]], columns=df.columns)

# Ajout forme Hoopa Déchaîné      
hoopa_dechaine = hoopa_enchaine.assign(
    nom_pkmn='Hoopa (Déchaîné)', nom_pkmn_us='Hoopa (Confined)',
    url_image='/images/7/78/Hoopa_%28Déchaîné%29-ROSA.png',
    url_cri='/images/2/21/Cri_0720_D%C3%A9cha%C3%AFn%C3%A9_HOME.ogg',
    type_2='Ténèbres',
    attaque=160, attaque_speciale=150, vitesse=80
)



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
lougaroc_nocturne = df.loc[df.nom_pkmn == 'Lougaroc (Diurne)'].assign(
    nom_pkmn='Lougaroc (Nocturne)', nom_pkmn_us='Lycanroc (Midnight)',
    url_image='/images/a/a4/Lougaroc_%28Forme_Nocturne%29-SL.png',
    url_cri='/images/2/2d/Cri_0745_Nocturne_HOME.ogg',
    pv=85, attaque=115, defense=75, attaque_speciale=55, defense_speciale=75, vitesse=82
)
# Ajout Forme Crépusculaire
lougaroc_crepusculaire = df.loc[df.nom_pkmn == 'Lougaroc (Diurne)'].assign(
    nom_pkmn='Lougaroc (Crépusculaire)', nom_pkmn_us='Lycanroc (Dusk)',
    url_image='/images/f/ff/Lougaroc_%28Forme_Cr%C3%A9pusculaire%29-USUL.png',
    url_cri='/images/f/f2/Cri_0745_Cr%C3%A9pusculaire_HOME.ogg',
    talent_1='Griffe Dure', talent_2=None, talent_cache=None,
    pv=75, attaque=117, defense=65, attaque_speciale=55, defense_speciale=65, vitesse=110
)


#
##
### N.741 Plumeline
#
##
### N.741 Plumeline
# Modification de la forme existante en Style Flamenco
df.loc[df.nom_pkmn == 'Plumeline', [
    'nom_pkmn', 'nom_pkmn_us', 'url_image', 'type_1', 'type_2'
]] = [
    'Plumeline (Flamenco)', 'Oricorio (Baile Style)', 
    '/images/0/00/Plumeline_%28Style_Flamenco%29-SL.png',
    'Feu', 'Vol'
]

# Ajout de la forme Pom-Pom
plumeline_pompom = df.loc[df.nom_pkmn == 'Plumeline (Flamenco)'].assign(
    nom_pkmn='Plumeline (Pom-Pom)',nom_pkmn_us='Oricorio (Pom-Pom)',
    type_1='Électrik',
    url_image='/images/4/45/Plumeline_%28Style_Pom-Pom%29-SL.png',
    url_cri='/images/7/75/Cri_0741_Pom-Pom_HOME.ogg'
)

# Ajout de la forme Hula
plumeline_hula = df.loc[df.nom_pkmn == 'Plumeline (Flamenco)'].assign(
    nom_pkmn='Plumeline (Hula)',nom_pkmn_us="Oricorio (Pa'u)",
    type_1='Psy',
    url_image='/images/f/fb/Plumeline_%28Style_Hula%29-SL.png',
    url_cri='/images/a/a1/Cri_0741_Hula_HOME.ogg'
)

# Ajout de la forme Buyō
plumeline_buyo = df.loc[df.nom_pkmn == 'Plumeline (Flamenco)'].assign(
    nom_pkmn='Plumeline (Buyō)', nom_pkmn_us='Oricorio (Sensu)',
    type_1='Spectre',
    url_image='/images/a/ae/Plumeline_%28Style_Buyō%29-SL.png',
    url_cri='/images/e/ea/Cri_0741_Buy%C5%8D_HOME.ogg'
)


#
##
### N.746 Froussardine
#Forme solitaire
froussardine_solitaire = pd.DataFrame([[
    'Froussardine (Solitaire)', 'Wishiwashi (Solo)', 746, 
    '/images/8/8b/Froussardine_%28Forme_Solitaire%29-SL.png', '/images/0/0a/Cri_0746_Solitaire_HOME.ogg',
    'Eau', None, 0.2, 0.3, 'Banc', None, None,
    '50 % femelle ; 50 % mâle', 60, 15, 'Aquatique 2', None, '+1 PV', '61 exp.', '800 000 epx.', 
    45, 20, 20, 25, 25, 40
    ]], columns=df.columns
)
#forme banc
froussardine_banc = froussardine_solitaire.assign(
    nom_pkmn='Froussardine (Banc)', nom_pkmn_us='Wishiwashi (School)',
    url_image='/images/d/d5/Froussardine_%28Forme_Banc%29-SL.png',
    url_cri='/images/3/36/Cri_0746_Banc_HOME.ogg',
    taille_m=8.2, poids_kg=78.6,
    attaque=140, defense=130, attaque_speciale=140, defense_speciale=135, vitesse=30
)


#
##
### N.774 Météno
#Forme meteore
meteno_meteore = pd.DataFrame([[
    'Météno (Météore)', 'Minior (Meteor)', 774, 
    '/images/1/1c/Météno_%28Forme_Météore%29-SL.png', '/images/0/05/Cri_0774_HOME.ogg',
    'Roche', 'Vol', 
    0.3, 40.0, 
    'Bouclier-Carcan', None, None,
    'Asexué', 30, 25, 'Minéral', None, '+1 Défense; +1 Défense Spéciale', '154 exp.', '1 059 860 exp.', 
    60, 60, 100, 60, 100, 60
]], columns=df.columns)
#Forme noyau
meteno_noyau = meteno_meteore.assign(
    nom_pkmn='Météno (Noyau)', nom_pkmn_us='Minior (Core)',
    url_image='/images/c/c2/Météno_%28Noyau_Rouge%29-SL.png',
    poids_kg=0.3, points_effort='+1 Att.;+1 Att. Spé',
    attaque=100, defense=60, attaque_speciale=100, defense_speciale=60, vitesse=120
)


#
##
### N.849 Salarsen
df.loc[df.nom_pkmn == 'Salarsen', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_2', 'talent_cache']] = [
    'Salarsen (Aïgue)', 'Toxtricity (Amped)', 
    'Punk Rock', 'Plus', 'Technicien']
#Ajout Forme Grave
salarsen_grave = df.loc[df.nom_pkmn == 'Salarsen (Aïgue)'].assign(
    nom_pkmn='Salarsen (Grave)', nom_pkmn_us='Toxtricity (Low Key)',
    url_image='/images/8/8f/Salarsen_%28Forme_Grave%29-EB.png',
    url_cri='/images/6/6f/Cri_0849_Grave_HOME.ogg',
    talent_2='Moins'
)
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
wimessir_femelle = df.loc[df.nom_pkmn == 'Wimessir (♂)'].assign(
    nom_pkmn='Wimessir (♀)', nom_pkmn_us='Indeedee (♀)',
    url_image='/images/1/1c/Wimessir_%28Femelle%29-EB.png',
    url_cri='/images/6/63/Cri_0876_%E2%99%80_HOME.ogg',
    talent_1='Attention',
    pv=70, attaque=55, defense=65, attaque_speciale=95, defense_speciale=105, vitesse=85
)


#
##
### N.888 Zacian
#Forme Heros Aguerri
zacian_heros_aguerri = pd.DataFrame([[
    'Zacian (Héros Aguerri)', 'Zacian (Hero of Many Battles)', 888, 
    '/images/d/dc/Zacian_%28Héros_Aguerri%29-EB.png', 
    '/images/b/b8/Cri_0888_H%C3%A9ros_Aguerri_HOME.ogg',
    'Fée', None, 
    2.8, 110.0, 
    'Lame Indomptable', None, None, 
    'Asexué', 10, 120, 'Inconnu', None, '+3 Vit.', '335 exp.', '1 250 000 exp.', 
    92, 130, 115, 80, 115, 138
]], columns=df.columns)
#Forme epee supreme
zacian_epee_supreme = zacian_heros_aguerri.assign(
    nom_pkmn='Zacian (Épée Suprême)', nom_pkmn_us='Zacian (Crowned Sword)',
    url_image='/images/5/52/Zacian_%28Épée_Suprême%29-EB.png',
    url_cri='/images/5/5d/Cri_0888_%C3%89p%C3%A9e_Supr%C3%AAme_HOME.ogg',
    type_2='Acier',
    poids_kg=355.0,
    attaque=170, vitesse=148
)


#
##
### N.889 Zamazenta
#Forme Heros Aguerri
zamazenta_heros_aguerri = pd.DataFrame([[
    'Zamazenta (Héros Aguerri)', 'Zamazenta (Hero of Many Battles)', 889, 
    '/images/5/5a/Zamazenta_%28Héros_Aguerri%29-EB.png', 
    '/images/5/50/Cri_0889_H%C3%A9ros_Aguerri_HOME.ogg',
    'Combat', None, 
    2.9, 210.0, 
    'Égide Inflexible', None, None, 
    'Asexué', 10, 120, 'Inconnu', None, '+3 Vit.', '225 exp.', '1 250 000 exp.', 
    92, 130, 115, 80, 115, 138
]], columns=df.columns)
#Forme Bouclier supreme
zamazenta_bouclier_supreme = zamazenta_heros_aguerri.assign(
    nom_pkmn='Zamazenta (Bouclier Suprême)', nom_pkmn_us='Zamazenta (Crowned Shield)',
    url_image='/images/c/cf/Zamazenta_%28Bouclier_Suprême%29-EB.png',
    url_cri='/images/e/e9/Cri_0889_Bouclier_Supr%C3%AAme_HOME.ogg',
    type_2='Acier',
    poids_kg=785.0,
    defense=145, defense_speciale=145, vitesse=128
)


#
##
### N.892 Shifours
# Modification de la forme existante en Style Poing Final
df.loc[df.nom_pkmn == 'Shifours', [
    'nom_pkmn', 'nom_pkmn_us', 'type_1','type_2', 'url_image'
]] = [
    'Shifours (Style Poing Final)', 'Urshifu (Single Strike)', 
    'Combat','Ténèbres', 
    '/images/7/73/Shifours_%28Style_Poing_Final%29-EB.png'
]

# Ajout de la forme Style Mille Poings
shifours_mille_poings = df.loc[df.nom_pkmn == 'Shifours (Style Poing Final)'].assign(
    nom_pkmn='Shifours (Style Mille Poings)',
    nom_pkmn_us='Urshifu (Rapid Strike)',
    type_2='Eau',
    url_image='/images/a/ac/Shifours_%28Style_Mille_Poings%29-EB.png',
    url_cri='/images/8/88/Cri_0892_Mille_Poings_HOME.ogg'
)

# Changements forme Gigamax

df.loc[df.nom_pkmn == 'Shifours Gigamax', [
    'nom_pkmn', 'nom_pkmn_us', 'type_1','type_2', 'url_image', 'taille_m'
]] = [
    'Shifours Gigamax(Style Poing Final)', 'Urshifu (Single Strike)', 
    'Combat','Ténèbres', 
    '/images/8/8c/Shifours_Gigamax_%28Style_Poing_Final%29-EB.png',
    29.0
]

shifours_gigamax_mille_poings = df.loc[df.nom_pkmn == 'Shifours Gigamax (Style Poing Final)'].assign(
    nom_pkmn='Shifours Gigamax (Style Mille Poings)',
    nom_pkmn_us='Urshifu (Rapid Strike)',
    type_2='Eau',
    url_image='/images/8/8c/Shifours_Gigamax_%28Style_Poing_Final%29-EB.png',
    url_cri='/images/6/69/Cri_0892_Gigamax_Mille_Poings_HOME.ogg',
    taille_m=26.0
)



#
##
### N.901 Ursaking
#forme normale
ursaking_normale = pd.DataFrame([[
    'Ursaking (Normale)', 'Ursaluna (Normal)', 901, 
    '/images/2/28/Ursaking-LPA.png', 
    '/images/2/28/Cri_0901_HOME.ogg',
    'Sol', 'Normal', 
    2.4, 290, 
    'Cran', 'Pare-Balles', 'Tension',
    '50 % femelle ; 50 % mâle', 20, 20,
    'Terrestre', None, '+3 Att.', '275 exp.', '1 000 000 exp.', 
    130, 140, 105, 45, 80, 50
]], columns=df.columns)
#Forme Lune Vermeille
ursaking_lune_vermeille = ursaking_normale.assign(
    nom_pkmn='Ursaking (Lune Vermeille)', nom_pkmn_us='Ursaluna (Bloodmoon)',
    url_image='/images/f/fb/Ursaking_%28Lune_Vermeille%29-EV.png',
    url_cri='/images/f/f6/Cri_0901_Lune_Vermeille_HOME.ogg',
    taille_m=2.7, poids_kg=333,
    talent_1='Œil Révélateur', talent_2=None, talent_cache=None,
    sexe='0 % femelle ; 100 % mâle', points_effort='+3 Att. Spé.',
    pv=113, attaque=70, defense=120, attaque_speciale=135, defense_speciale=65, vitesse=52
)


#
##
### N.905 Amovénus 
df.loc[df.nom_pkmn == 'Amovénus', ['nom_pkmn', 'nom_pkmn_us', 'talent_1', 'talent_cache', 'taille_m']] = [
    'Amovénus (Avatar)', 'Enamorus (Incarnate)',
    'Joli Sourire', 'Contestation',
    1.6
]
# Ajout forme totémique
amovenus_totemique = df.loc[df.nom_pkmn == 'Amovénus (Avatar)'].assign(
    nom_pkmn='Amovénus (Totémique)', nom_pkmn_us='Enamorus (Therian)',
    url_image='/images/9/99/Amov%C3%A9nus_%28Forme_Tot%C3%A9mique%29-LPA.png',
    url_cri='/images/0/0b/Cri_0905_Tot%C3%A9mique_HOME.ogg',
    taille_m=1.6, 
    talent_1='Envelocape',
    talent_cache=None,
    defense=110, defense_speciale=100, vitesse=46
)


#
##
### N.916 Fragrouin
# Fragrouin (♂)
df.loc[df.nom_pkmn == 'Fragrouin', ['nom_pkmn', 'nom_pkmn_us', 'url_image', 'talent_1', 'talent_2', 'talent_cache']] = [
    'Fragrouin (♂)', 'Oinkologne (♂)', 
    '/images/b/b7/Fragroin_%28M%C3%A2le%29-EV.png', 
    'Aroma-Voile', 'Gloutonnerie', 'Isograisse']
# Ajout Fragrouin (♀)
fragrouin_femelle = df.loc[df.nom_pkmn == 'Fragrouin (♂)'].assign(
    nom_pkmn='Fragrouin (♀)', nom_pkmn_us='Oinkologne (♀)',
    url_image='/images/a/a0/Fragroin_%28Femelle%29-EV.png',
    url_cri='/images/0/0f/Cri_0916_%E2%99%80_HOME.ogg',
    pv=115, attaque=90, defense=70, defense_speciale=90
)


#
##
### N.925 Famignol
# Ajout forme Famille de Trois
famignol_famille_de_trois = pd.DataFrame([[
    'Famignol (Famille de Trois)', 'Maushold (Family of Three)', 925, 
    '/images/5/5a/Sprite_0925_Trois_EV.png', 
    '/images/7/77/Cri_0925_Trois_HOME.ogg',
    'Normal', None, 
    0.3, 2.3, 
    'Garde-Ami', 'Bajoues', 'Technicien', 
    'Asexué', 75, 10,
    'Terrestre', 'Féerique', '+2 Vitesse', '165 exp.', '800 000 exp.', 
    74, 75, 70, 65, 75, 111
]], columns=df.columns)
# Ajout forme Famille de Quatre
famignol_famille_de_quatre = famignol_famille_de_trois.assign(
    nom_pkmn='Famignol (Famille de Quatre)', nom_pkmn_us='Maushold (Family of Four)',
    url_image='/images/4/46/Sprite_0925_Quatre_EV.png',
    url_cri='/images/5/58/Cri_0925_Quatre_HOME.ogg',
    poids_kg=2.8
)


#
##
### N.931 Tapatoès 
df.loc[df.nom_pkmn == 'Tapatoès', ['talent_1', 'talent_2', 'talent_cache']] = [
    'Agitation', 'Intimidation', 'Cran (Plumages Vert et Bleu) / Sans Limite (Plumages Jaune et Blanc)']


#
##
### N.964 Superdofin
#Forme ordinaire
superdofin_ordinaire = pd.DataFrame([[
    'Superdofin (Ordinaire)', 'Palafin (Zero)', 964, 
    '/images/b/b7/Superdofin_%28Forme_Ordinaire%29-EV.png', 
    '/images/f/f0/Cri_0963_HOME.ogg',
    'Eau', None, 
    1.3, 60.2, 
    'Supermutation', None, None, 
    '50 % femelle ; 50 % mâle', 45, 40,
    'Terrestre', 'Aquatique 2', '+2 PV', '160 Exp.', '1 250 000 exp.', 
    100, 70, 72, 53, 62, 100
]], columns=df.columns)
#Forme Super
superdofin_super = superdofin_ordinaire.assign(
    nom_pkmn='Superdofin (Super)', nom_pkmn_us='Palafin (Hero)',
    url_image='/images/9/90/Superdofin_%28Forme_Super%29-EV.png',
    url_cri='/images/5/52/Cri_0964_Super_HOME.ogg',
    taille_m=1.8, poids_kg=97.4,
    attaque=160, defense=97, attaque_speciale=106, defense_speciale=87
)


#
##
### N.982 Deusolourdo
# Ajout forme Double
deusolourdo_double = pd.DataFrame([[
    'Deusolourdo (Double)', 'Dudunsparce (Two-Segment)', 982, 
    '/images/c/c4/Sprite_0982_Double_HOME.png', 
    '/images/5/5a/Cri_0982_HOME.ogg',
    'Normal', None, 
    3.6, 39.2, 
    'Sérénité', 'Fuite', 'Phobique',
    '50 % femelle ; 50 % mâle', 45, 20,
    'Terrestre', None, '+2 PV', '182 exp.', '1 000 000', 
    'pv', 'attaque', 'attaque_speciale', 'defense', 'defense_speciale', 'vitesse'
]], columns=df.columns)
# Ajout forme Triple
deusolourdo_triple = deusolourdo_double.assign(
    nom_pkmn='Deusolourdo (Triple)', nom_pkmn_us='Dudunsparce (Three-Segment)',
    url_image='/images/7/71/Sprite_0982_Triple_HOME.png',
    taille_m=4.5, poids_kg=47.4
)


#
##
### N.999 Mordudor
#Forme coffre
mordudor_coffre = pd.DataFrame([[
    'Mordudor (Coffre)', 'Gimmighoul (Chest)', 999, 
    '/images/b/b2/Mordudor_%28Forme_Coffre%29-EV.png', 
    '/images/0/0d/Cri_0999_Coffre_HOME.ogg',
    'Spectre', None, 
    0.3, 5.0, 
    'Phobique', None, None, 
    'Asexué', 45, 50,
    'Inconnu', None, '+1 Att. Spé', '60 exp.', '1 250 000 exp.', 
    45, 30, 25, 75, 45, 80
]], columns=df.columns)
# Ajout forme Marche
mordudor_marche = mordudor_coffre.assign(
    nom_pkmn='Mordudor (March)', nom_pkmn_us='Gimmighoul (Roaming)',
    url_image='/images/3/33/Mordudor_%28Forme_Marche%29-EV.png',
    url_cri='/images/8/8f/Cri_0999_Marche_HOME.ogg',
    taille_m=0.1, poids_kg=0.1
)


#
##
### N.1017 Ogerpon
df.loc[df.nom_pkmn == 'Ogerpon', ['nom_pkmn', 'nom_pkmn_us', 'url_image', 'talent_1', 'talent_2']] = [
    'Ogerpon (Masque Turquoise)', 'Ogerpon (Teal Mask)',  
    '/images/8/8d/Ogerpon_%28Masque_Turquoise%29-EV.png', 
    'Acharné', 'Force Mémorielle (sous forme téracristallisée)']
# Ajout masque du puits
orgerpon_masque_puits = df.loc[df.nom_pkmn == 'Ogerpon (Masque Turquoise)'].assign(
    nom_pkmn='Ogerpon (Masque du Puits)', nom_pkmn_us='Ogerpon (Wellspring Mask)',
    url_image='/images/1/1d/Ogerpon_%28Masque_du_Puits%29-EV.png',
    type_2='Eau',
    talent_1='Absorb-Eau'
)
# Ajout masque du fourneau
ogerpon_masque_fourneau = df.loc[df.nom_pkmn == 'Ogerpon (Masque Turquoise)'].assign(
    nom_pkmn='Ogerpon (Masque du Fourneau)', nom_pkmn_us='Ogerpon (Hearthflame Mask)',
    url_image='/images/2/26/Ogerpon_%28Masque_du_Fourneau%29-EV.png',
    type_2='Feu',
    talent_1='Brise-Moule'
)
#Ajout masque de la pierre
ogerpon_masque_pierre = df.loc[df.nom_pkmn == 'Ogerpon (Masque Turquoise)'].assign(
    nom_pkmn='Ogerpon (Masque de la Pierre)', nom_pkmn_us='Ogerpon (Cornerstone Mask)',
    url_image='/images/5/54/Ogerpon_%28Masque_de_la_Pierre%29-EV.png',
    type_2='Roche',
    talent_1='Fermeté'
)


#
##
### N.1024 Terapagos
#Forme Normal
terapagos_normale = pd.DataFrame([[
    'Terapagos (Normale)', 'Terapagos (Normal)', 1024,
    '/images/1/15/Terapagos_%28Forme_Normale%29-EV.png',
    '/images/9/90/Cri_1024_HOME.ogg',
    'Normal', None,
    0.2, 6.5,
    'Téramorphose', None, None,
    '50 % femelle ; 50 % mâle', 255, None,
    'Inconnu', None, '+1 Défense', None, '1 250 000 exp.',
    90, 65, 85, 65, 85, 60
]], columns=df.columns)
# Ajout forme Téracristal
terapagos_teracristal = terapagos_normale.assign(
    nom_pkmn='Terapagos (Téracristal)', nom_pkmn_us='Terapagos (Terastal)',
    url_image='/images/d/d4/Terapagos_%28Forme_Téracristal%29-EV.png',
    taille_m=0.3, poids_kg=16.0,
    talent_1='Téra-carapace',
    pv=95, attaque=95, defense=110, attaque_speciale=105, defense_speciale=110, vitesse=85
)
# Ajout forme Stellaire
terapagos_stellaire = terapagos_normale.assign(
    nom_pkmn='Terapagos (Stellaire)', nom_pkmn_us='Terapagos (Stellar)',
    url_image='/images/3/37/Sprite_1024_Stellaire_HOME.png',
    taille_m=1.7, poids_kg=77.0,
    talent_1='Téraformation 0',
    pv=160, attaque=105, defense=110, attaque_speciale=130, defense_speciale=110, vitesse=85
)
       
df = pd.concat([
    df, 
    tauros_race_combattive, tauros_race_flamboyante, tauros_race_aquatique, 
    mewtwo_blinde,
    morpheo_solaire, morpheo_eau_de_pluie, morpheo_blizzard, 
    deoxys_attaque, deoxys_defense, deoxys_vitesse, 
    cheniti_cape_sable, cheniti_cape_dechet, cheniselle_cape_plante, cheniselle_cape_dechet, 
    motisma_froid, motisma_helice, motisma_lavage, motisma_tonte, 
    dialga_normale, dialga_originelle, palkia_normale, palkia_originelle, giratina_alternative, giratina_originelle, 
    shaymin_terrestre, shaymin_celeste, 
    bargantua_motif_rouge, bargantua_motif_bleu, 
    darumacho_transe, darumacho_galar_transe,
    boreas_totemique, fulguris_totemique, demeteros_totemique, 
    meloetta_danse, amphinobi_sacha, 
    mistigrix_femelle, exagide_assaut, 
    pitrouille_mini, pitrouille_normale, pitrouille_maxi, pitrouille_ultra, 
    banshitrouye_mini, banshitrouye_normale, banshitrouye_maxi, banshitrouye_ultra, 
    zygarde_10, zygarde_50, zygarde_parfaite, 
    hoopa_enchaine, hoopa_dechaine, 
    lougaroc_nocturne, lougaroc_crepusculaire, 
    plumeline_pompom, plumeline_hula, plumeline_buyo,
    froussardine_solitaire, froussardine_banc, 
    meteno_meteore, meteno_noyau, 
    salarsen_grave, wimessir_femelle, 
    zacian_heros_aguerri, zacian_epee_supreme, zamazenta_heros_aguerri, zamazenta_bouclier_supreme, 
    ursaking_normale, ursaking_lune_vermeille, 
    shifours_mille_poings, shifours_gigamax_mille_poings,
    amovenus_totemique, fragrouin_femelle, 
    famignol_famille_de_trois, famignol_famille_de_quatre, 
    superdofin_ordinaire, superdofin_super, 
    deusolourdo_double, deusolourdo_triple, 
    mordudor_coffre, mordudor_marche, 
    orgerpon_masque_puits, ogerpon_masque_fourneau, ogerpon_masque_pierre, 
    terapagos_normale, terapagos_teracristal, terapagos_stellaire], ignore_index=True)


df.to_csv('../../B___Data/CSV/pokemons_v2.csv')