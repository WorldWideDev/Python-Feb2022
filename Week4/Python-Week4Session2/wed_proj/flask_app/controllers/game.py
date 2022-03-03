from flask import render_template, request, session, redirect  # Import Flask to allow us to create our app
from flask_app import app
import random

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def new_player():
    return render_template("new_player.html")  # Return the string 'Hello World!' as a response

@app.route('/players/new', methods=["POST"])
def create_player():
    # session = {}
    session["playerName"] = request.form["playerName"]
    session["playerEmail"] = request.form["playerEmail"]
    session["playerAge"] = request.form["playerAge"]
    session['win'] = 0
    session['loss'] = 0
    session['tie'] = 0
    session['activity_log'] = []
    return redirect("/players/1")
    #return redirect("f/players/{player.id}")

@app.route('/players/<int:id>')
def show_player(id):
    return render_template("player.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/home")
def home():
    return render_template("home.html")

# 1 - win -1 - loss 0- tie
def determineWinner(player_move, opp_move):
    if player_move == opp_move:
        return 0
    if player_move=="rock":
        if(opp_move=="paper"):
            return -1
        # opp move is scissors
        else:
            return 1
    elif player_move=="paper":
        if(opp_move=="scissors"):
            return -1
        # opp move is rock
        else:
            return 1
    else:
        if(opp_move=="rock"):
            return -1
        # opp move is paper
        else:
            return 1


@app.route("/play", methods=["POST"])
def play():
    player_move = request.form["item"]
    print(player_move)
    opp_move = random.choice(["rock", "paper", "scissors"])
    print(f"Opp move was {opp_move}")
    result = determineWinner(player_move, opp_move)
    if result == 1:
        session['win'] += 1
        session['activity_log'].append(f"{session['playerName']} won the match by playing {player_move} and beating the opp's {opp_move}")
    if result == -1:
        session['loss'] += 1 
        session['activity_log'].append(f"{session['playerName']} loss the match by playing {player_move} and losing to the opp's {opp_move}")
   
    if result == 0:
        session['tie'] += 1   
        session['activity_log'].append(f"{session['playerName']} tied the match by playing {player_move}")

    return redirect("/home")

    # showForm - /
# submit new player form - /players/new
# all players - /players GET
# get a specific player - /players/1 GET
# show edit player form - /players/1/edit GET
# submit edit player form - /players/1/update POST
# show delete player form - /players/1/delete GET
# submit delete player form - /players/1/destroy POST


#RESTful routing
#Representational
#State
#Transfer