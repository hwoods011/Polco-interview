
# File that I was going to use when I was going to try to use an ORM

"""
from sqlalchemy import Column, String, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy(app)
# not used anymore
class Genre(db.Model):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    genre_name = Column(String)

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)




class Artist(db.Model):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre_id = Column(Integer,ForeignKey('genre.id'))

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)





class Album(db.Model):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(Integer,ForeignKey('artist.id'))

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)



class Song(db.Model):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(Integer,ForeignKey('artist.id'))
    album_id = Column(Integer, ForeignKey('album.id'))

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)



class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)

    # Got from https://stackoverflow.com/a/1639249
    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

class UserFavorites(db.Model):
    __tablename__ = 'favorites'
    user_id = Column(Integer,ForeignKey('user.id'), primary_key=True)
    song_id = Column(Integer,ForeignKey('song.id'), primary_key=True)

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)



class_map = {'Genre': Genre, 'Artist': Artist, 'Album': Album, 'Song': Song, 'User': User, 'UserFavorites': UserFavorites}

def seedClass(classType, data):
    d = classType(data)
    db.session.add(d)

if __name__ == '__main__':
    print('here')

    db.create_all()
    #test = User(username='test', firstname='t', lastname='est')
    with open('./seed_data.json', 'r') as f:
        data =json.load(f)

    classType = None
    classStr = ''
    for k,v in data.items():
        print(k)
        print(v)
        if k == 'class':
            # will blow up if not a valid class
            classType =  class_map.get(v)

        elif classType :
            for row in v:
                seedClass(classType, row )

            
            
    #db.session.add(data)
    db.session.commit()

"""

