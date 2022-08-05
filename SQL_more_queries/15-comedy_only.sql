-- list all tv shows
SELECT x.title
FROM tv_shows x
JOIN tv_show_genres y ON x.id = y.show_id
JOIN tv_genres s ON y.genre_id = s.id
WHERE s.name = 'comedy'
ORDER BY a.title ASC;
