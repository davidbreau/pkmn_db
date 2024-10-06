# Lors du scrap, certaines exceptions n'ont pas vu leurs talents leurs formes correctement scrapés ou  (env. 100 sur 1051)
# Ce script sert à les insérer à la main
import sys
sys.path.append('../..')
from B___Data.connectors import Test_Database as Pkmn_Database
from B___Data.pokemon import Pokemon



#### CORRECTIF DES URL DES IMAGES
db = Pkmn_Database()
connection = db.connect()
cursor = connection.cursor()

# Requête SQL pour mettre à jour les URL des images
update_query = """
UPDATE Pokemons
SET url_image = CASE
    WHEN url_image LIKE '%/thumb%' THEN
        '/images' || substr(url_image, instr(url_image, '/thumb') + 6, 
            instr(substr(url_image, instr(url_image, '/thumb') + 6), '/') - 1)
    ELSE
        substr(url_image, 1, length(url_image) - 1)
END
"""

# Exécution de la requête de mise à jour
cursor.execute(update_query)
connection.commit()
print("URLs des images mises à jour avec succès.")

# Fermeture de la connexion
connection.close()


#### Correction des formes/information manquantes 


#
##
### N.58 CANINOS
Pokemon('Caninos').update(
    talent_1='Intimidation',
    talent_2='Torche',
    talent_cache='Cœur Noble'
)


#
##
### N.75 Gravalanch
Pokemon('Gravalanch').update(
    talent_1='Tête de Roc',
    talent_2='Fermeté',
    talent_cache='Voile Sable'
)


#
##
### N.128 Tauros
# Tauros de Paldéa (Race Combattive)
Pokemon('Tauros').add_new_form(
    'Tauros de Paldéa (Race Combattive)',
    nom_pkmn_us='Paldean Tauros (Combat Breed)',
    url_image='/images/9/9a/Tauros_de_Paldea_%28Race_Combative%29-EV.png',
    type_1='Combat',
    taille_m=1.4,
    poids_kg=115.0,  # Correction de la valeur (11.0 -> 115.0)
    talent_cache='Ruminant',
    points_exp='172 exp.',
    attaque=110,
    defense=105,
    attaque_speciale=30,
    vitesse=100
)

# Tauros de Paldéa (Race Flamboyante)
Pokemon('Tauros de Paldéa (Race Combattive)').add_new_form(
    'Tauros de Paldéa (Race Flamboyante)',
    nom_pkmn_us='Paldean Tauros (Blaze Breed)',
    url_image='/images/5/55/Tauros_de_Paldea_%28Race_Flamboyante%29-EV.png',
    type_2='Feu',
    poids_kg=85.0
)

# Tauros de Paldéa (Race Aquatique)
Pokemon('Tauros de Paldéa (Race Combattive)').add_new_form(
    'Tauros de Paldéa (Race Aquatique)',
    nom_pkmn_us='Paldean Tauros (Aqua Breed)',
    url_image='/images/2/28/Tauros_de_Paldea_%28Race_Aquatique%29-EV.png',
    type_2='Eau',
    poids_kg=85.0
)



#
##
### N.275 Tengalice
Pokemon('Tengalice').update(
    talent_1='Chlorophylle',
    talent_2='Matinal (gen :8) / Aéroporté (gen 9:)',
    talent_cache='Pickpocket'
)

#
##
### N.351 Morphéo
# Mise à jour de la forme normale
Pokemon('Morphéo').update(
    nom_pkmn='Morphéo (Normale)',
    nom_pkmn_us='Castform (Normal)',
    type_1='Normal'
)

# Ajout forme solaire
Pokemon('Morphéo (Normale)').add_new_form(
    'Morphéo (Solaire)',
    nom_pkmn_us='Castform (Sunny)',
    url_image='/images/f/fa/Morphéo_%28Forme_Solaire%29-USUL.png',
    type_1='Feu'
)

# Ajout forme Eau de Pluie
Pokemon('Morphéo (Normale)').add_new_form(
    'Morphéo (Eau de Pluie)',
    nom_pkmn_us='Castform (Rainy)',
    url_image='/images/b/b7/Morphéo_%28Forme_Eau_de_Pluie%29-USUL.png',
    type_1='Eau'
)

# Ajout forme Blizzard
Pokemon('Morphéo (Normale)').add_new_form(
    'Morphéo (Blizzard)',
    nom_pkmn_us='Castform (Snowy)',
    url_image='/images/0/08/Morphéo_%28Forme_Blizzard%29-USUL.png',
    type_1='Glace'  # Changé de type_2 à type_1 car c'est son seul type dans cette forme
)


#
##
### N.386 Deoxys
Pokemon('Deoxys').update(
    nom_pkmn='Deoxys (Normale)',
    nom_pkmn_us='Deoxys (Normal)'
)

# Ajout forme Attaque
Pokemon('Deoxys (Normale)').add_new_form(
    'Deoxys (Attaque)',
    nom_pkmn_us='Deoxys (Attack)',
    url_image='/images/f/fc/Deoxys_%28Forme_Attaque%29-RFVF.png',
    attaque=180,
    defense=20,
    attaque_speciale=180,
    defense_speciale=20
)

# Ajout forme Defense
Pokemon('Deoxys (Normale)').add_new_form(
    'Deoxys (Defense)',
    nom_pkmn_us='Deoxys (Defense)',
    url_image='/images/7/7c/Deoxys_%28Forme_Défense%29-RFVF.png',
    attaque=70,
    defense=160,
    attaque_speciale=70,
    defense_speciale=160
)

# Ajout forme Vitesse
Pokemon('Deoxys (Normale)').add_new_form(
    'Deoxys (Vitesse)',
    nom_pkmn_us='Deoxys (Speed)',
    url_image='/images/6/63/Deoxys_%28Forme_Vitesse%29-E.png',
    attaque=95,
    defense=90,
    attaque_speciale=95,
    defense_speciale=90
)


#
##
### N.393 Tiplouf
Pokemon('Tiplouf').update(
    talent_1='Torrent',
    talent_cache='Acharné (gen :8)/ Battant (gen 9:)'
)

# N.394 Prinplouf
Pokemon('Prinplouf').update(
    talent_1='Torrent',
    talent_cache='Acharné (gen :8)/ Battant (gen 9:)'
)

