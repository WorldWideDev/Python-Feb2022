import spotipy
from spotipy import SpotifyClientCredentials

cid = 'PUT YOUR OWN CID'
secret = 'PUT YOUR OWN SECRET'
auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
results= sp.search("Beyonce")
print(results)