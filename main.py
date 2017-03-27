# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from src.spotify_api import _search


app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/', defaults = {'track_response':"", 'album_response':""})
def index(track_response, album_response):
    return render_template('index.html', track_response=track_response, album_response=album_response)

@app.route('/search/', methods=['POST'])
def search():

    response = _search(request.form)

    track_response = ""
    album_response = ""


    track_html_template = '''
    <tr>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s:%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
    </tr>
    '''

    album_html_template = '''
    <tr>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s:%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
    </tr>
    '''
    for i in range(0, len(response["playlist"])):
        track_response += track_html_template%(
            response["playlist"][i]["track_name"],
            response["playlist"][i]["artists"],
            response["playlist"][i]["album_name"],
            divmod(response["playlist"][i]["duration_s"], 60)[0],
            divmod(response["playlist"][i]["duration_s"], 60)[1],
            i+1
        )

    for i in range(0, len(response["track"])):
        track_response += track_html_template%(
            response["track"][i]["track_name"],
            response["track"][i]["artists"],
            response["track"][i]["album_name"],
            divmod(response["track"][i]["duration_s"], 60)[0],
            divmod(response["track"][i]["duration_s"], 60)[1],
            i+1
        )

    for i in range(0, len(response["album"])):
        album_response += album_html_template%(
            response["album"][i]["album_name"],
            response["album"][i]["artists"],
            divmod(response["album"][i]["duration_s"], 60)[0],
            divmod(response["album"][i]["duration_s"], 60)[1],
            i+1
        )

    return render_template('index.html', track_response=track_response, album_response=album_response)
    
    

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
