#!/usr/bin/env python3
from gtts import gTTS
import os

#from requests.packages.urllib3.exceptions import InsecureRequestWarning

### SETTINGS
audiofile_name = 'audio.mp3'
audio_text = 'You have downloaded ransomware'
# Ways to play mp3
play_options = ['webbrowser', 'mpg123', 'pygame']


working_directory = os.path.dirname(__file__)
mp3_path = '/'.join([working_directory, audiofile_name])
 
tts = gTTS(text=audio_text, lang='en')
tts.save(mp3_path)

for play_option in play_options:
    try:
        if play_option == 'webbrowser':
            import webbrowser
            webbrowser.open(mp3_path)
        elif play_option == 'mpg123':
            os.system("mpg123 {}".format(mp3_path))
        elif play_option == 'pygame':
            raise NotImplementedError
            #from pygame import mixer # Load the required library
        break
    except Exception as e:
        print('Exception: {}'.format(e))
        continue