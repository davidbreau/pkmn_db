-- EXECUTE THIS FILE TO CREATE PKMN.DB TABLES
-- RUN BASH COMMAND : sqlite3 2_Data/pkmn.db < 1_Databases_Building/pkmn/create_pkmn_tables.sql

-- ####################################################################################
-- ################################### TABLES #########################################
-- ####################################################################################

-- POKEMON
CREATE TABLE IF NOT EXISTS Pokemons (
    nom_pkmn TEXT PRIMARY KEY,
    num_pokedex INTEGER,
    generation INTEGER,
    region TEXT,
    type_1 TEXT,
    type_2 TEXT NULL, 
    taille_m FLOAT,
    poids_kg FLOAT,
    talent_1 TEXT,
    talent_2 TEXT NULL,
    talent_cache TEXT NULL,
    sexe TEXT NULL,
    taux_de_capture INTEGER,
    cycle_eclosion INTEGER NULL,
    groupe_oeuf_1 TEXT,
    groupe_oeuf_2 TEXT NULL,
    points_effort TEXT,
    point_exp TEXT,
    exp_niv100 TEXT,
    pv INTEGER,
    attaque INTEGER,
    attaque_speciale INTEGER,
    defense INTEGER,
    defense_speciale INTEGER,
    vitesse INTEGER,
    GO_attaque INTEGER NULL,
    GO_defense INTEGER NULL,
    GO_resistance INTEGER NULL,
    GO_Buddy_Distance_Km INTEGER NULL,
    FOREIGN KEY (nom_pkmn) REFERENCES Evolutions(pre_evolution),
    FOREIGN KEY (nom_pkmn) REFERENCES Evolutions(evolution),
    FOREIGN KEY (nom_pkmn) REFERENCES Apprentissages(nom_pkmn),
    FOREIGN KEY (nom_pkmn) REFERENCES GO_Apprentissages(nom_pkmn),
    FOREIGN KEY (type_1) REFERENCES Types(type_pkmn),
    FOREIGN KEY (type_2) REFERENCES Types(type_pkmn),
    FOREIGN KEY (talent_1) REFERENCES Talents(talent),
    FOREIGN KEY (talent_2) REFERENCES Talents(talent),
    FOREIGN KEY (talent_cache) REFERENCES Talents(talent)
);

-- TYPE
CREATE TABLE IF NOT EXISTS Types (
    type_pkmn TEXT PRIMARY KEY,
    generation INTEGER,
    FOREIGN KEY (type_pkmn) REFERENCES Pokemons(type_1),
    FOREIGN KEY (type_pkmn) REFERENCES Pokemons(type_2),
    FOREIGN KEY (type_pkmn) REFERENCES Capacites(type_pkmn),
    FOREIGN KEY (type_pkmn) REFERENCES GO_Capacites(type_pkmn),
    FOREIGN KEY (type_pkmn) REFERENCES Efficacite_des_types(type_offensif),
    FOREIGN KEY (type_pkmn) REFERENCES Efficacite_des_types(type_deffensif)
);

-- CAPACITE
CREATE TABLE IF NOT EXISTS Capacites (
    capacite TEXT PRIMARY KEY,
    type_pkmn TEXT,
    categorie TEXT,
    pp INTEGER,
    puissance INTEGER NULL,
    cible TEXT,
    taux_critique INTEGER NULL,
    priorite INTEGER,
    effet TEXT,
    FOREIGN KEY (capacite) REFERENCES Apprentissage(nom_pk),
    FOREIGN KEY (type_pkmn) REFERENCES Types(type_pkmn)
);


-- CAPACITE (Pokemon GO)
CREATE TABLE IF NOT EXISTS GO_Capacites (
    capacite TEXT PRIMARY KEY,
    type_pkmn TEXT,
    categorie TEXT,
    raids_dommage INTEGER,
    raids_delai_recuperation FLOAT,
    raids_gain_energie INTEGER NULL,
    raids_temps_dommage FLOAT,
    pvp_dommage INTEGER,
    pvp_delai_recuperation INTEGER NULL,
    pvp_gain_energie INTEGER NULL,
    pvp_cout_energie INTEGER,
    stats_boost TEXT NULL,
    FOREIGN KEY (capacite) REFERENCES GO_Apprentissage(capacite),
    FOREIGN KEY (type_pkmn) REFERENCES Types(type_pkmn)
);


-- TALENT
CREATE TABLE IF NOT EXISTS Talents (
    talent TEXT PRIMARY KEY,
    generation INTEGER,
    effet TEXT,
    FOREIGN KEY (talent) REFERENCES Pokemons(talent_1),
    FOREIGN KEY (talent) REFERENCES Pokemons(talent_2),
    FOREIGN KEY (talent) REFERENCES Pokemons(talent_cache)
);

-- ####################################################################################
-- ############################## TABLES D'ASSOCIATIONS ###############################
-- ####################################################################################

-- EFFICACITE DES TYPES // Type à Type
CREATE TABLE IF NOT EXISTS Efficacite_des_types (
    type_offensif TEXT,
    type_deffensif TEXT,
    multiplicateur FLOAT,
    GO_multiplicateur FLOAT,
    FOREIGN KEY (type_offensif) REFERENCES Types(type_pkmn),
    FOREIGN KEY (type_deffensif) REFERENCES Types(type_pkmn)
);


-- EVOLUTION // Pokemon - Pokemon 
CREATE TABLE IF NOT EXISTS Evolutions (
    pre_evolution TEXT NOT NULL,
    evolution TEXT NOT NULL,
    niveau INTEGER NULL,
    condition TEXT NULL,
    objet TEXT NULL,
    GO_Bonbons TEXT NULL,
    GO_Condition TEXT NULL,
    FOREIGN KEY (pre_evolution) REFERENCES Pokemons(nom_pkmn),
    FOREIGN KEY (evolution) REFERENCES Pokemons(nom_pkmn)
);


-- APPRENTISSAGE // Pokemon - Capacite
CREATE TABLE IF NOT EXISTS Apprentissages (
    nom_pkmn TEXT,
    capacite TEXT,
    generation INTEGER,
    ct INTEGER NULL,
    dt INTEGER NULL,
    reproduction BOOLEAN,
    FOREIGN KEY (nom_pkmn) REFERENCES Pokemons(nom_pkmn),
    FOREIGN KEY (capacite) REFERENCES Capacites(capacite)
);


-- APPRENTISSAGE (Pokemon GO) // Pokemon - GO_Capacite
CREATE TABLE IF NOT EXISTS GO_Apprentissages (
    nom_pkmn TEXT,
    capacite TEXT,
    elite BOOLEAN,
    FOREIGN KEY (nom_pkmn) REFERENCES Pokemons(nom_pkmn),
    FOREIGN KEY (capacite) REFERENCES Capacites(capacite)
);

