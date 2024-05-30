import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

scope = "user-library-read"
SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI=os.getenv("SPOTIFY_REDIRECT_URI")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI, scope=scope))
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
  track = item['track']
  print(idx, track['artists'][0]['name'], " - ", track['name'])


# Use Authorization Code Flow
# Start by requesting authorization from the user in order to to access the spotify resources on their behalf
# Send a GET request to /authorize with the client id, response type (set to code), and redirect uri is http://127.0.0.1:5000/

#TODO: Authenticate user then redirect to here. (done)