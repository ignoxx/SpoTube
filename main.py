# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from src.spotify_api.py import _search


app = Flask(__name__)

@app.route('/', defaults = {'response':""})
def index(response):
    return render_template('index.html', response=response)

@app.route('/search/', methods=['POST'])
def search():
    response = _search(request.form["searchText"])

    html_template ='''
    <tr>
        <td class="mdl-data-table__cell--non-numeric">
            <div class="demo-card-square mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title mdl-card--expand">
                    <h2 class="mdl-card__title-text">title</h2>
                </div>
                <div class="mdl-card__supporting-text">
                    Hellu
                </div>
                <div class="mdl-card__actions mdl-card--border">
                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Open
                    </a>

                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Preview
                    </a>

                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Download
                    </a>
                </div>
            </div>
        </td>

        <td class="mdl-data-table__cell--non-numeric">
            <div class="demo-card-square mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title mdl-card--expand">
                    <h2 class="mdl-card__title-text">title</h2>
                </div>
                <div class="mdl-card__supporting-text">
                    Hellu
                </div>
                <div class="mdl-card__actions mdl-card--border">
                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Open
                    </a>

                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Preview
                    </a>

                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Download
                    </a>
                </div>
            </div>
        </td>

        <td class="mdl-data-table__cell--non-numeric">
            <div class="demo-card-square mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title mdl-card--expand">
                    <h2 class="mdl-card__title-text">title</h2>
                </div>
                <div class="mdl-card__supporting-text">
                    Hellu
                </div>
                <div class="mdl-card__actions mdl-card--border">
                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Open
                    </a>

                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Preview
                    </a>

                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Download
                    </a>
                </div>
            </div>
        </td>
    </tr>
    '''

    '''
    search = "---- Tracks ---- <br>"
    for i in range(0, len(respones["track"])):
        search += "<img src=%s width='64' height='64' /><strong> %s - %s | Duration: %s:%s min. </strong> <br>"%(
            respones["track"][i]["cover_url"],
            respones["track"][i]["artists"], 
            respones["track"][i]["track_name"],
            divmod(respones["track"][i]["duration_s"], 60)[0],
            divmod(respones["track"][i]["duration_s"], 60)[1]
        )
    search += "<br>---- Albums ----<br><br>"


    for i in range(0, len(respones["album"])):
        search += "<img src=%s width='64' height='64' /><strong> %s - %s | Duration: %s:%s min. </strong> <br>"%(
            respones["album"][i]["cover_url"],
            respones["album"][i]["artists"], 
            respones["album"][i]["album_name"],
            divmod(respones["album"][i]["duration_s"], 60)[0],
            divmod(respones["album"][i]["duration_s"], 60)[1]
        )
    '''

    search = html_template
    return render_template('index.html', response=search)
    
    

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
