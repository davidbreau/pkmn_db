from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel

class NotFoundError(Exception):
    pass


class Base(DeclarativeBase):
    pass

#####################################################
############## USERS DATABASE CLASSES ###############
#####################################################

class DBUser(Base):
    __tablename__ = "Users"

    user_id: Mapped[str] = mapped_column(primary_key=True, index=True)
    username: Mapped[str]
    email: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    hashed_password: Mapped[str]
    
class DBToken(Base):
    __tablename__ = "Tokens"

    username: Mapped[str] = mapped_column(primary_key=True, index=True)
    token: Mapped[str]
    
#####################################################
############### PKMN DATABASE CLASSES ###############
#####################################################

class Pokemon(BaseModel):
    __tablename__ = "Pokemons"
    
    nom_pkmn: str
    num_pokedex: int
    generation: int
    region: str
    type_1: str
    type_2: str 
    taille_m: float
    poids_kg: float
    talent_1: str
    talent_2: str
    talent_cache: str
    sexe: str
    taux_de_capture: int
    cycle_eclosion: int
    groupe_oeuf_1: str
    groupe_oeuf_2: str
    points_effort: str
    point_exp: str
    exp_niv100: str
    pv: int
    attaque: int
    attaque_speciale: int
    defense: int
    defense_speciale: int
    vitesse: int
    GO_attaque: int
    GO_defense: int
    GO_resistanc: int
    GO_Buddy_Distance_Km: int

class Type_Pkmn(BaseModel):
    __tablename__ = "Types"
    
    type_pkmn: str
    generation: int

class Capacite(BaseModel):
    __tablename__ = "Capacites"
    
    capacite: str
    type_pkmn: str
    categorie: str
    pp: int
    puissance: int
    cible: str
    taux_critique: int
    priorite: int
    effet: str
    
class GO_Capacite(BaseModel):
    __tablename__ = "GO_Capacites"
    
    capacite: str
    type_pkmn: str
    categorie: str
    raids_dommage: int
    raids_delai_recuperation: float
    raids_gain_energie: int
    raids_temps_dommage: float
    pvp_dommage: int
    pvp_delai_recuperation: int
    pvp_gain_energie: int
    pvp_cout_energie: int
    stats_boost: str
    
class Talent(BaseModel):
    __tablename__ = "Talents"
    
    talent: str
    generation: int
    effet: str

class EfficaciteDeType(BaseModel):
    __tablename__ = "EfficaciteDesTypes"
    
    type_offensif: str
    type_deffensif: str
    multiplicateur: float
    GO_multiplicateur: float

class Evolution(BaseModel):
    __tablename__ = "Evolutions"
    
    pre_evolution: str
    evolution: str
    niveau: int
    condition: str
    objet: str
    GO_Bonbons: str
    GO_Condition: str

class Apprentissage(BaseModel):
    __tablename__ = "Apprentissages"
    
    nom_pkmn: str
    capacite: str
    generation: int
    ct: int
    dt: int
    reproduction: bool

class GO_Apprentissage(BaseModel):
    __tablename__ = "GO_Apprentissages"
    
    nom_pkmn: str
    capacite: str
    elite: bool
