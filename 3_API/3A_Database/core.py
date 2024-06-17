from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

PKMN_DATABASE_URL = 'sqlite:///2_Data/pkmn.db'
USERS_DATABASE_URL = 'sqlite:///2_Data/users.db'

# class NotFoundError(Exception):
#     pass

# class Base(DeclarativeBase):
#     pass

# class DBUsers(Base):

#     __tablename__ = "Users"

#     user_id: Mapped[str] = mapped_column(primary_key=True, index=True)
#     username: Mapped[str]
#     email: Mapped[str]
#     first_name: Mapped[str]
#     last_name: Mapped[str]
#     hashed_password: Mapped[str]
    
# class DBToken(Base):
    
#     __tablename__ = "Tokens"
    
#     username: Mapped[str] = mapped_column(primary_key=True, index=True)
#     token: Mapped[str]

engine_users = create_engine(USERS_DATABASE_URL)
engine_pkmn = create_engine(PKMN_DATABASE_URL)

SessionLocalUsers = sessionmaker(autocommit=False, autoflush=False, bind=engine_users)
SessionLocalPkmn = sessionmaker(autocommit=False, autoflush=False, bind=engine_pkmn)

def get_db_users():
    db = SessionLocalUsers()
    try:
        yield db
    finally:
        db.close()

def get_db_pkmn():
    db = SessionLocalPkmn()
    try:
        yield db
    finally:
        db.close()