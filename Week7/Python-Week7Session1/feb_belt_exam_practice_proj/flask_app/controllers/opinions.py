from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.opinion import Opinion

@app.route("/dashboard")
def dashboard():
    user_data = {
        'id': session['user_id']
    }
    return render_template("dashboard.html", user=User.get_user_by_id(user_data), opinions = Opinion.get_all_with_favorites(), 
    opinions_liked_by_user=Opinion.get_all_user_favorited_opinions(user_data))

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
    #How to get the user id?
    #session['user_id']
    #how to get the user id of user who created the opinion 
    data = {
        'id': id
    }
    opinion= Opinion.get_one(data)
    if session['user_id'] != opinion.user_id:
        return redirect("/dashboard")
    return render_template("edit_opinion.html", opinion= opinion)
@app.route("/opinions/<int:id>/delete")
def delete_opinion(id):
    data = {
        'id': id
    }
    opinion= Opinion.get_one(data)
    if session['user_id'] != opinion.user_id:
        return redirect("/dashboard")
    return render_template("delete_opinion.html", opinion= opinion)
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

@app.route("/opinions/<int:id>/like")
def like_opinion(id):
    data = {
        'user_id': session['user_id'],
        'opinion_id': id
    }
    Opinion.like(data)
    return redirect("/dashboard")

@app.route("/opinions/<int:id>/dislike")
def dislike_opinion(id):
    data = {
        'user_id': session['user_id'],
        'opinion_id': id
    }
    Opinion.dislike(data)
    return redirect("/dashboard")

