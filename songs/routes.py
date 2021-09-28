from . import app
from .db import get_db

@app.route('/')
def test():
    return 'OK'

@app.route('/users')
def users():
    db = get_db()
    users = db.execute('select * from user').fetchall()
    output = dict()
    output['users'] = []
    for user in users:
        output['users'].append({'id': user['id'], 'username': user['username'], 'firstname': user['firstname'], 'lastname': user['lastname']})
    return output

@app.route('/favorites/<username>')
def getUserFavorites(username):
    db = get_db()
    # Not pretty, would want likely want to switch to an ORM or at least move queries to files
    favorites = db.execute("""select bl.rank as 'song_rank', s.name as 'Song_Name', art.name as 'Artist_name', alb.name as 'Album_name', genre.name as 'genre_name' from user_favorites uf 
join user u on uf.user_id = u.id
join song s on uf.song_id = s.id 
join artist art on s.artist_id = art.id
join album alb on s.album_id = alb.id
join genre on art.genre_id = genre.id
join billboard_list bl on s.id = bl.song_id
where u.username = ?;
""", (username,)).fetchall()
    output = dict()
    output['favorites'] = []
    for fave in favorites:
        output['favorites'].append({ 'rank': fave['song_rank'], 'song': fave['song_name'], 'artist': fave['artist_name'], 'album': fave['album_name'], 'genre': fave['genre_name']})
    return output