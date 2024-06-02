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


range = "short_term"
tempos = []
trackNames = []
valences = []
artistName = []
duration = []

# Top Tracks this month
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
    "Duration": duration
  })
  return data

print("\n=============================== Your Top 10 Songs This Month ===============================\n\n")
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

print("\n=============================== Your Top 10 Artists This Month ===============================\n\n")
topArtists = getTopArtists()
print(topArtists)

print('\n')
plotext.simple_bar(trackNames, tempos, width=100, color='green' ,title='Tempo Visualization')
plotext.show()

print('\n')
plotext.simple_bar(trackNames, valences, width=100, color='green', title='Valence Visualization')
plotext.show()