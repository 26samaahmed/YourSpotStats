import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import plotext

load_dotenv()

scope = "user-top-read"
SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI=os.getenv("SPOTIFY_REDIRECT_URI")


spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI, scope=scope))

print("\n*  ੈ✩‧₊˚*  ੈ✩‧₊˚*  ੈ✩ Welcome to YourSpotStats ‧₊˚*  ੈ✩‧₊˚*  ੈ✩‧₊˚*\n")

# Top Tracks this month
range = "short_term"
tracks = spotify.current_user_top_tracks(time_range=range, limit=10)
tempos = []
trackNames = []
valences = []
#print("+--------------------------------------------------------------------+")
for i, track in enumerate(tracks['items']):

  # Convert from ms to min and secs
  m_sec = track['duration_ms']
  total_sec = m_sec / 1000
  min = int(total_sec // 60)
  sec = int(total_sec % 60)
  
  #TODO: If i have a number like 4, make it 04 so it looks like 3:04 instead of 3:4

  print('|', track['name'], "by", track['artists'][0]['name'])
  #print('|', 'Duration', min, ':', sec)
  #print('|', 'Tempo: ', spotify.audio_features(track['uri'])[0]['tempo'])
  trackNames.append(track['name'])
  tempos.append(spotify.audio_features(track['uri'])[0]['tempo'])
  #print('|', 'Valence: ', spotify.audio_features(track['uri'])[0]['valence'])
  valences.append(spotify.audio_features(track['uri'])[0]['valence'])
  #print('|', "----------------------------------------------------------------------\n")

print('\n\n')
plotext.bar(trackNames, tempos, orientation="horizontal")
plotext.title('Tempo Visualization (Bar Chart)')
plotext.show()


print('\n\n')
plotext.hist(valences)
plotext.title('Valence Visualization (Histogram)')
plotext.show()
