from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.movie import Movie
from flask_app.models.director import Director

@app.route("/movies")
def movies():
    movies = Movie.get_all()
    directors = Director.get_all()
    return render_template("movies.html", movies = movies, directors=directors)

@app.route("/movies/create", methods=["POST"])
def create_movie():
    Movie.create(request.form)
    return redirect("/movies")