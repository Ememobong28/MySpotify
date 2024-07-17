import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'f366ebe272bb47c09e56c719b08ca406'
client_secret = 'dfecd956c85d400d90c1c60001df69c4'
redirect_uri = 'http://localhost:8888/callback'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

track_id = '3n3Ppam7vgaVa1iaRUc9Lp'
track = sp.track(track_id)
print(track)  
