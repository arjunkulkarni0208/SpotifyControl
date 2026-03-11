import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secrets # Your file with CLIENT_ID and CLIENT_SECRET

# 1. Setup Credentials
REDIRECT_URI = 'http://127.0.0.1:9000/callback'
scope = "user-modify-playback-state user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=secrets.CLIENT_ID,
    client_secret=secrets.CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))

def get_active_device():
    devices = sp.devices()
    for device in devices['devices']:
        # Priority: Smartphone, then Tablet, then Computer
        if device['type'].lower() in ['smartphone', 'tablet', 'computer']:
            return device['id'], device['name']
    return None, None

def play_uri(uri):
    device_id, device_name = get_active_device()

    if device_id:
        print(f"Playing on: {device_name}")
        # Logic to handle both single tracks and albums/playlists
        if "track" in uri:
            sp.start_playback(device_id=device_id, uris=[uri])
        else:
            sp.start_playback(device_id=device_id, context_uri=uri)
    else:
        print("No active Spotify device found!")

# if __name__ == "__main__":
#     play_uri("spotify:playlist:6VcmfbREyNjp0eMNQMTb7")