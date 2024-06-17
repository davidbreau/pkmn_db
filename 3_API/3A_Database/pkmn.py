from typing import List
from sqlalchemy.orm import Session
from .models import NotFoundError, Pokemon, Type_Pkmn, Capacite, GO_Capacite, Talent, EfficaciteDeType, Apprentissage, GO_Apprentissage, Evolution
import string



######################################################################
############################## CREATE ################################
######################################################################


#_______________________________________________________________TABLES

def create_pokemon(pokemon: Pokemon, session: Session) -> Pokemon:
    db_pokemon = Pokemon(**pokemon.model_dump(exclude_none=True))
    session.add(db_pokemon)
    session.commit()
    session.refresh(db_pokemon)
    return

def create_type(type_pkmn: Type_Pkmn, session: Session) -> Type_Pkmn:
    db_type_pkmn = Type_Pkmn(**type_pkmn.model_dump(exclude_none=True))
    session.add(db_type_pkmn)
    session.commit()
    session.refresh(db_type_pkmn)
    return type_pkmn

def create_capacite(capacite: Capacite, session: Session) -> Capacite:
    db_capacite = Capacite(**capacite.model_dump(exclude_none=True))
    session.add(db_capacite)
    session.commit()
    session.refresh(db_capacite)
    return db_capacite

def create_go_capacite(go_capacite: GO_Capacite, session: Session) -> GO_Capacite:
    db_go_capacite = GO_Capacite(**go_capacite.model_dump(exclude_none=True))
    session.add(db_go_capacite)
    session.commit()
    session.refresh(db_go_capacite)
    return db_go_capacite

def create_talent(talent: Talent, session: Session) -> Talent:
    db_talent = Talent(**talent.model_dump(exclude_none=True))
    session.add(db_talent)
    session.commit()
    session.refresh(db_talent)
    return db_talent


#______________________________________________ TABLES D'ASSOCIATIONS

def create_efficacite_des_types(efficacite: EfficaciteDeType, session: Session) -> EfficaciteDeType:
    db_efficacite = EfficaciteDeType(**efficacite.model_dump(exclude_none=True))
    session.add(db_efficacite)
    session.commit()
    session.refresh(db_efficacite)
    return db_efficacite

def create_evolution(evolution: Evolution, session: Session) -> Evolution:
    db_evolution = Evolution(**evolution.model_dump(exclude_none=True))
    session.add(db_evolution)
    session.commit()
    session.refresh(db_evolution)
    return db_evolution

def create_apprentissage(apprentissage: Apprentissage, session: Session) -> Apprentissage:
    db_apprentissage = Apprentissage(**apprentissage.model_dump(exclude_none=True))
    session.add(db_apprentissage)
    session.commit()
    session.refresh(db_apprentissage)
    return db_apprentissage

def create_go_apprentissage(go_apprentissage: GO_Apprentissage, session: Session) -> GO_Apprentissage:
    db_go_apprentissage = GO_Apprentissage(**go_apprentissage.model_dump(exclude_none=True))
    session.add(db_go_apprentissage)
    session.commit()
    session.refresh(db_go_apprentissage)
    return db_go_apprentissage




######################################################################
############################### READ #################################
######################################################################


##### SINGLE ENTRY READ

def read_one_pkmn(nom_pkmn: str, session: Session) -> Pokemon:
    db_pokemon = session.query(Pokemon).filter(Pokemon.nom_pkmn == nom_pkmn).first()
    if db_pokemon is None:
        raise NotFoundError(f'No Pokemon name found with {nom_pkmn}')
    return db_pokemon

def read_one_type(type_pkmn: str, session: Session) -> Type_Pkmn:
    db_type = session.query(Type_Pkmn).filter(Type_Pkmn.type_pkmn == type_pkmn).first()
    if db_type is None:
        raise NotFoundError(f'No {type_pkmn} Type found')
    return type

def read_one_capacite(capacite: str, session: Session) -> Capacite:
    db_capacite = session.query(Capacite).filter(Capacite.capacite == capacite).first()
    if db_capacite is None:
        raise NotFoundError(f'No capacite found with name : {capacite}')
    return db_capacite

def read_one_go_capacite(go_capacite: str, session: Session) -> GO_Capacite:
    db_go_capacite = session.query(GO_Capacite).filter(GO_Capacite.capacite ==  go_capacite).first()
    if db_go_capacite is None:
        raise NotFoundError(f'No go_capacite found with name: {go_capacite}')
    return db_go_capacite

def read_db_one_talent(talent: str, session: Session) -> Talent:
    db_talent = session.query(Talent).filter(Talent.talent == talent).first()
    if db_talent is None:
        raise NotFoundError(f'No talent found with name: {talent}')
    return db_talent

##### MULTIPLE ENTRY READ

def read_db_

