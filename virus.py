#!/usr/bin/env python3
from gtts import gTTS
import os

### SETTINGS
audiofile_name = 'audio.mp3'
audio_text = 'You have downloaded ransomware'
audio_folder = '.audio'
# Ways to play mp3
play_options_priority = ['vlc', 'pygame', 'webbrowser', 'mpg123']

working_directory = os.path.dirname(__file__)
mp3_path = '/'.join([working_directory, audio_folder, audiofile_name])

def create_audio(audio_text, mp3_path):
    tts = gTTS(text=audio_text, lang='en')
    tts.save(mp3_path)

def play_audio(mp3_path):
    for play_option in play_options_priority:
        print(play_option)
        try:
            if play_option == 'vlc':
                os.system('vlc --qt-start-minimized --play-and-exit {}'.format(mp3_path))
            elif play_option == 'webbrowser':
                import webbrowser
                webbrowser.open(mp3_path)
                #subprocess.run(["ls", "-l"])
            elif play_option == 'mpg123':
                os.system("mpg123 {}".format(mp3_path))
            elif play_option == 'pygame':
                raise NotImplementedError
            break
        except Exception as e:
            print('Exception: {}'.format(e))
            continue

def create_and_play(audio_text):
    create_audio(audio_text, mp3_path)
    play_audio(mp3_path)

def main():
#    create_and_play('This is a sample test to speech input.')
    files_to_encrypt = list_files(os.path.join(working_directory, 'Totally_Secret_Folder'))
#    print(next(files_to_encrypt))
    while True:
        try:
            print(next(files_to_encrypt))
        except Exception as e:
            print('Exception: {}'.format(e))
            break
#    print()

if __name__ == '__main__':
    main()
