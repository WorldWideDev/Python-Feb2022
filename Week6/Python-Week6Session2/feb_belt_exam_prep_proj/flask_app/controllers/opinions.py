from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.opinion import Opinion

@app.route("/dashboard")
def dashboard():
    user_data = {
        'id': session['user_id']
    }
    return render_template("dashboard.html", user=User.get_user_by_id(user_data), opinions = Opinion.get_all())

## Show create form - GET
@app.route("/opinions/add")
def add_opinion_form():
    return render_template("add_opinion.html")

## Process create form - POST
@app.route("/opinions/create", methods=["POST"])
def create_opinion():
    if not Opinion.validate_opinion(request.form):
        return redirect("/opinions/add")
    opinion_data = {
        'movie_title' :request.form['movie_title'],
        'experience' : request.form['experience'],
        'date_watched': request.form['date_watched'],
        'rating' : request.form['rating'],
        'user_id': session['user_id']
    }
    Opinion.create_opinion(opinion_data)
    return redirect("/dashboard")
# REMAINING GET REQUESTS
@app.route("/opinions/<int:id>")
def show_opinion(id):
    data = {
        'id': id
    }
    return render_template("show_opinion.html", opinion= Opinion.get_one(data))
@app.route("/opinions/<int:id>/edit")
def edit_opinion(id):
    
    data = {
        'id': id
    }
    return render_template("edit_opinion.html", opinion= Opinion.get_one(data))
@app.route("/opinions/<int:id>/delete")
def delete_opinion(id):
    data = {
        'id': id
    }
    return render_template("delete_opinion.html", opinion= Opinion.get_one(data))
# REMAINING POST REQUESTS
@app.route("/opinions/<int:id>/update", methods=["POST"])
def update_opinion(id):
    if not Opinion.validate_opinion(request.form):
        return redirect(f"/opinions/{id}/edit")
    Opinion.update(request.form)
    return redirect(f"/opinions/{id}/edit")
@app.route("/opinions/<int:id>/destroy", methods=["POST"])
def destroy_opinion(id):

    Opinion.destroy(request.form)
    return redirect("/dashboard")