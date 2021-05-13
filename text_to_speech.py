# Using this code we can convert text to speech
# Run python3 text_to_speech.py <"Your Text">
import sys
from gtts import gTTS

audio = 'speech.mp3'
language = 'en'

# Take the text from terminal
text_to_convert = sys.argv[1]

sp = gTTS(text=text_to_convert, lang=language, slow=False)

# Save the audio file
sp.save(audio)