# N.395 Pingoléon
Pokemon('Pingoléon').update(
    talent_1='Torrent',
    talent_cache='Acharné (gen :8)/ Battant (gen 9:)'
)


#
##
### N.413 Cheniti
Pokemon('Cheniti').update(
    nom_pkmn='Cheniti (Cape Plante)',
    nom_pkmn_us='Burmy (Plant Cloak)'
)

# Ajout Cape Sable
Pokemon('Cheniti (Cape Plante)').add_new_form(
    'Cheniti (Cape Sable)',
    nom_pkmn_us='Burmy (Sandy Cloak)',
    url_image='/images/9/9f/Cheniti_%28Cape_Sable%29-DP.png'
)

# Ajout Cape Déchet
Pokemon('Cheniti (Cape Plante)').add_new_form(
    'Cheniti (Cape Déchet)',
    nom_pkmn_us='Burmy (Trash Cloak)',
    url_image='/images/b/bf/Cheniti_%28Cape_Déchet%29-DP.png'
)

#

### N.414 Cheniselle
Pokemon('Cheniselle').update(
    nom_pkmn='Cheniselle (Cape Sable)',
    nom_pkmn_us='Wormadam (Sandy Cloak)',
    type_1='Insecte',
    type_2='Sol',
    attaque=79,
    defense=105,
    attaque_speciale=59,
    defense_speciale=85
)

# Ajout Cape Plante
Pokemon('Cheniselle (Cape Sable)').add_new_form(
    'Cheniselle (Cape Plante)',
    nom_pkmn_us='Wormadam (Plant Cloak)',
    url_image='/images/4/44/Cheniselle_%28Cape_Plante%29-DP.png',
    type_2='Plante',
    attaque=79,
    defense=105,
    attaque_speciale=59,
    defense_speciale=85
)

# Ajout Cape Déchet
Pokemon('Cheniselle (Cape Sable)').add_new_form(
    'Cheniselle (Cape Déchet)',
    nom_pkmn_us='Wormadam (Trash Cloak)',
    url_image='/images/7/78/Cheniselle_%28Cape_Déchet%29-DP.png',
    type_2='Acier',
    attaque=69,
    defense=95,
    attaque_speciale=69,
    defense_speciale=95
)


#
##
### N.479 Motisma
Pokemon('Motisma').update(
    nom_pkmn='Motisma (Normale)',
    nom_pkmn_us='Rotom (Normal)',
    type_1='Électrik',
    type_2='Spectre'
)

# Ajout forme Chaleur
Pokemon('Motisma (Normale)').add_new_form(
    'Motisma (Chaleur)',
    nom_pkmn_us='Rotom (Heat)',
    url_image='/images/3/34/Motisma_%28Chaleur%29-Pt.png',
    type_2='Feu',
    attaque=65,
    defense=107,
    attaque_speciale=105,
    defense_speciale=107,
    vitesse=86
)

# Ajout forme Froid
Pokemon('Motisma (Normale)').add_new_form(
    'Motisma (Froid)',
    nom_pkmn_us='Rotom (Frost)',
    url_image='/images/0/06/Motisma_%28Froid%29-Pt.png',
    type_2='Glace',
    attaque=65,
    defense=107,
    attaque_speciale=105,
    defense_speciale=107,
    vitesse=86
)

# Ajout forme Hélice
Pokemon('Motisma (Normale)').add_new_form(
    'Motisma (Hélice)',
    nom_pkmn_us='Rotom (Fan)',
    url_image='/images/6/6b/Motisma_%28Hélice%29-Pt.png',
    type_2='Vol',
    attaque=65,
    defense=107,
    attaque_speciale=105,
    defense_speciale=107,
    vitesse=86
)

# Ajout forme Lavage
Pokemon('Motisma (Normale)').add_new_form(
    'Motisma (Lavage)',
    nom_pkmn_us='Rotom (Wash)',
    url_image='/images/a/a8/Motisma_%28Lavage%29-Pt.png',
    type_2='Eau',
    attaque=65,
    defense=107,
    attaque_speciale=105,
    defense_speciale=107,
    vitesse=86
)

# Ajout forme Tonte
Pokemon('Motisma (Normale)').add_new_form(
    'Motisma (Tonte)',
    nom_pkmn_us='Rotom (Mow)',
    url_image='/images/8/81/Motisma_%28Tonte%29-Pt.png',
    type_2='Plante',
    attaque=65,
    defense=107,
    attaque_speciale=105,
    defense_speciale=107,
    vitesse=86
)

#
##
### N.483 Dialga
# Ajout forme Normale
Pokemon.create(
    nom_pkmn='Dialga (Normale)',
    nom_pkmn_us='Dialga (Normal)',
    numero_national=483,
    url_image='/images/e/e4/Dialga-DEPS.png',
    url_son='/images/0/0d/Cri_0483_HOME.ogg',
    type_1='Acier',
    type_2='Dragon',
    taille_m=5.4,
    poids_kg=683.0,
    talent_1='Pression',
    talent_cache='Télépathe',
    groupe_oeuf_1='Asexué',
    couleur='3',
    taux_capture=120,
    categorie='Inconnu',
    ev_donne='+3 Att. Spé',
    points_exp='220 Exp.',
    exp_pour_niveau_100='1 250 000 exp',
    pv=100,
    attaque=120,
    defense=120,
    attaque_speciale=150,
    defense_speciale=100,
    vitesse=90
)

Pokemon('Dialga (Normale)').add_new_form(
    'Dialga (Originelle)',
    nom_pkmn_us='Dialga (Origin)',
    url_image='/images/5/55/Dialga_%28Forme_Originelle%29-LPA.png',
    taille_m=7.0,
    poids_kg=850.0,
    attaque=100,
    defense_speciale=120
)
#
##
### N.484 Palkia
# Ajout forme Normale
Pokemon.create(
    nom_pkmn='Palkia (Normale)',
    nom_pkmn_us='Palkia (Normal)',
    numero_national=484,
    url_image='/images/c/c7/Palkia-DEPS.png',
    url_son='/images/e/ef/Cri_0484_HOME.ogg',
    type_1='Acier',
    type_2='Eau',
    taille_m=4.2,
    poids_kg=336.0,
    talent_1='Pression',
    talent_cache='Télépathe',
    groupe_oeuf_1='Asexué',
    couleur='3',
    taux_capture=120,
    categorie='Inconnu',
    ev_donne='+3 Att. Spé',
    points_exp='220 Exp.',
    exp_pour_niveau_100='1 250 000 exp',
    pv=90,
    attaque=120,
    defense=100,
    attaque_speciale=150,
    defense_speciale=120,
    vitesse=100
)

