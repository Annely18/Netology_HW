
-- название и год выхода альбомов, вышедших в 2018 году;
SELECT album_title, album_released FROM album
WHERE album_released = 2018;

-- название и продолжительность самого длительного трека;
SELECT track_title, lenght FROM track 
WHERE lenght = (SELECT MAX(lenght) FROM track);

-- название треков, продолжительность которых не менее 3,5 минуты;
SELECT track_title FROM track
WHERE lenght >= '3:30';

-- названия сборников, вышедших в период с 2018 по 2020 год включительно;
SELECT collection_title FROM collection
WHERE  collection_released BETWEEN 2018 AND 2020;

-- исполнители, чье имя состоит из 1 слова;
SELECT name FROM artist
WHERE name NOT LIKE '% %';

-- название треков, которые содержат слово "мой"/"my".
SELECT track_title FROM track
WHERE track_title LIKE '%My%' OR track_title LIKE '%Мой%';
