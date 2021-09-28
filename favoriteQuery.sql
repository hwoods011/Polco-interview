select s.name as 'Song_Name', art.name as 'Artist_name', alb.name as 'Album_name', genre.name as 'genre_name' from userFavorites uf 
join user u on uf.user_id = u.id
join song s on uf.song_id = s.id 
join artist art on s.artist_id = art.id
join album alb on s.album_id = alb.id
join genre on art.genre_id = genre.id
where u.username = ?;