Pokemon('Palkia (Normale)').add_new_form(
    'Palkia (Originelle)',
    nom_pkmn_us='Palkia (Origin)',
    url_image='/images/7/7f/Palkia_%28Forme_Originelle%29-LPA.png',
    taille_m=7.0,
    poids_kg=850.0,
    attaque=100,
    vitesse=120
)


#
##
### N.487 Giratina
# Ajout forme Alternative
Pokemon.create(
    nom_pkmn='Giratina (Alternative)',
    nom_pkmn_us='Giratina (Altered)',
    numero_national=487,
    url_image='/images/2/2d/Giratina_%28Forme_Alternative%29-DEPS.png',
    url_son='/images/d/d6/Cri_0487_HOME.ogg',
    type_1='Spectre',
    type_2='Dragon',
    taille_m=4.5,
    poids_kg=750.0,
    talent_1='Pression',
    talent_cache='Télépathe',
    groupe_oeuf_1='Asexué',
    couleur='3',
    taux_capture=120,
    categorie='Inconnu',
    ev_donne='+3 PV',
    points_exp='220 Exp.',
    exp_pour_niveau_100='1 250 000 exp',
    pv=150,
    attaque=100,
    defense=120,
    attaque_speciale=100,
    defense_speciale=120,
    vitesse=90
)

Pokemon('Giratina (Alternative)').add_new_form(
    'Giratina (Originelle)',
    nom_pkmn_us='Giratina (Origin)',
    url_image='/images/f/f1/Giratina_%28Forme_Originelle%29-Pt.png',
    taille_m=6.9,
    poids_kg=650.0,
    attaque=120,
    defense=100,
    attaque_speciale=120,
    defense_speciale=100
)


#
##
### N. 492 Shaymin
# Ajout forme Terrestre
Pokemon.create(
    nom_pkmn='Shaymin (Terrestre)',
    nom_pkmn_us='Shaymin (Land)',
    numero_national=492,
    url_image='/images/3/3d/Shaymin_%28Forme_Terrestre%29-DEPS.png',
    url_son='/images/7/7a/Cri_0492_HOME.ogg',
    type_1='Plante',
    taille_m=0.2,
    poids_kg=2.1,
    talent_1='Médic Nature',
    groupe_oeuf_1='Asexué',
    couleur=45,
    taux_capture=120,
    categorie='Inconnu',
    ev_donne='+3 PV',
    exp_pour_niveau_100='1 059 860 exp.',
    pv=100,
    attaque=100,
    defense=100,
    attaque_speciale=100,
    defense_speciale=100,
    vitesse=100
)

Pokemon('Shaymin (Terrestre)').add_new_form(
    'Shaymin (Céleste)',
    nom_pkmn_us='Shaymin (Sky)',
    url_image='/images/d/db/Shaymin_%28Forme_Céleste%29-Pt.png',
    url_son='/images/7/76/Cri_0492_C%C3%A9leste_HOME.ogg',
    type_2='Vol',
    talent_1='Sérénité',
    attaque=103,
    defense=75,
    attaque_speciale=120,
    defense_speciale=75,
    vitesse=127
)


#
##
### N.524 Nodulithe
Pokemon('Nodulithe').update(
    talent_1='Fermeté',
    talent_2='Armurouillée (gen :7)',
    talent_cache='Force Sable'
)

#
##
### N.524 Brutapode
Pokemon('Brutapode').update(
    talent_1='Point Poison',
    talent_2='Essaim',
    talent_cache='Pied Véloce (gen 5) / Turbo (gen 6:)'
)


#
##
### N.545 Bargantua
# Mise à jour de Bargantua Motif Blanc
Pokemon('Bargantua').update(
    nom_pkmn='Bargantua (Motif Blanc)',
    nom_pkmn_us='Basculin (White-Striped)',
    talent_1='Phobique',
    talent_2='Adaptabilité',
    talent_cache='Brise Moule'
)

Pokemon('Bargantua (Motif Blanc)').add_new_form(
    'Bargantua (Motif Rouge)',
    nom_pkmn_us='Basculin (Red-Striped)',
    url_image='/images/5/52/Bargantua_%28Motif_Rouge%29-NB.png',
    talent_1='Téméraire'
)

Pokemon('Bargantua (Motif Blanc)').add_new_form(
    'Bargantua (Motif Bleu)',
    nom_pkmn_us='Basculin (Blue-Striped)',
    url_image='/images/7/7c/Bargantua_%28Motif_Bleu%29-NB.png',
    talent_1='Tête de Roc'
)


#
##
### N.609 Lugulabre
Pokemon('Lugulabre').update(
    talent_1='Torche',
    talent_2='Corps Ardent',
    talent_cache='Marque Ombre (gen 5) / Infiltration (gen 6:)'
)


#
##
### N.641 Boréas
Pokemon('Boréas').update(
    nom_pkmn='Boréas (Avatar)',
    nom_pkmn_us='Tornadus (Incarnate)',
    talent_1='Farceur',
    talent_cache='Acharné',
    taille_m=1.5
)

Pokemon('Boréas (Avatar)').add_new_form(
    'Boréas (Totémique)',
    nom_pkmn_us='Tornadus (Therian)',
    url_image='/images/a/a1/Boréas_%28Forme_Totémique%29-N2B2.png',
    url_son='/images/1/1b/Cri_0641_Tot%C3%A9mique_HOME.ogg',
    taille_m=1.4,
    talent_1='Régé-Force',
    talent_cache=None,
    attaque=100,
    defense=80,
    attaque_speciale=110,
    defense_speciale=90,
    vitesse=121
)


#
##
### N.642 Fulguris
Pokemon('Fulguris').update(
    nom_pkmn='Fulguris (Avatar)',
    nom_pkmn_us='Thundurus (Incarnate)',
    talent_1='Farceur',
    talent_cache='Acharné',
    taille_m=1.5
)

