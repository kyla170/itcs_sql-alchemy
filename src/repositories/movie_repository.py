from src import models

Movie = models.Movie
db = models.db

class MovieRepository:
    def __init__(self) -> None:
        # In memory database which is a simple list of movies
        self.movies: list[models.Movie] = []

    def get_all_movies(self):
        return Movie.query.all()

    def get_movie_by_id(self, movie_id):
        allMovies = self.get_all_movies()
        # Perform a linear search through the in-memory database
        for mov in allMovies:
            # If the movie title matches, return the movie
            if mov.movie_id == movie_id:
                return mov
        # If we made it this far, no movies matched so return None
        return None

    def create_movie(self, newTitle, newDirector, newRating):
        # Create the movie instance
        newID = Movie.query.last().id + 1
        print("NewID =", newID)
        new_movie = Movie(movie_id = newID, title = newTitle, director = newDirector, rating = newRating)
        # Save the instance in our in-memory database
        self.movies.append(new_movie)
        db.session.add(new_movie)
        db.session.commit()
        # Return the movie instance
        return None

    def search_movies(self, title):
        allMovies = self.get_all_movies()
        # Perform a linear search through the in-memory database
        for mov in allMovies:
            # If the movie title matches, return the movie
            if mov.title.lower() == title.lower():
                return mov
        # If we made it this far, no movies matched so return None
        return None

# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
