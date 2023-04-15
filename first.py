from flask import Flask, request, render_template
from github import Github
import requests, helpers 



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']

    url = text

    components
    url = url + '/tree/main/src/components'
    
    g = Github(helpers.get_from_env('GH_TOKEN'))
    print(helpers.get_from_env('GH_TOKEN'))

    repo = g.get_user().get_repo( url )
    print (repo.get_dir_contents(""))
    page = requests.get(url)


    print (page.text)
    processed_text = 'meow'

    





    return processed_text