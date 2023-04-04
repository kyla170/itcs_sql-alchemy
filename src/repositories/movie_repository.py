from src import models

class MovieRepository:
    dbase = models.db

    def __init__(self) -> None:
        # In memory database which is a simple list of movies
        self.database: list[models.Movie] = []

    def get_all_movies(self):
        # TODO get all movies from the DB
        return self.database

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        # Perform a linear search through the in-memory database
        for movie in self.database:
            # If the movie title matches, return the movie
            if movie.movie_id == movie_id:
                return movie
        # If we made it this far, no movies matched so return None
        return None

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        # Create the movie instance
        movie = models.Movie(title, director, rating)
        # Save the instance in our in-memory database
        self.database.append(movie)
        # Return the movie instance
        return None

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        # Perform a linear search through the in-memory database
        for movie in self.database:
            # If the movie title matches, return the movie
            if movie.title == title:
                return movie
        # If we made it this far, no movies matched so return None
        return None

# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
