# csv-to-spotify-playlist

Easily import songs from a CSV file into a new Spotify playlist using the Spotify Web API.

## Features
- Reads a CSV file with a column of Spotify Track URIs
- Creates a new playlist in your Spotify account
- Adds all tracks from the CSV to the playlist

---

## Prerequisites
- Python 3.7+
- A Spotify account
- A Spotify Developer App (for Client ID/Secret)

---

## 1. Clone the Repository

```bash
cd ~
git clone https://github.com/broknhrt2562/csv-to-spotify-playlist.git
cd csv-to-spotify-playlist
```

Cloning into 'csv-to-spotify-playlist'...
remote: Enumerating objects: 3, done.
...
Receiving objects: 100% (3/3), done.

---

## 2. Set Up Your Spotify Developer App

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
2. Log in and create a new app.
3. Note your **Client ID** and **Client Secret**.
4. In your app settings, add this Redirect URI:
   ```
   http://127.0.0.1:8888/callback
   ```
5. Save the settings.

---

## 3. Prepare Your CSV File

- Your CSV must have a column named `Track URI` with Spotify track URIs.
- Example:

  | Track URI                              | Track Name                | Album Name                  |
  |----------------------------------------|---------------------------|-----------------------------|
  | spotify:track:5n1FBtJgcDePfo8q6hBQPu   | Gaallo Thelinattunde      | Jalsa                       |
  | spotify:track:5J2CHimS7dWYMI...        | A Hard Day's Night        | A Hard Day's Night (Rem...) |

- Place your CSV file somewhere accessible, e.g., `~/Desktop/liked_songs.csv`.

---

## 4. Install Dependencies

It's best to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 5. Configure the Script

Edit `csv_to_spotify.py` and fill in:

```python
CLIENT_ID = 'your_spotify_client_id'
CLIENT_SECRET = 'your_spotify_client_secret'
CSV_PATH = '/path/to/your/liked_songs.csv'
PLAYLIST_NAME = 'Your Playlist Name'
```

---

## 6. Run the Script

```bash
python csv_to_spotify.py
```

- A browser window will open for you to log in and authorize the app.
- After authorization, your playlist will be created and filled with tracks from your CSV!

---

## Troubleshooting

- **INVALID_CLIENT: Invalid redirect URI**  
  Make sure the redirect URI in your script matches exactly what you set in the Spotify Developer Dashboard.
- **ModuleNotFoundError**  
  Make sure you installed dependencies in the correct environment.

---

## License

MIT

---

## Credits
- [Spotipy](https://spotipy.readthedocs.io/)
- [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) 
```

</rewritten_file>