Pokemon('Fulguris (Avatar)').add_new_form(
    'Fulguris (Totémique)',
    nom_pkmn_us='Thundurus (Therian)',
    url_image='/images/d/d8/Fulguris_%28Forme_Totémique%29-N2B2.png',
    url_son='/images/e/ec/Cri_0642_Tot%C3%A9mique_HOME.ogg',
    taille_m=3.0,
    talent_1='Absorbe-Volt',
    talent_cache=None,
    attaque=105,
    attaque_speciale=145,
    vitesse=101
)

#
##
### N.645 Démétéros
Pokemon('Démétéros').update(
    nom_pkmn='Démétéros (Avatar)',
    nom_pkmn_us='Landorus (Incarnate)',
    talent_1='Force Sable',
    talent_cache='Sans Limite',
    taille_m=1.5
)

Pokemon('Démétéros (Avatar)').add_new_form(
    'Démétéros (Totémique)',
    nom_pkmn_us='Landorus (Therian)',
    url_image='/images/e/eb/Démétéros_%28Forme_Totémique%29-N2B2.png',
    url_son='/images/a/aa/Cri_0645_Tot%C3%A9mique_HOME.ogg',
    taille_m=1.3,
    talent_1='Intimidation',
    talent_cache=None,
    attaque=145,
    attaque_speciale=105,
    vitesse=91
)


#
##
### N.658 Amphinobi
# Amphinobi Forme Normale
Pokemon('Amphinobi').update(
    talent_1='Torrent',
    talent_cache='Protéen'
)

Pokemon('Amphinobi').add_new_form(
    'Amphinobi (Sacha)',
    nom_pkmn_us='Greninja (Ash)',
    url_image='/images/5/5c/Amphinobi_%28Forme_Sacha%29-SL.png',
    talent_1='Synergie',
    talent_cache=None,
    attaque=145,
    attaque_speciale=153,
    vitesse=132
)


#
##
### N.678 Mistigrix
# Mistigrix (♂)
Pokemon('Mistigrix').update(
    nom_pkmn='Mistigrix (♂)',
    nom_pkmn_us='Meowstic (♂)',
    talent_1='Regard Vif',
    talent_2='Infiltration',
    talent_cache='Farceur'
)
# Ajout Mistigrix (♀)
Pokemon('Mistigrix (♂)').add_new_form(
    'Mistigrix (♀)',
    nom_pkmn_us='Meowstic (♀)',
    url_image='/images/5/57/Mistigrix_%28Femelle%29-XY.png',
    talent_cache='Battant'
)


#
##
### N.710 Pitrouille
Pokemon.create(
    nom_pkmn='Pitrouille (Mini)',
    nom_pkmn_us='Pumpkaboo (Small)',
    numero_national=710,
    url_image='/images/b/b7/Sprite_0710_Mini_HOME.png',
    url_son='/images/5/59/Cri_0710_HOME.ogg',
    type_1='Spectre',
    type_2='Plante',
    taille_m=0.3,
    poids_kg=3.5,
    talent_1='Ramassage',
    talent_2='Fouille',
    talent_cache='Insomnia',
    groupe_oeuf_1='50 % femelle ; 50 % mâle',
    couleur=190,
    taux_capture=20,
    categorie='Amorphe',
    ev_donne='+1 Défense',
    points_exp='67 exp.',
    exp_pour_niveau_100='1 000 000 exp.',
    pv=44,
    attaque=66,
    defense=55,
    attaque_speciale=44,
    defense_speciale=55,
    vitesse=56
)

Pokemon('Pitrouille (Mini)').add_new_form(
    'Pitrouille (Normale)',
    nom_pkmn_us='Pumpkaboo (Average)',
    url_image='/images/b/ba/Sprite_0710_Normale_HOME.png',
    taille_m=0.4,
    poids_kg=5.0,
    pv=49,
    vitesse=51
)

Pokemon('Pitrouille (Mini)').add_new_form(
    'Pitrouille (Maxi)',
    nom_pkmn_us='Pumpkaboo (Large)',
    url_image='/images/9/98/Sprite_0710_Maxi_HOME.png',
    taille_m=0.5,
    poids_kg=7.5,
    pv=54,
    vitesse=46
)

Pokemon('Pitrouille (Mini)').add_new_form(
    'Pitrouille (Ultra)',
    nom_pkmn_us='Pumpkaboo (Super)',
    url_image='/images/9/98/Sprite_0710_Maxi_HOME.png',
    url_son='/images/b/bf/Cri_0710_Ultra_HOME.ogg',
    taille_m=0.8,
    poids_kg=15,
    pv=59,
    vitesse=41
)


#
##
### N.711 Banshitrouye
Pokemon.create(
    nom_pkmn='Banshitrouye (Mini)',
    nom_pkmn_us='Gourgeist (Small)',
    numero_national=711,
    url_image='/images/2/23/Sprite_0711_Mini_HOME.png',
    url_son='/images/4/46/Cri_0711_HOME.ogg',
    type_1='Spectre',
    type_2='Plante',
    taille_m=0.7,
    poids_kg=9.5,
    talent_1='Ramassage',
    talent_2='Fouille',
    talent_cache='Insomnia',
    groupe_oeuf_1='50 % femelle ; 50 % mâle',
    couleur=190,
    taux_capture=20,
    categorie='Amorphe',
    ev_donne='+2 Défense',
    points_exp='173 exp.',
    exp_pour_niveau_100='1 000 000 exp.',
    pv=55,
    attaque=85,
    defense=122,
    attaque_speciale=58,
    defense_speciale=75,
    vitesse=99
)

Pokemon('Banshitrouye (Mini)').add_new_form(
    'Banshitrouye (Normale)',
    nom_pkmn_us='Gourgeist (Average)',
    url_image='/images/8/84/Sprite_0711_Normale_HOME.png',
    taille_m=0.9,
    poids_kg=12.5,
    pv=65,
    attaque=90,
    vitesse=84
)

Pokemon('Banshitrouye (Mini)').add_new_form(
    'Banshitrouye (Maxi)',
    nom_pkmn_us='Gourgeist (Large)',
    url_image='/images/c/c5/Sprite_0711_Maxi_HOME.png',
    taille_m=1.1,
    poids_kg=14.0,
    pv=75,
    attaque=95,
    vitesse=69
)

