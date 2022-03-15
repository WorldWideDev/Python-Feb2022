from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.director import Director

@app.route("/directors")
def directors():
    directors = Director.get_all()
    return render_template("directors.html", directors = directors)

@app.route("/directors/<int:id>")
def director(id):
    data = {
        'id': id
    }
    director = Director.get_one(data)
    return render_template("director.html", director=director)

@app.route("/directors/create", methods=["POST"])
def create_director():
    Director.create(request.form)
    return redirect("/directors")

# @app.route("/directors/<int:id>/delete")