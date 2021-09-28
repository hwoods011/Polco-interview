insert into user (username, firstname, lastname) values ('hwoods', 'hayden', 'woods');

insert into genre (name) values ('Rock');
insert into genre (name) values ('Alternative');

insert into artist (name, genre_id) values ('Glass Animals', (select id from genre where name='Alternative'));

insert into album (name, artist_id) values ('Dreamland', (select id from artist where name='Glass Animals'));

insert into song (name, artist_id, album_id) values ('Heat Waves', (select id from artist where name='Glass Animals'), (select id from album where name='Dreamland'));

insert into user_favorites (user_id, song_id) values ((select id from song where name='Heat Waves'), (select id from user where username='hwoods'));

insert into billboard_list (rank, song_id) values (16, (select id from song where name='Heat Waves'));