Pokemon('Banshitrouye (Mini)').add_new_form(
    'Banshitrouye (Ultra)',
    nom_pkmn_us='Gourgeist (Super)',
    url_image='/images/5/51/Sprite_0711_Ultra_HOME.png',
    url_son='/images/4/41/Cri_0711_Ultra_HOME.ogg',
    taille_m=1.7,
    poids_kg=39.0,
    pv=85,
    attaque=100,
    vitesse=54
)



#
##
### N.718 Zygarde
# Ajout forme 10%
Pokemon.create(
    nom_pkmn='Zygarde (10%)',
    nom_pkmn_us='Zygarde (10%)',
    numero_national=718,
    url_image='/images/6/63/Zygarde_%28Forme_10_%25%29-SL.png',
    url_son='/images/7/75/Cri_0718_10_%25_HOME.ogg',
    type_1='Dragon',
    type_2='Sol',
    taille_m=1.2,
    poids_kg=33.5,
    talent_1='Aura Inversée',
    talent_2='Rassemblement',
    groupe_oeuf_1='Asexué',
    couleur=3,
    taux_capture=120,
    categorie='Inconnu',
    ev_donne='+3 PV',
    points_exp='306 exp.',
    exp_pour_niveau_100='1 250 000 exp.',
    pv=54,
    attaque=100,
    defense=71,
    attaque_speciale=61,
    defense_speciale=85,
    vitesse=115
)

Pokemon('Zygarde (10%)').add_new_form(
    'Zygarde (50%)',
    nom_pkmn_us='Zygarde (50%)',
    url_image='/images/0/0b/Zygarde_%28Forme_50_%25%29-XY.png',
    url_son='/images/0/00/Cri_0718_50_%25_HOME.ogg',
    taille_m=5.0,  # Correction de 108 à 5.0 mètres
    poids_kg=305.0,  # Correction de 121 à 305.0 kg
    pv=108,
    defense=121,
    attaque_speciale=81,
    defense_speciale=95,
    vitesse=95
)

Pokemon('Zygarde (10%)').add_new_form(
    'Zygarde (Parfaite)',
    nom_pkmn_us='Zygarde (Complete)',
    url_image='/images/5/5f/Zygarde_%28Forme_Parfaite%29-SL.png',
    url_son='/images/a/ae/Cri_0718_Parfaite_HOME.ogg',
    taille_m=4.5,  # Correction de 216 à 4.5 mètres
    poids_kg=610.0,  # Correction de 121 à 610.0 kg
    pv=216,
    attaque=100,
    defense=121,
    attaque_speciale=91,
    defense_speciale=95,
    vitesse=85
)


#
##
### N.720 Hoopa
# Ajout forme Hoopa Enchaîné
Pokemon.create(
    nom_pkmn='Hoopa (Enchaîné)',
    nom_pkmn_us='Hoopa (Confined)',
    numero_national=720,
    url_image='/images/0/04/Hoopa_%28Enchaîné%29-ROSA.png',
    url_son='/images/4/4c/Cri_0720_HOME.ogg',
    type_1='Psy',
    type_2='Spectre',
    taille_m=0.5,
    poids_kg=9.0,
    talent_1='Maigicien',
    groupe_oeuf_1='Asexué',
    couleur=3,
    taux_capture=120,
    categorie='Inconnu',
    ev_donne='+3 Attaque Spéciale',
    points_exp='270 exp.',
    exp_pour_niveau_100='1 250 000 exp.',
    pv=80,
    attaque=110,
    defense=60,
    attaque_speciale=150,
    defense_speciale=130,
    vitesse=70
)

Pokemon('Hoopa (Enchaîné)').add_new_form(
    'Hoopa (Déchaîné)',
    nom_pkmn_us='Hoopa (Unbound)',  # Correction de 'Confined' à 'Unbound'
    url_image='/images/7/78/Hoopa_%28Déchaîné%29-ROSA.png',
    url_son='/images/2/21/Cri_0720_D%C3%A9cha%C3%AFn%C3%A9_HOME.ogg',
    type_2='Ténèbres',
    taille_m=6.5,  # Ajout de la taille correcte
    poids_kg=490.0,  # Ajout du poids correct
    attaque=160,
    attaque_speciale=170,  # Correction de 150 à 170
    vitesse=80
)



#
##
### N.744 Rocabot
Pokemon('Rocabot').update(
    talent_1='Regard Vif / Tempo Perso (Spécial)',
    talent_2='Esprit Vital',
    talent_cache='Impassible'
)

#
##
### N.745 Lougaroc (Diurne)
Pokemon('Lougaroc').update(
    nom_pkmn='Lougaroc (Diurne)',
    nom_pkmn_us='Lycanroc (Midday)',
    talent_1='Regard Vif',
    talent_2='Esprit Vital',
    talent_cache='Annule Garde'
)

Pokemon('Lougaroc (Diurne)').add_new_form(
    'Lougaroc (Nocturne)',
    nom_pkmn_us='Lycanroc (Midnight)',
    url_image='/images/a/a4/Lougaroc_%28Forme_Nocturne%29-SL.png',
    url_son='/images/2/2d/Cri_0745_Nocturne_HOME.ogg',
    pv=85,
    attaque=115,
    defense=75,
    attaque_speciale=55,
    defense_speciale=75,
    vitesse=82
)

Pokemon('Lougaroc (Diurne)').add_new_form(
    'Lougaroc (Crépusculaire)',
    nom_pkmn_us='Lycanroc (Dusk)',
    url_image='/images/f/ff/Lougaroc_%28Forme_Cr%C3%A9pusculaire%29-USUL.png',
    url_son='/images/f/f2/Cri_0745_Cr%C3%A9pusculaire_HOME.ogg',
    talent_1='Griffe Dure',
    talent_2=None,
    talent_cache=None,
    pv=75,
    attaque=117,
    defense=65,
    attaque_speciale=55,
    defense_speciale=65,
    vitesse=110
)


#
##
### N.746 Froussardine
#Forme solitaire
Pokemon.create(
    nom_pkmn='Froussardine (Solitaire)',
    nom_pkmn_us='Wishiwashi (Solo)',
    numero_national=746,
    url_image='/images/8/8b/Froussardine_%28Forme_Solitaire%29-SL.png',
    url_son='/images/0/0a/Cri_0746_Solitaire_HOME.ogg',
    type_1='Eau',
    taille_m=0.2,
    poids_kg=0.3,
    talent_1='Banc',
    groupe_oeuf_1='50 % femelle ; 50 % mâle',
    couleur=60,
    taux_capture=15,
    categorie='Aquatique 2',
    ev_donne='+1 PV',
    points_exp='61 exp.',
    exp_pour_niveau_100='800 000 exp.',
    pv=45,
    attaque=20,
    defense=20,
    attaque_speciale=25,
    defense_speciale=25,
    vitesse=40
)

