from flask import render_template, redirect, session, request, flash
from flask_app import app
import requests
import spotipy
from spotipy import SpotifyClientCredentials
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))


@app.route("/")
def store():
    headers = {
        'TRN-api-key': 'd717a54c-5dea-4d9a-bbec-b458d29e8ec6'
    }
    r = requests.get('https://api.fortnitetracker.com/v1/store', headers=headers)
    print(r.json())
    return render_template("store.html", items= r.json())
@app.route("/search/new")
def search_form():
    return render_template("search_form.html")


@app.route("/search", methods=["POST"])
def search():
    search_term = request.form['search_term']
    cid = 'PUT YOUR OWN CID'
    secret = 'PUT YOUR OWN SECRET'
    auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    results= sp.search(search_term, type="track", limit=50)
    print(results)
    return render_template("tracks.html", tracks= results['tracks']['items'])
@app.route("/tracks")
def tracks():
    cid = 'PUT YOUR OWN CID'
    secret = 'PUT YOUR OWN SECRET'
    auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    results= sp.search("Beyonce", type="track", limit=50)
    print(results)
    return render_template("tracks.html", tracks= results['tracks']['items'])
