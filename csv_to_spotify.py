import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ==== Your Spotify API credentials ====
CLIENT_ID = 'your_spotify_client_id'
CLIENT_SECRET = 'your_spotify_client_secret'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'
# ======================================

# === Update this to your actual CSV file path ===
CSV_PATH = '/path/to/your/liked_songs.csv'
PLAYLIST_NAME = 'CSV Imported Playlist'
# ================================================

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope='playlist-modify-public'
))

# Load CSV
df = pd.read_csv(CSV_PATH)
if 'Track URI' not in df.columns:
    raise ValueError("CSV must contain a 'Track URI' column")

# Create a new playlist
user_id = sp.me()['id']
playlist = sp.user_playlist_create(user=user_id, name=PLAYLIST_NAME, public=True)
playlist_id = playlist['id']

# Collect Spotify track URIs directly from the CSV
track_uris = df['Track URI'].dropna().tolist()

# Add tracks to the playlist (max 100 per request)
for i in range(0, len(track_uris), 100):
    sp.playlist_add_items(playlist_id, track_uris[i:i+100])

print(f"✅ Playlist '{PLAYLIST_NAME}' created with {len(track_uris)} tracks.")