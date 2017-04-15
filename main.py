# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, render_template, request, redirect, url_for
from src.spotify_api import _search,_download


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


@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/download/', methods=['POST'])
def download():
    response = _download(request.form)

    return "request.form"

@app.route('/search/', methods=['POST'])
def search():
    response = _search(request.form)

    track_response = ""
    album_response = ""

    index_html = '''
    <hr> </hr>
    <button id="btn_download" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
        Download selected tracks
    </button>

    <hr></hr> 

    <table class="mdl-data-table mdl-js-data-table mdl-data-table--selectable mdl-shadow--2dp">
        <thead>
            <tr>
            <th class="mdl-data-table__cell--non-numeric">Track</th>
            <th class="mdl-data-table__cell--non-numeric">Artist</th>
            <th class="mdl-data-table__cell--non-numeric">Album</th>
            <th class="mdl-data-table__cell--non-numeric">Length</th>
            <th class="mdl-data-table__cell--non-numeric">Number</th>
            </tr>
        </thead>
        <tbody>
            %s
        </tbody>
    </table>

    <hr></hr> 

    <table class="mdl-data-table mdl-js-data-table mdl-data-table--selectable mdl-shadow--2dp">
        <thead>
            <tr>
                <th class="mdl-data-table__cell--non-numeric">Album</th>
                <th class="mdl-data-table__cell--non-numeric">Artist</th>
                <th class="mdl-data-table__cell--non-numeric">Length</th>
                <th class="mdl-data-table__cell--non-numeric">Number</th>
            </tr>
        </thead>
        <tbody>
            %s
        </tbody>
    </table>
    '''

    track_html_template = '''
    <tr>
      <td class="mdl-data-table__cell--non-numeric" id="song">%s</td>
      <td class="mdl-data-table__cell--non-numeric" id="artist">%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s:%s min</td>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
    </tr>
    '''

    album_html_template = '''
    <tr>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
      <td class="mdl-data-table__cell--non-numeric">%s:%s min</td>
      <td class="mdl-data-table__cell--non-numeric">%s</td>
    </tr>
    '''

    for i in range(0, len(response["playlist"])):
        track_response += track_html_template % (
            response["playlist"][i]["track_name"],
            response["playlist"][i]["artists"],
            response["playlist"][i]["album_name"],
            divmod(response["playlist"][i]["duration_s"], 60)[0],
            divmod(response["playlist"][i]["duration_s"], 60)[1],
            i+1
        )
    if track_response == "":
        for i in range(0, len(response["track"])):
            track_response += track_html_template % (
                response["track"][i]["track_name"],
                response["track"][i]["artists"],
                response["track"][i]["album_name"],
                divmod(response["track"][i]["duration_s"], 60)[0],
                divmod(response["track"][i]["duration_s"], 60)[1],
                i+1
            )

        for i in range(0, len(response["album"])):
            album_response += album_html_template % (
                response["album"][i]["album_name"],
                response["album"][i]["artists"],
                divmod(response["album"][i]["duration_s"], 60)[0],
                divmod(response["album"][i]["duration_s"], 60)[1],
                i+1
            )
     
    return render_template_string(index_html%(track_response, album_response))
    
    

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
