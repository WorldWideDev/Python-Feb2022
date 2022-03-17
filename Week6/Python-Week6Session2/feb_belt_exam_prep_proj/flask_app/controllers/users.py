from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User


from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)  

@app.route("/")
def log_and_reg():
    return render_template("log_and_reg.html")

@app.route("/users/register", methods=["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect("/")
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    register_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id = User.register_user(register_data)
    session['user_id'] = user_id
    return redirect("/dashboard")

@app.route("/users/login", methods=["POST"])
def login():
    if not User.validate_login(request.form):
        flash("User does not exist")
        return redirect("/")
    user_data = {
        'email': request.form['email']
    }
    user = User.get_user_by_email(user_data)
    if user:
        if not bcrypt.check_password_hash(user.password, request.form['password']):
            flash("Email/Password combination is incorrect")
            return redirect("/")
    
        session['user_id'] = user.id
        flash("Login was successful")
        return redirect("/dashboard")
    return redirect("/")
    

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

