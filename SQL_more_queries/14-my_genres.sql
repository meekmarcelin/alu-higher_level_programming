-- list the names in database
SELECT x.name
FROM tv_genres x
JOIN tv_show_genres y ON x.id = y.genre_id
JOIN tv_shows s ON s.id = y.show_id
WHERE  s.title = 'Dexter'
ORDER BY x.name ASC;
