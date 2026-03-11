from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()
try:
    print("Hold your tag against the reader to see its ID...")
    tag_id, _ = reader.read()
    print(f"Your Tag ID is: {tag_id}")
finally:
    GPIO.cleanup()