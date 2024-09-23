# main.py
from ocr import image_to_text
from text_to_speech import text_to_audio
from rpa import automate_process
import requests

# Step 1: Receive image from endpoint
image_url = 'http://example.com/image.jpg'
response = requests.get(image_url)
with open('image.jpg', 'wb') as f:
    f.write(response.content)

# Step 2: Convert image to text
text = image_to_text('image.jpg')

# Step 3: Convert text to audio
text_to_audio(text, 'audio.mp3')

# Step 4: Automate audio playback
automate_process()