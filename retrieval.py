from secrets import *
from uris import *
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Authentication to use API
authManager = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE, username = 'wbuisson')
sp = spotipy.Spotify(auth_manager=authManager)

liked_tracks = sp.tracks(liked_uris)['tracks']
for track in liked_tracks:
    print(track["name"])

feature_list = sp.audio_features(liked_uris)
df = pd.DataFrame(feature_list)
