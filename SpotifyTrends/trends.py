import spotipy
import pprint
import sys
import os
import subprocess
import spotipy
import spotipy.util as util

sp = spotipy.Spotify()
id = 121047020

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python user_playlists.py [username]")
    sys.exit()

token = util.prompt_for_user_token(username)

def topSongs(artist):
	results = sp.search(q=artist, limit=20)
	for i, t in enumerate(results['tracks']['items']):
	    print ' ', i, t['name']

def showPlaylists():
	if token:
	    sp = spotipy.Spotify(auth=token)

	    user = sp.user(username)
	    pprint.pprint(user)
	    
	    playlists = sp.user_playlists(username)
	    for playlist in playlists['items']:
	        print(playlist['name'])
	    print "hi"
	else:
	    print("Can't get token for", username)

def trackInfo():
	# shows track info for a URN or URL
	if len(sys.argv) > 1:
	    urn = sys.argv[1]
	else:
	    urn = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'

	sp = spotipy.Spotify()
	track = sp.track(urn)
	pprint.pprint(track)

def tracks():
	scope = 'user-library-read'
	token = util.prompt_for_user_token(username, scope)

	if token:
	    sp = spotipy.Spotify(auth=token)
	    results = sp.current_user_saved_tracks()
	    for item in results['items']:
	        track = item['track']
	        print(track['name'] + ' - ' + track['artists'][0]['name'])
	else:
	    print("Can't get token for", username)

#showPlaylists()
#topSongs("britney spears")
#trackInfo()
tracks()