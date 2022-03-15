from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.director import Director

@app.route("/")
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
    #Validation passes, create director
    if Director.validate_director(request.form):
        Director.create(request.form)
    
    #If input fails validation no-op, redirect back to /directors with flash messaging
    return redirect("/directors")

#show the edit form
@app.route("/directors/<int:id>/edit")
def edit_director_form(id):
    data = {
        'id': id
    }
    director = Director.get_one(data)
    return render_template("edit_director.html", director=director)

#perform the update
@app.route("/directors/<int:id>/update", methods=['POST'])
def update_director(id):
    Director.edit(request.form)
    return redirect(f"/directors/{id}")

@app.route("/directors/<int:id>/delete")
def delete_director_form(id):
    data = {
        'id': id
    }
    director = Director.get_one(data)
    return render_template("delete_director.html", director=director)

@app.route("/directors/<int:id>/destroy", methods=["POST"])
def delete_director(id):
    Director.delete(request.form)
    return redirect("/directors")
