import spotipy
from spotipy import SpotifyClientCredentials

cid = 'f93680415d4d48b8805a8334eb8e7e43'
secret = 'ddc2931f3c1742c9a6215804570df7e1'
auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
results= sp.search("Beyonce")
print(results)