Pokemon('Froussardine (Solitaire)').add_new_form(
    'Froussardine (Banc)',
    nom_pkmn_us='Wishiwashi (School)',
    url_image='/images/d/d5/Froussardine_%28Forme_Banc%29-SL.png',
    url_son='/images/3/36/Cri_0746_Banc_HOME.ogg',
    taille_m=8.2,
    poids_kg=78.6,
    attaque=140,
    defense=130,
    attaque_speciale=140,
    defense_speciale=135,
    vitesse=30
)


#
##
### N.774 Météno
#Forme meteore
Pokemon.create(
    nom_pkmn='Météno (Météore)',
    nom_pkmn_us='Minior (Meteor)',
    numero_national=774,
    url_image='/images/1/1c/Météno_%28Forme_Météore%29-SL.png',
    url_son='/images/0/05/Cri_0774_HOME.ogg',
    type_1='Roche',
    type_2='Vol',
    taille_m=0.3,
    poids_kg=40.0,
    talent_1='Bouclier-Carcan',
    groupe_oeuf_1='Asexué',
    couleur=30,
    taux_capture=25,
    categorie='Minéral',
    ev_donne='+1 Défense; +1 Défense Spéciale',
    points_exp='154 exp.',
    exp_pour_niveau_100='1 059 860 exp.',
    pv=60,
    attaque=60,
    defense=100,
    attaque_speciale=60,
    defense_speciale=100,
    vitesse=60
)

Pokemon('Météno (Météore)').add_new_form(
    'Météno (Noyau)',
    nom_pkmn_us='Minior (Core)',
    url_image='/images/c/c2/Météno_%28Noyau_Rouge%29-SL.png',
    poids_kg=0.3,
    ev_donne='+1 Att.;+1 Att. Spé',
    attaque=100,
    defense=60,
    attaque_speciale=100,
    defense_speciale=60,
    vitesse=120
)


#
##
### N.849 Salarsen
Pokemon('Salarsen').update(
    nom_pkmn='Salarsen (Aïgue)',
    nom_pkmn_us='Toxtricity (Amped)',
    talent_1='Punk Rock',
    talent_2='Plus',
    talent_cache='Technicien'
)

Pokemon('Salarsen (Aïgue)').add_new_form(
    'Salarsen (Grave)',
    nom_pkmn_us='Toxtricity (Low Key)',
    url_image='/images/8/8f/Salarsen_%28Forme_Grave%29-EB.png',
    url_son='/images/6/6f/Cri_0849_Grave_HOME.ogg',
    talent_2='Moins'
)

Pokemon('Salarsen Gigamax').update(
    talent_1='Punk Rock',
    talent_2='Plus (forme Aïgue) / Moins (forme Grave)',
    talent_cache='Technicien'
)


#
##
### N.876 Wimessir
okemon('Wimessir').update(
    nom_pkmn='Wimessir (♂)',
    nom_pkmn_us='Indeedee (♂)',
    talent_1='Tempo Perso',
    talent_2='Synchro',
    talent_cache='Créa-Psy'
)

Pokemon('Wimessir (♂)').add_new_form(
    'Wimessir (♀)',
    nom_pkmn_us='Indeedee (♀)',
    url_image='/images/1/1c/Wimessir_%28Femelle%29-EB.png',
    url_son='/images/6/63/Cri_0876_%E2%99%80_HOME.ogg',
    talent_1='Attention',
    pv=70,
    attaque=55,
    defense=65,
    attaque_speciale=95,
    defense_speciale=105,
    vitesse=85
)


#
##
### N.888 Zacian
#Forme Heros Aguerri
Pokemon.create(
    nom_pkmn='Zacian (Héros Aguerri)',
    nom_pkmn_us='Zacian (Hero of Many Battles)',
    numero_national=888,
    url_image='/images/d/dc/Zacian_%28Héros_Aguerri%29-EB.png',
    url_son='/images/b/b8/Cri_0888_H%C3%A9ros_Aguerri_HOME.ogg',
    type_1='Fée',
    taille_m=2.8,
    poids_kg=110.0,
    talent_1='Lame Indomptable',
    groupe_oeuf_1='Asexué',
    couleur=10,
    taux_capture=120,
    categorie='Inconnu',
    ev_donne='+3 Vit.',
    points_exp='335 exp.',
    exp_pour_niveau_100='1 250 000 exp.',
    pv=92,
    attaque=130,
    defense=115,
    attaque_speciale=80,
    defense_speciale=115,
    vitesse=138
)

Pokemon('Zacian (Héros Aguerri)').add_new_form(
    'Zacian (Épée Suprême)',
    nom_pkmn_us='Zacian (Crowned Sword)',
    url_image='/images/5/52/Zacian_%28Épée_Suprême%29-EB.png',
    url_son='/images/5/5d/Cri_0888_%C3%89p%C3%A9e_Supr%C3%AAme_HOME.ogg',
    type_2='Acier',
    poids_kg=355.0,
    attaque=170,
    vitesse=148
)


#
##
### N.889 Zamazenta
Pokemon.create(
    nom_pkmn='Zamazenta (Héros Aguerri)',
    nom_pkmn_us='Zamazenta (Hero of Many Battles)',
    numero_national=889,
    url_image='/images/5/5a/Zamazenta_%28Héros_Aguerri%29-EB.png',
    url_son='/images/5/50/Cri_0889_H%C3%A9ros_Aguerri_HOME.ogg',
    type_1='Combat',
    taille_m=2.9,
    poids_kg=210.0,
    talent_1='Égide Inflexible',
    groupe_oeuf_1='Asexué',
    couleur=10,
    taux_capture=120,
    categorie='Inconnu',
    ev_donne='+3 Vit.',
    points_exp='225 exp.',
    exp_pour_niveau_100='1 250 000 exp.',
    pv=92,
    attaque=130,
    defense=115,
    attaque_speciale=80,
    defense_speciale=115,
    vitesse=138
)

