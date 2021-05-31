# Using this you can convert you text to hand writing text
# Run python3 text_to_handwriting.py "Your Text to write"

import sys
import pywhatkit as pywhat

# take the argument from terminal
text_to_write = sys.argv[1]

# Change the rge value to change the color of the text
pywhat.text_to_handwriting(text_to_write, rgb=[0, 0, 0]


