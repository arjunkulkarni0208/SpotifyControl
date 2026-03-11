import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from control import play_uri  # Importing your function

# This dictionary maps the Tag ID (Physical) to the Spotify URI (Digital)
# Tip: Run the 'read' script once to find your Tag IDs
tag_registry = {
    108234567890: "spotify:album:1ATL5uq9zdQC9pYm9WOfid", # Example: Discovery - Daft Punk
    509876543210: "spotify:playlist:37i9dQZF1DXcBWndjB06l1", # Example: Coffee Table Jazz
}

reader = SimpleMFRC522()

print("--- RFID Jukebox Active ---")

try:
    last_tag = None # To prevent the same tag from re-triggering constantly

    while True:
        print("\nWaiting for tag...")
        tag_id, _ = reader.read()

        if tag_id == last_tag:
            # Skip if the tag is still resting on the reader
            time.sleep(1)
            continue

        print(f"Tag Detected: {tag_id}")

        if tag_id in tag_registry:
            uri = tag_registry[tag_id]
            play_uri(uri) # Calling your Spotify code
            last_tag = tag_id
        else:
            print(f"Unknown Tag! ID: {tag_id}. Add this to your registry.")
            last_tag = tag_id

        time.sleep(2) # Cooldown

except KeyboardInterrupt:
    print("\nShutting down...")
finally:
    GPIO.cleanup()