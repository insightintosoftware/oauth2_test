from flask import render_template
from flask import Flask, request
import requests
import urllib
import yaml
import json

app = Flask(__name__)

with open("appsettings.yaml", 'r') as ymlfile:
    config = yaml.full_load(ymlfile)

@app.route('/')
def index():
    url = "https://accounts.google.com/o/oauth2/auth"
    params = {
        'redirect_uri': config['redirect_uri'],
        'state': config['state'],
        'client_id': config['client_id'],
        'response_type': 'code',
        'scope': config['scope']}
    return render_template('index.html', title='OAuth2', url=url, params=urllib.parse.urlencode(params))

@app.route('/callback')
def callback():
    code = request.args.get('code')

    url = "https://oauth2.googleapis.com/token"
    header_data = {
        'Content-type': 'application/x-www-form-urlencoded'}
    post_fields = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': config['redirect_uri'],
        'client_id': config['client_id'],
        'client_secret': config['client_secret']}

    resp = requests.post(url, headers=header_data, data=post_fields)
    if resp.status_code != 200:
        return resp.status_code

    parsed = resp.json()

    with open("tokens.yaml", "w", encoding='utf-8') as f:
        yaml.dump(parsed, f)

    return render_template('result.html', title='OAuth2', result=parsed)

@app.route('/getalbum')
def getalbum():
    with open("tokens.yaml", 'r') as ymlfile:
        tokens = yaml.full_load(ymlfile)

    url = "https://photoslibrary.googleapis.com/v1/albums"
    header_data = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + tokens["access_token"]}

    resp = requests.get(url, headers=header_data)
    return '<pre>'+json.dumps(json.loads(resp.text), indent=4)+'</pre>'

@app.route('/getphoto')
def getphoto():
    with open("tokens.yaml", 'r') as ymlfile:
        tokens = yaml.full_load(ymlfile)

    url = "https://photoslibrary.googleapis.com/v1/mediaItems:search"
    header_data = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + tokens["access_token"]}
    post_fields = {}

    resp = requests.post(url, headers=header_data, data=post_fields)
    print(resp.status_code)
    print(resp.text)
    content = json.loads(resp.text)
    return '<img src="' + content["mediaItems"][0]["baseUrl"] + '" />'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)