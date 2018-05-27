import logging
from flask import Flask, render_template, request, Response
from flask_cors import CORS
import werkzeug
from . import virus
from . import totally_secret
import time
import os
import webbrowser

app = Flask(__name__)
CORS(app)

@app.route('/win')
def win():
    name = request.args.get('name', default = '')
    virus.create_and_play('Oh no, {}, you nearly fell for ransomware.'.format(name))
    totally_secret.crypt_files(encrypt_dir_path=os.path.join(os.path.dirname(__file__),
                                'Totally_Secret_Folder'))

    webbrowser.open_new_tab('http://localhost:3000/')
    return Response('Ok, but not ok', 200)

@app.route('/complete', methods=['POST'])
def submitted_form():
    totally_secret.crypt_files(encrypt_dir_path=os.path.join(os.path.dirname(__file__),
                                'Totally_Secret_Folder'))

    return Response('Toggle encryption/decryption', 200)

def main():
    virus.create_and_play('You have downloaded ramsomware')

if __name__ == '__main__':
    main()
