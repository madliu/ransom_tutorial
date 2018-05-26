#!/usr/bin/env python3
from gtts import gTTS
import os
#import requests
#from pygame import mixer # Load the required library
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

working_directory = os.path.dirname(__file__)
mp3_path = '/'.join([working_directory, 'audio.mp3'])

tts = gTTS(text='You have downloaded ransomware', lang='en')
tts.save(mp3_path)
os.system("mpg123 {}".format(mp3_path))
