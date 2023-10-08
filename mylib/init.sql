-- Create a table for movie genres
CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(255) NOT NULL
);

-- Create a table for movies
CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre_id INT,
    release_year INT,
    director VARCHAR(255),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

-- Create a table for movie ratings
CREATE TABLE ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    rating DECIMAL(3, 1) NOT NULL,
    review_text TEXT,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);


Certainly! If you want to create a database schema and populate it with a different entity besides authors, you can modify the SQL script accordingly. Let's consider an example where you want to work with a database related to "Movies". Here's how you could modify the script for a movies-related dataset:

1. Modify Table Structure for Movies:
sql
Copy code
-- Create a table for movie genres
CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(255) NOT NULL
);

-- Create a table for movies
CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre_id INT,
    release_year INT,
    director VARCHAR(255),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

-- Create a table for movie ratings
CREATE TABLE ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    rating DECIMAL(3, 1) NOT NULL,
    review_text TEXT,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

INSERT INTO genres (genre_name) VALUES ('Action');
INSERT INTO genres (genre_name) VALUES ('Comedy');
INSERT INTO genres (genre_name) VALUES ('Drama');

-- Insert sample movies
INSERT INTO movies (title, genre_id, release_year, director) VALUES ('Movie A', 1, 2022, 'Director A');
INSERT INTO movies (title, genre_id, release_year, director) VALUES ('Movie B', 2, 2021, 'Director B');

-- Insert sample ratings
INSERT INTO ratings (movie_id, rating, review_text) VALUES (1, 4.5, 'Great action scenes!');
INSERT INTO ratings (movie_id, rating, review_text) VALUES (2, 3.8, 'Hilarious comedy movie.');