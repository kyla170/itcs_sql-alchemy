from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Movie({self.movie_id}, {self.title}, {self.director}, {self.rating})'