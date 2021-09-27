# flask_sqlalchemy/models.py
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite+pysqlite:///:memory:', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(Integer,ForeignKey(''))
    album_id = Column(Integer, ForeignKey('album.id'))

class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre_id = Column(Integer,ForeignKey('artist.id'))

class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre_id = Column(Integer,ForeignKey('genre.id'))

class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    genre_name = Column(String)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
