import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import plotext
import pandas as pd

load_dotenv()

scope = "user-top-read"
SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI=os.getenv("SPOTIFY_REDIRECT_URI")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI, scope=scope))

print("\n*  ੈ✩‧₊˚*  ੈ✩‧₊˚*  ੈ✩ ‧₊˚*  ੈ✩‧₊˚*  ੈ✩‧₊˚* Welcome to YourSpotStats *  ੈ✩‧₊˚*  ੈ✩‧₊˚*  ੈ✩ ‧₊˚*  ੈ✩‧₊˚*  ੈ✩‧₊˚*\n")

# Top Tracks this month
range = "short_term"
tempos = []
trackNames = []
valences = []
artistName = []
duration = []

def getTopTracks():
  topTracks = spotify.current_user_top_tracks(time_range=range, limit=10)

  for track in topTracks['items']:

    # Convert from ms to min and secs
    m_sec = track['duration_ms']
    total_sec = m_sec / 1000
    min = int(total_sec // 60)
    sec = int(total_sec % 60)

    # Prints 04 instead of 4
    if sec < 10:
      sec = "0" + str(sec)
    
    artistName.append(track['artists'][0]['name'])
    duration.append(str(min) + ":" + str(sec))
    trackNames.append(track['name'])
    tempos.append(spotify.audio_features(track['uri'])[0]['tempo'])
    valences.append(spotify.audio_features(track['uri'])[0]['valence'])



  # Create Data Frame

  data = pd.DataFrame( {
    "Track": trackNames,
    "Artist": artistName,
    "Tempo": tempos,
    "Valences": valences,
    "Duration": duration
  })
  return data

#data.style.set_properties(**{'border': '1.3px solid white', 'color': 'blue'})
#data.style.set_properties(subset=['trackNames'], **{'width': '100px'})
print("\n\n=============================== Your Top 10 Songs This Month ===============================\n\n")
topTracks = getTopTracks()
print(topTracks)



# User's Top 10 Songs
def getTopArtists():
  artistList = []
  artistGenre = []
  topArtists = spotify.current_user_top_artists(time_range=range,limit=10)
  for artist in topArtists['items']:
    artistList.append(artist['name'])
    artistGenre.append(artist['genres'])

  data2 = pd.DataFrame( {
    "Artist": artistList,
    "Genre": artistGenre
  })

  return data2


print("\n\n=============================== Your Top 10 Artists This Month ===============================\n\n")
topArtists = getTopArtists()
print(topArtists)

'''
print('\n\n')
plotext.bar(trackNames, tempos, orientation="horizontal")
plotext.title('Tempo Visualization (Bar Chart)')
plotext.show()

print('\n\n')
plotext.hist(valences)
plotext.title('Valence Visualization (Histogram)')
plotext.show()
'''