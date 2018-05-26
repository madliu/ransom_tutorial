from gtts import gTTS
import os
import requests
from pygame import mixer # Load the required library

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
tts = gTTS(text='You have downloaded ransomware', lang='en')
tts.save("audio.mp3")
cwd = os.getcwd()
os.system(cwd+"/audio.mp3")
