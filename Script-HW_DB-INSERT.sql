INSERT INTO Genre (genre_title)
VALUES ('Pop'), ('Dance'), ('Rock'), ('Alternative'), ('Blues');

INSERT INTO Artist (name)
VALUES ('Madonna'), ('Linkin Park'), ('Joe Cocker'), ('Lady Gaga'), ('Shakira'), ('Reamonn'), ('U2'), ('Imagine Dragons');

INSERT INTO Album (album_title, album_released)
VALUES ('Eleven', 2010), ('Hybrid Theory', 2000), ('No Ordinary World', 1999), ('Chromatica', 2020), ('El Dorado', 2017), ('Madame X', 2019), ('How to Dismantle an Atomic Bomb', 2004), ('Mercury — Act 1', 2021), ('Origins ', 2018);

INSERT INTO Track (album_id, track_title, lenght)
VALUES (1, 'Yesterday', '02:51'), (1, 'Colder', '03:09'), (2, 'A Place for My Head', '3:04'), (2, 'Crawling', '3:29'), (3, 'On My Way Home', '4:13'), (4, 'Stupid Love', '03:13'), (4, '1000 Doves', '03:35'), (5, 'Deja Vu', '03:16'), (6, 'I Don’t Search I Find', '04:08'), (6, 'God Control', '06:19'), (7, 'Crumbs from Your Table', '05:03'), (7, 'Sometimes You Can’t Make It on Your Own', '05:08'), (9, 'Digital', '03:21'), (9, 'Love', '02:46'), (8, 'My Life', '03:44'), (8, 'No Time for Toxic People', '3:27');

INSERT INTO GenreArtist
VALUES (1, 1), (2, 1), (3, 1), (3, 2), (4, 2), (5, 3), (1, 4), (2, 4), (1, 5), (2, 5), (3, 6), (3, 7), (3, 8), (4, 8), (1, 8);

INSERT INTO ArtistAlbum
VALUES (6, 1), (2, 2), (3, 3), (4, 4), (5, 5), (1, 6), (7, 7), (8, 8), (8, 9);

INSERT INTO Collection (collection_title, collection_released)
VALUES ('Retro', 2019), ('Best of Imagine Dragons', 2021), ('Dance', 2020), ('Blues', 2005), ('Rock', 2011), ('Pop', 2020), ('Latina', 2018), ('Medley', 2022);

INSERT INTO CollectionTrack
VALUES (1, 3), (1, 4), (1, 11), (1, 12), (2, 14), (2, 13), (2, 15), (2, 16), (3, 8), (3, 7), (3, 6), (4, 5), (6, 11), (6, 12), (6, 2), (6, 1), (7, 8), (8, 1), (8, 2), (8, 3), (8, 5), (8, 7), (8, 9), (8, 11), (8, 15);
