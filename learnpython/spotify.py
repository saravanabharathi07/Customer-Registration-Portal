# spotify_search.py
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

if not client_id or not client_secret:
    raise SystemExit("Set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET in your environment")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)


sp = spotipy.Spotify(auth_manager=auth_manager)

query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "ar rahman"

results = sp.search(q=query, type="track", limit=10)

for track in results["tracks"]["items"]:
    print(track["name"], "-", track["artists"][0]["name"])
