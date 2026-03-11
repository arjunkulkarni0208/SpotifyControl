import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secrets

# 1. Setup Credentials
REDIRECT_URI = 'http://127.0.0.1:9000/callback'
scope = "user-modify-playback-state user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=secrets.CLIENT_ID,
    client_secret=secrets.CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))


def play(uri):
    devices = sp.devices()
    device_id = None

    for device in devices['devices']:
        if device['type'].lower() == 'smartphone': # Or 'tablet'
            device_id = device['id']
            print(f"Found active mobile: {device['name']}")
            break

    if device_id:
        sp.start_playback(device_id=device_id, context_uri=uri)
    else:
        print("No active mobile device found. Open Spotify on your phone first!")


if __name__ == "__main__":
    play(input("Enter uri: "))