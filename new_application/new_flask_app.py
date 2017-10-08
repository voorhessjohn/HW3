from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)
app.debug = True 



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/NewBandNameICallIt')
def show_form():
    return render_template("new_band_name_form.html")


@app.route('/newBandNameResult')
# I have changed this function to search only for 'musicArtist' as the entity since this
# is intended to check whether a band name has already been used.
def resultTunes():
    if request.method == 'GET':
        result = request.args
        params = {}
        params['term'] = result.get('artist')
        params['entity'] = 'musicArtist'
        resp = requests.get('https://itunes.apple.com/search?', params = params)
        data = json.loads(resp.text)
    return render_template('band_name_result.html', results = data['results'])