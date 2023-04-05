from flask import Flask, abort, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton
from src.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=\
    'mysql://root:abc123@localhost:3306/movies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    py_movies = movie_repository_singleton.get_all_movies()
    return render_template('list_all_movies.html', movies=py_movies, list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)

@app.post('/movies/new')
def create_movie():
    # These variables are fetched from /movies/new
    py_movie = request.form.get('movie')
    py_director = request.form.get('director')
    py_rating = request.form.get('rating')
    if (py_movie != '' and py_director != ''):
        # Adds movie to dictionary, with movie name as key
        movie_repository_singleton.create_movie(py_movie, py_director, py_rating) 
    # After creating the movie in the database, we redirect to a page that lists all the movies
    return redirect('/movies')

@app.get('/movies/search')
def search_movies():
    return render_template('search_movies.html', search_active=True)

@app.post('/movies/search')
def fetch_results():
    print("Hello?")
    py_movie = request.form.get('title')
    print(py_movie)
    py_result =  movie_repository_singleton.get_movie_by_title(py_movie)
    print(py_result)
    return render_template('search_result.html', result=py_result)
