drop table if exists user;
drop table if exists genre;
drop table if exists artist;
drop table if exists album;
drop table if exists song;
drop table if exists user_favorites;
drop table if exists billboard_list;



CREATE TABLE user (
  id INTEGER PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL
);

CREATE TABLE genre (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE NOT NULL
);


CREATE TABLE artist (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  genre_id INTEGER not null,
  FOREIGN KEY(genre_id) REFERENCES genre(id)
);

CREATE TABLE album (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  artist_id INTEGER not null,
  FOREIGN KEY(artist_id) REFERENCES artist(id)
);


CREATE TABLE song (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  artist_id INTEGER not null,
  album_id INTEGER not null,
  FOREIGN KEY(artist_id) REFERENCES artist(id),
  FOREIGN KEY(album_id) REFERENCES album(id)
);

CREATE TABLE user_favorites (
  user_id INTEGER not null ,
  song_id INTEGER not null,
  FOREIGN KEY(user_id) REFERENCES user(id),
  FOREIGN KEY(song_id) REFERENCES song(id),
  PRIMARY KEY(user_id, song_id)
);

CREATE TABLE billboard_list (
  rank INTEGER not null,
  song_id INTEGER not null,
  FOREIGN KEY(song_id) REFERENCES song(id),
  PRIMARY KEY(rank, song_id)
);