Pokemon('Zamazenta (Héros Aguerri)').add_new_form(
    'Zamazenta (Bouclier Suprême)',
    nom_pkmn_us='Zamazenta (Crowned Shield)',
    url_image='/images/c/cf/Zamazenta_%28Bouclier_Suprême%29-EB.png',
    url_son='/images/e/e9/Cri_0889_Bouclier_Supr%C3%AAme_HOME.ogg',
    type_2='Acier',
    poids_kg=785.0,
    defense=145,
    defense_speciale=145,
    vitesse=128
)


#
##
### N.901 Ursaking
Pokemon.create(
    nom_pkmn='Ursaking (Normale)',
    nom_pkmn_us='Ursaluna (Normal)',
    numero_national=901,
    url_image='/images/2/28/Ursaking-LPA.png',
    url_son='/images/2/28/Cri_0901_HOME.ogg',
    type_1='Sol',
    type_2='Normal',
    taille_m=2.4,
    poids_kg=290.0,
    talent_1='Cran',
    talent_2='Pare-Balles',
    talent_cache='Tension',
    groupe_oeuf_1='50 % femelle ; 50 % mâle',
    couleur=20,
    taux_capture=20,
    categorie='Terrestre',
    ev_donne='+3 Att.',
    points_exp='275 exp.',
    exp_pour_niveau_100='1 000 000 exp.',
    pv=130,
    attaque=140,
    defense=105,
    attaque_speciale=45,
    defense_speciale=80,
    vitesse=50
)

Pokemon('Ursaking (Normale)').add_new_form(
    'Ursaking (Lune Vermeille)',
    nom_pkmn_us='Ursaluna (Bloodmoon)',
    url_image='/images/f/fb/Ursaking_%28Lune_Vermeille%29-EV.png',
    url_son='/images/f/f6/Cri_0901_Lune_Vermeille_HOME.ogg',
    taille_m=2.7,
    poids_kg=333.0,
    talent_1='Œil Révélateur',
    talent_2=None,
    talent_cache=None,
    groupe_oeuf_1='0 % femelle ; 100 % mâle',
    ev_donne='+3 Att. Spé.',
    pv=113,
    attaque=70,
    defense=120,
    attaque_speciale=135,
    defense_speciale=65,
    vitesse=52
)


#
##
### N.905 Amovénus 
Pokemon('Amovénus').update(
    nom_pkmn='Amovénus (Avatar)',
    nom_pkmn_us='Enamorus (Incarnate)',
    talent_1='Joli Sourire',
    talent_cache='Contestation',
    taille_m=1.6
)

Pokemon('Amovénus (Avatar)').add_new_form(
    'Amovénus (Totémique)',
    nom_pkmn_us='Enamorus (Therian)',
    url_image='/images/9/99/Amov%C3%A9nus_%28Forme_Tot%C3%A9mique%29-LPA.png',
    url_son='/images/0/0b/Cri_0905_Tot%C3%A9mique_HOME.ogg',
    taille_m=1.6,
    talent_1='Envelocape',
    talent_cache=None,
    defense=110,
    defense_speciale=100,
    vitesse=46
)

#
##
### N.916 Fragrouin
# Fragrouin (♂)
Pokemon('Fragrouin').update(
    nom_pkmn='Fragrouin (♂)',
    nom_pkmn_us='Oinkologne (♂)',
    url_image='/images/b/b7/Fragroin_%28M%C3%A2le%29-EV.png',
    talent_1='Aroma-Voile',
    talent_2='Gloutonnerie',
    talent_cache='Isograisse'
)

Pokemon('Fragrouin (♂)').add_new_form(
    'Fragrouin (♀)',
    nom_pkmn_us='Oinkologne (♀)',
    url_image='/images/a/a0/Fragroin_%28Femelle%29-EV.png',
    url_son='/images/0/0f/Cri_0916_%E2%99%80_HOME.ogg',
    pv=115,
    attaque=90,
    defense=70,
    defense_speciale=90
)


#
##
### N.925 Famignol
# Ajout forme Famille de Trois
Pokemon.create(
    nom_pkmn='Famignol (Famille de Trois)',
    nom_pkmn_us='Maushold (Family of Three)',
    numero_national=925,
    url_image='/images/5/5a/Sprite_0925_Trois_EV.png',
    url_son='/images/7/77/Cri_0925_Trois_HOME.ogg',
    type_1='Normal',
    taille_m=0.3,
    poids_kg=2.3,
    talent_1='Garde-Ami',
    talent_2='Bajoues',
    talent_cache='Technicien',
    groupe_oeuf_1='Asexué',
    couleur=75,
    taux_capture=10,
    categorie='Terrestre',
    categorie_2='Féerique',
    ev_donne='+2 Vitesse',
    points_exp='165 exp.',
    exp_pour_niveau_100='800 000 exp.',
    pv=74,
    attaque=75,
    defense=70,
    attaque_speciale=65,
    defense_speciale=75,
    vitesse=111
)

Pokemon('Famignol (Famille de Trois)').add_new_form(
    'Famignol (Famille de Quatre)',
    nom_pkmn_us='Maushold (Family of Four)',
    url_image='/images/4/46/Sprite_0925_Quatre_EV.png',
    url_son='/images/5/58/Cri_0925_Quatre_HOME.ogg',
    poids_kg=2.8
)


#
##
### N.931 Tapatoès 
Pokemon('Tapatoès').update(
    talent_1='Agitation',
    talent_2='Intimidation',
    talent_cache='Cran (Plumages Vert et Bleu) / Sans Limite (Plumages Jaune et Blanc)'
)

#
##
### N.964 Superdofin
Pokemon.create(
    nom_pkmn='Superdofin (Ordinaire)',
    nom_pkmn_us='Palafin (Zero)',
    numero_national=964,
    url_image='/images/b/b7/Superdofin_%28Forme_Ordinaire%29-EV.png',
    url_son='/images/f/f0/Cri_0963_HOME.ogg',
    type_1='Eau',
    taille_m=1.3,
    poids_kg=60.2,
    talent_1='Supermutation',
    groupe_oeuf_1='50 % femelle ; 50 % mâle',
    couleur=45,
    taux_capture=40,
    categorie='Terrestre',
    categorie_2='Aquatique 2',
    ev_donne='+2 PV',
    points_exp='160 Exp.',
    exp_pour_niveau_100='1 250 000 exp.',
    pv=100,
    attaque=70,
    defense=72,
    attaque_speciale=53,
    defense_speciale=62,
    vitesse=100
)

