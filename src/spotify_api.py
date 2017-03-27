# -*- coding: utf-8 -*-
#Spotify Import
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pyperclip    #TO COPY

#YouTube Import
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import codecs
import json
import sys

#There was an encoding error if exist delete '''
'''
if sys.stdout.encoding != 'cp850':
  sys.stdout = codecs.getwriter('cp850')(sys.stdout, 'strict')
if sys.stderr.encoding != 'cp850':
  sys.stderr = codecs.getwriter('cp850')(sys.stderr, 'strict')
'''

#YouTube ID and Secret
DEVELOPER_KEY = "AIzaSyBmOvFVjmpEnW3jpdPOTZHdUrik62MTt64"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

#Spotify ID and Secret
my_client_id='1516224ff93e4ffaa507140ab351632f'
my_client_secret='5d4ca6f6a09e41bdaeb38a587193dcf6'

client_credentials_manager = SpotifyClientCredentials(client_id=my_client_id,client_secret=my_client_secret)
SP = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def _search(_input):
    if len(_input['searchText']) > 0:
        videoIDS = []
        videoLink = []
        isSet = False
        createLink = 0
        _return = {"track": [], "album": [], "playlist": []}
        def generateYTLink(ids):
            for ID in ids:
                videoLink.append("https://www.youtube.com/watch?v="+ID)
        def youtube_search(options):
            youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

            # Call the search.list method to retrieve results matching the specified query term.
            search_response = youtube.search().list(
                q = options,
                part = "id,snippet",
                maxResults = 1
            ).execute()

            #filter the video ID's and save them
            for search_result in search_response.get("items", []):
                #check search_result or search_response for understanding
                #print json.dumps(search_result, indent=4)
                if search_result["id"]["kind"] == "youtube#video":
                    vid=search_result["id"]["videoId"]
                    videoIDS.append(vid)

        if "spotify" in _input['searchText']:
            if "open.spotify" or "play.spotify" in _input['searchText']:
                #https://play.spotify.com/user/spotify_germany/playlist/7zfy6XVCBYHlBxPRGYSsfI
                #https://open.spotify.com/user/1143242003/playlist/2N8fsNZRuWQOyMurU8myu2
                username = _input['searchText'].split('/')[4]
                playlist_id = _input['searchText'].split('/')[6]
                isSet = True
            else:
                #spotify:user:1143242003:playlist:1cpIoi6uRhLWbA4tlnxIok
                username = _input['searchText'].split(':')[2]
                playlist_id = _input['searchText'].split(':')[4]
                isSet = True
                

        elif "youtube" in _input['searchText']:
            if "list" in _input['searchText']:
                print "test"
            else:
                print "test"


          
        # grab playlist or track data
        if isSet == True:
            playlist_results = SP.user_playlist(username, playlist_id)
            for i in range(0, len(playlist_results['tracks']['items'])):
                _return["playlist"].append(
                    {
                        "id":           playlist_results['tracks']['items'][i]['track']['id'],
                        "duration_s":   playlist_results['tracks']['items'][i]['track']['duration_ms']/1000,
                        "cover_url":    playlist_results['tracks']['items'][i]['track']['album']['images'][0]['url'],
                        "track_url":    playlist_results['tracks']['items'][i]['track']['external_urls'],
                        "track_name":   playlist_results['tracks']['items'][i]['track']['name'],
                        "artists":      playlist_results['tracks']['items'][i]['track']['artists'][0]['name'],
                        "album_name":   playlist_results['tracks']['items'][i]['track']['album']['name']
                    }
                )
        else:
            if int(_input['sliderTracks']) > 0 and _input['checkboxTracks'] == "true":
                track_results = SP.search(q = "track:" + _input['searchText'], type = "track", limit=int(_input['sliderTracks']))
                for i in range(0, len(track_results['tracks']['items'])):
                    _return["track"].append(
                        {
                            "id":           track_results['tracks']['items'][i]['id'],
                            "duration_s":   track_results['tracks']['items'][i]['duration_ms']/1000,
                            "cover_url":    track_results['tracks']['items'][i]['album']['images'][0]['url'],
                            "track_url":    track_results['tracks']['items'][i]['external_urls'],
                            "track_name":   track_results['tracks']['items'][i]['name'],
                            "artists":      track_results['tracks']['items'][i]['artists'][0]['name'],
                            "album_name":   track_results['tracks']['items'][i]['album']['name']
                        }
                    )


        # grab album data
        if int(_input['sliderAlbum']) > 0 and _input['checkboxAlbum'] == "true":
            album_results = SP.search(q = "album:" + _input['searchText'], type = "album", limit=int(_input['sliderAlbum']))

            for i in range(0, len(album_results['albums']['items'])):
                # grab all album tracks
                tracks = dict()
                album_duration = 0
                for index, track in enumerate(SP.album_tracks(album_results['albums']['items'][i]['uri'])['items']):
                    tracks[str(index)] = {
                        'name':         track['name'],
                        'duration_s':   track['duration_ms']/1000,
                        'track_number': track['track_number'] 
                    }

                    album_duration += track['duration_ms']/1000
                

                _return["album"].append({
                        "album_name":       album_results['albums']['items'][i]['name'],
                        "artists":          album_results['albums']['items'][i]['artists'][0]['name'],
                        "cover_url":        album_results['albums']['items'][i]['images'][0]['url'],
                        "duration_s":       album_duration,
                        "album_tracks":     tracks
                    }
                )
       
        if isSet == True:
            for i in range(0,len(playlist_results['tracks']['items'])):
                youtube_search(_return["playlist"][i]['artists'] + " - " + _return["playlist"][i]['track_name'])
            generateYTLink(videoIDS)
        else:
            for i in range(0, len(track_results['tracks']['items'])):
                youtube_search(_return["track"][i]['artists'] + " - " + _return["track"][i]['track_name'])
            generateYTLink(videoIDS)

        #print json.dumps(videoLink, indent=4)
        
       
    return _return