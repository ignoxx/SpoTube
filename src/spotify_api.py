# -*- coding: utf-8 -*-
import spotipy

SP = spotipy.Spotify()
SP.trace = False

def _search(_input):
    if len(_input) > 0:
        _return = {"track": [], "album": [], "playlist": []}
        
        # grab track data
        track_results = SP.search(q = "track:" + _input, type = "track", limit=10)
        for i in range(0, len(track_results['tracks']['items'])):
            _return["track"].append(
                {
                    "id":           track_results['tracks']['items'][i]['id'],
                    "duration_s":   track_results['tracks']['items'][i]['duration_ms']/1000,
                    "cover_url":    track_results['tracks']['items'][i]['album']['images'][0]['url'],
                    "track_url":    track_results['tracks']['items'][i]['external_urls'],
                    "track_name":   track_results['tracks']['items'][i]['name'],
                    "artists":      track_results['tracks']['items'][i]['artists'][0]['name']
                }
            )


        # grab album data
        album_results = SP.search(q = "album:" + _input, type = "album", limit=10)

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
            

            _return["album"].append(
                {
                    "album_name":       album_results['albums']['items'][i]['name'],
                    "artists":          album_results['albums']['items'][i]['artists'][0]['name'],
                    "cover_url":        album_results['albums']['items'][i]['images'][0]['url'],
                    "duration_s":       album_duration,
                    "album_tracks":     tracks
                }
            )
        
        return _return