Pokemon('Superdofin (Ordinaire)').add_new_form(
    'Superdofin (Super)',
    nom_pkmn_us='Palafin (Hero)',
    url_image='/images/9/90/Superdofin_%28Forme_Super%29-EV.png',
    url_son='/images/5/52/Cri_0964_Super_HOME.ogg',
    taille_m=1.8,
    poids_kg=97.4,
    attaque=160,
    defense=97,
    attaque_speciale=106,
    defense_speciale=87
)


#
##
### N.982 Deusolourdo
Pokemon.create(
    nom_pkmn='Deusolourdo (Double)',
    nom_pkmn_us='Dudunsparce (Two-Segment)',
    numero_national=982,
    url_image='/images/c/c4/Sprite_0982_Double_HOME.png',
    url_son='/images/5/5a/Cri_0982_HOME.ogg',
    type_1='Normal',
    taille_m=3.6,
    poids_kg=39.2,
    talent_1='Sérénité',
    talent_2='Fuite',
    talent_cache='Phobique',
    groupe_oeuf_1='50 % femelle ; 50 % mâle',
    couleur=45,
    taux_capture=20,
    categorie='Terrestre',
    ev_donne='+2 PV',
    points_exp='182 exp.',
    exp_pour_niveau_100='1 000 000'
)

Pokemon('Deusolourdo (Double)').add_new_form(
    'Deusolourdo (Triple)',
    nom_pkmn_us='Dudunsparce (Three-Segment)',
    url_image='/images/7/71/Sprite_0982_Triple_HOME.png',
    taille_m=4.5,
    poids_kg=47.4
)



#
##
### N.999 Mordudor
Pokemon.create(
    nom_pkmn='Mordudor (Coffre)',
    nom_pkmn_us='Gimmighoul (Chest)',
    numero_national=999,
    url_image='/images/b/b2/Mordudor_%28Forme_Coffre%29-EV.png',
    url_son='/images/0/0d/Cri_0999_Coffre_HOME.ogg',
    type_1='Spectre',
    taille_m=0.3,
    poids_kg=5.0,
    talent_1='Phobique',
    groupe_oeuf_1='Asexué',
    couleur=45,
    taux_capture=50,
    categorie='Inconnu',
    ev_donne='+1 Att. Spé',
    points_exp='60 exp.',
    exp_pour_niveau_100='1 250 000 exp.',
    pv=45,
    attaque=30,
    defense=25,
    attaque_speciale=75,
    defense_speciale=45,
    vitesse=80
)

Pokemon('Mordudor (Coffre)').add_new_form(
    'Mordudor (Marche)',
    nom_pkmn_us='Gimmighoul (Roaming)',
    url_image='/images/3/33/Mordudor_%28Forme_Marche%29-EV.png',
    url_son='/images/8/8f/Cri_0999_Marche_HOME.ogg',
    taille_m=0.1,
    poids_kg=0.1
)


#
##
### N.1017 Ogerpon
Pokemon('Ogerpon').update(
    nom_pkmn='Ogerpon (Masque Turquoise)',
    nom_pkmn_us='Ogerpon (Teal Mask)',
    url_image='/images/8/8d/Ogerpon_%28Masque_Turquoise%29-EV.png',
    talent_1='Acharné',
    talent_2='Force Mémorielle (sous forme téracristallisée)'
)

Pokemon('Ogerpon (Masque Turquoise)').add_new_form(
    'Ogerpon (Masque du Puits)',
    nom_pkmn_us='Ogerpon (Wellspring Mask)',
    url_image='/images/1/1d/Ogerpon_%28Masque_du_Puits%29-EV.png',
    type_2='Eau',
    talent_1='Absorb-Eau'
)

Pokemon('Ogerpon (Masque Turquoise)').add_new_form(
    'Ogerpon (Masque du Fourneau)',
    nom_pkmn_us='Ogerpon (Hearthflame Mask)',
    url_image='/images/2/26/Ogerpon_%28Masque_du_Fourneau%29-EV.png',
    type_2='Feu',
    talent_1='Brise-Moule'
)

Pokemon('Ogerpon (Masque Turquoise)').add_new_form(
    'Ogerpon (Masque de la Pierre)',
    nom_pkmn_us='Ogerpon (Cornerstone Mask)',
    url_image='/images/5/54/Ogerpon_%28Masque_de_la_Pierre%29-EV.png',
    type_2='Roche',
    talent_1='Fermeté'
)


#
##
### N.1024 Terapagos
Pokemon.create(
    nom_pkmn='Terapagos (Normale)',
    nom_pkmn_us='Terapagos (Normal)',
    numero_national=1024,
    url_image='/images/1/15/Terapagos_%28Forme_Normale%29-EV.png',
    url_son='/images/9/90/Cri_1024_HOME.ogg',
    type_1='Normal',
    taille_m=0.2,
    poids_kg=6.5,
    talent_1='Téramorphose',
    groupe_oeuf_1='50 % femelle ; 50 % mâle',
    couleur=255,
    categorie='Inconnu',
    ev_donne='+1 Défense',
    exp_pour_niveau_100='1 250 000 exp.',
    pv=90,
    attaque=65,
    defense=85,
    attaque_speciale=65,
    defense_speciale=85,
    vitesse=60
)

Pokemon('Terapagos (Normale)').add_new_form(
    'Terapagos (Téracristal)',
    nom_pkmn_us='Terapagos (Terastal)',
    url_image='/images/d/d4/Terapagos_%28Forme_Téracristal%29-EV.png',
    taille_m=0.3,
    poids_kg=16.0,
    talent_1='Téra-carapace',
    pv=95,
    attaque=95,
    defense=110,
    attaque_speciale=105,
    defense_speciale=110,
    vitesse=85
)

Pokemon('Terapagos (Normale)').add_new_form(
    'Terapagos (Stellaire)',
    nom_pkmn_us='Terapagos (Stellar)',
    url_image='/images/3/37/Sprite_1024_Stellaire_HOME.png',
    taille_m=1.7,
    poids_kg=77.0,
    talent_1='Téraformation 0',
    pv=160,
    attaque=105,
    defense=110,
    attaque_speciale=130,
    defense_speciale=110,
    vitesse=85
)
       