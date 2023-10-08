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
INSERT INTO genres (genre_name) VALUES ('Thriller');
INSERT INTO genres (genre_name) VALUES ('Sci-Fi');
INSERT INTO genres (genre_name) VALUES ('Romance');
INSERT INTO genres (genre_name) VALUES ('Horror');
INSERT INTO genres (genre_name) VALUES ('Fantasy');
INSERT INTO genres (genre_name) VALUES ('Action');
INSERT INTO genres (genre_name) VALUES ('Comedy');
INSERT INTO genres (genre_name) VALUES ('Drama');

-- Insert sample movies
INSERT INTO movies (title, genre_id, release_year, director) VALUES ('Movie A', 1, 2022, 'Director A');
INSERT INTO movies (title, genre_id, release_year, director) VALUES ('Movie B', 2, 2021, 'Director B');
INSERT INTO movies (title, genre_id, release_year, director) VALUES ('Thriller Movie 1', 1, 2022, 'Director X');
INSERT INTO movies (title, genre_id, release_year, director) VALUES ('Sci-Fi Movie 1', 2, 2022, 'Director Y');
INSERT INTO movies (title, genre_id, release_year, director) VALUES ('Romance Movie 1', 3, 2022, 'Director Z');
INSERT INTO movies (title, genre_id, release_year, director) VALUES ('Horror Movie 1', 4, 2022, 'Director W');
INSERT INTO movies (title, genre_id, release_year, director) VALUES ('Fantasy Movie 1', 5, 2022, 'Director V');

-- Insert sample ratings
INSERT INTO ratings (movie_id, rating, review_text) VALUES (1, 4.5, 'Great action scenes!');
INSERT INTO ratings (movie_id, rating, review_text) VALUES (2, 3.8, 'Hilarious comedy movie.');
INSERT INTO ratings (movie_id, rating, review_text) VALUES (1, 8.5, 'Exciting thriller plot!');
INSERT INTO ratings (movie_id, rating, review_text) VALUES (2, 9.2, 'Mind-bending sci-fi experience.');
INSERT INTO ratings (movie_id, rating, review_text) VALUES (3, 7.9, 'Heartwarming romance story.');
INSERT INTO ratings (movie_id, rating, review_text) VALUES (4, 7.2, 'Scary horror elements, well-executed.');
INSERT INTO ratings (movie_id, rating, review_text) VALUES (5, 8.0, 'Imaginative fantasy world, loved it!');