-- Re/create DB
DROP DATABASE IF EXISTS movies;
CREATE DATABASE movies;
USE movies;

-- Create movie table
CREATE TABLE movie (
    movie_id INT          AUTO_INCREMENT,
    title    VARCHAR(255) NOT NULL,
    director VARCHAR(255) NOT NULL,
    rating   INT NOT      NULL,
    PRIMARY KEY (movie_id)
);
