CREATE TABLE IF NOT EXISTS Genre (
	id SERIAL PRIMARY KEY, 
	genre_title VARCHAR(40) NOT NULL
	);
	

CREATE TABLE IF NOT EXISTS Artist (
	id SERIAL PRIMARY KEY, 
	name VARCHAR(40) NOT NULL
	);


CREATE TABLE IF NOT EXISTS GenreArtist (
	genre_id INTEGER NOT NULL REFERENCES Genre(id),
	artist_id INTEGER NOT NULL REFERENCES Artist(id),
	CONSTRAINT pk_GenreArtist PRIMARY KEY (genre_id, artist_id)
	);


CREATE TABLE IF NOT EXISTS Album (
	id SERIAL PRIMARY KEY,
	album_title VARCHAR(40) NOT NULL,
	album_released smallint NOT NULL
	);
	

CREATE TABLE IF NOT EXISTS ArtistAlbum (
	artist_id INTEGER NOT NULL REFERENCES Artist(id),
	album_id INTEGER NOT NULL REFERENCES Album(id),
	CONSTRAINT pk_ArtistAlbum PRIMARY KEY (artist_id, album_id)
	);
	

CREATE TABLE IF NOT EXISTS Track (
	id SERIAL PRIMARY KEY,
	album_id INTEGER NOT NULL REFERENCES Album(id),
	track_title VARCHAR(40) NOT NULL,
	lenght time NOT NULL
	);
	

CREATE TABLE IF NOT EXISTS Collection (
	id SERIAL PRIMARY KEY,
	collection_title VARCHAR(40) NOT NULL,
	collection_released smallint NOT NULL
	);
	

CREATE TABLE IF NOT EXISTS CollectionTrack (
	collection_id INTEGER NOT NULL REFERENCES Collection(id),
	track_id INTEGER NOT NULL REFERENCES Track(id),
	CONSTRAINT pk_CollectionTrack PRIMARY KEY (collection_id, track_id)
	);