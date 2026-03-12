from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import os
import json

reader = SimpleMFRC522()

filename = "playlists.json"

try:
    print("Hold your tag against the reader to see its ID...")
    tag_id, _ = reader.read()
    print(f"Your Tag ID is: {tag_id}")
    uri=input("Enter the Spotify URI: ")
    label=input("Enter the Name of your Album/Playlist/Song: ")
    new_data = {"uri":uri, "label":label}


    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        print("File doesn't exist")

    data[str(tag_id)] = new_data

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

finally:
    GPIO.cleanup()