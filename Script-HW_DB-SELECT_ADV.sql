--количество исполнителей в каждом жанре;
SELECT genre_title, count(artist_id) AS artist_tally
FROM genre AS g
JOIN genreartist AS ga ON g.id = ga.genre_id  
GROUP BY g.genre_title;


--количество треков, вошедших в альбомы 2019-2020 годов;
SELECT count(track_title) AS track_tally
FROM album AS alb
JOIN track AS t ON alb.id = t.album_id
WHERE album_released = 2019 OR album_released = 2020;


--средняя продолжительность треков по каждому альбому;
SELECT album_title, AVG(lenght) AS avd_lenght
FROM album AS alb 
JOIN track AS t ON alb.id = t.album_id
GROUP BY album_title;


--все исполнители, которые не выпустили альбомы в 2020 году;
SELECT DISTINCT name
FROM artist AS art
JOIN artistalbum AS aa ON art.id = aa.artist_id
JOIN album AS alb ON aa.album_id = alb.id
WHERE alb.album_released != 2020;


--названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
SELECT DISTINCT collection_title
FROM collection AS col
JOIN collectiontrack ct ON col.id = ct.collection_id
JOIN track AS t ON ct.track_id = t.id
JOIN album AS alb ON t.album_id = alb.id
JOIN artistalbum AS aa ON alb.id = aa.album_id
JOIN artist AS art ON aa.artist_id = art.id
WHERE name = 'U2';


--название альбомов, в которых присутствуют исполнители более 1 жанра;
SELECT album_title
FROM album AS alb
JOIN artistalbum AS aa ON alb.id = aa.album_id
JOIN artist AS art ON aa.artist_id = art.id
JOIN genreartist AS ga ON art.id = ga.artist_id
GROUP BY album_title
HAVING count(genre_id) > 1;


--наименование треков, которые не входят в сборники;
SELECT track_title
FROM track AS t
LEFT JOIN collectiontrack AS ct ON ct.track_id = t.id
WHERE ct.track_id IS NULL;


--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
SELECT name
FROM artist AS art
JOIN artistalbum AS aa ON art.id = aa.artist_id 
JOIN album AS alb ON aa.album_id  = alb.id
JOIN track AS t ON alb.id = t.album_id 
WHERE lenght = (SELECT MIN(lenght) FROM track);


--название альбомов, содержащих наименьшее количество треков.
WITH track_count AS (
SELECT album_id, COUNT(track_title) AS track_tally
FROM track 
GROUP BY album_id)
SELECT album_title
FROM album
JOIN track_count ON album.id = track_count.album_id 
WHERE track_tally = (SELECT MIN(track_tally) FROM track_count);
