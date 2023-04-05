from src import models

Movie = models.Movie
db = models.db

class MovieRepository:
    def __init__(self) -> None:
        # In memory database which is a simple list of movies
        self.movies: list[models.Movie] = []

    def get_all_movies(self):
        return self.movies

    def get_movie_by_id(self, movie_id):
        # Perform a linear search through the in-memory database
        for movie in self.movies:
            # If the movie title matches, return the movie
            if movie.movie_id == movie_id:
                return movie
        # If we made it this far, no movies matched so return None
        return None

    def create_movie(self, newTitle, newDirector, newRating):
        # Create the movie instance
        #newID = models.Movie.query.filter_by(models.Movie.movie_id).last() + 1
        newID = 1
        print("NewID =", newID)
        new_movie = models.Movie(movie_id = newID, title = newTitle, director = newDirector, rating = newRating)
        # Save the instance in our in-memory database
        self.movies.append(new_movie)
        db.session.add(new_movie)
        db.session.commit()
        # Return the movie instance
        return None

    def search_movies(self, title):
        # Perform a linear search through the in-memory database
        for movie in self.movies:
            # If the movie title matches, return the movie
            if movie.title.lower() == title.lower():
                return movie
        # If we made it this far, no movies matched so return None
        return None

# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
