from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os
from dotenv import load_dotenv
load_dotenv()

#STUB - Create authentification informations
SPOTIPY_CLIENT_ID = os.getenv('CLIENT-ID')
SPOTIPY_CLIENT_SECRET = os.getenv('CLIENT-SECRET')
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "playlist-modify-private playlist-modify-public"
#NOTE -  Authentification
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SCOPE
))

#NOTE - For security reasons, this needs two differents playlists (you wouldn't like to have all your songs deleted, do you ?)
#STUB - ID of the playlist from where the tracks are extracted
playlist_from = "4Pl65fKobru8w00bwE36T7"
#STUB - ID of the playlist where the tracks will be sorted (make sure it's empty)
playlist_to = "2I1AAHgtb7lDm1NRnUNLQ8"

def get_all_tracks(playlist_id):
    tracks = []
    offset = 0
    while True:
        fetch = sp.playlist_items(
            playlist_id,
            offset=offset,
            limit=100 #NOTE - There is a limit of 100 tracks by fetch 
        )
        tracks.extend(fetch['items'])
        if len(fetch['items']) < 100: 
            break
        offset += 100
    return tracks

def get_artists(playlist):
    artists = set()
    for item in playlist:
        artists.add(item["track"]['artists'][0]['name'])
    return list(artists)

def insert_tracks(playlist_dict):
    for item in playlist:
        track = item["track"]
        track_info = (track["name"], track["id"])
        artist = track['artists'][0]['name']
        album = track['album']["name"]
        
        if album not in playlist_dict[artist]:
            playlist_dict[artist][album] = [track_info]
            playlist_dict[artist] = dict(sorted(playlist_dict[artist].items(), key=lambda x: x.lower()))
        else:
            playlist_dict[artist][album].append(track_info)
            playlist_dict[artist][album].sort()
        playlist_dict =  dict(sorted(playlist_dict.items(), key=lambda x: x.lower()))

def get_ids(playlist_dict):
    tracks_ids = list() 
    for artist_albums in playlist_dict.values():
        for tracks in artist_albums.values():
            for track in tracks:
                tracks_ids.append(track[1])
    
playlist = get_all_tracks(playlist_from) #NOTE - Contains unsorted tracks

playlist_dict : dict = dict()
#NOTE - Will contain sorted tracks under this form :
'''
{
    "artist1":{
        "album1":[
            (track1, id1),
            (track2, id2)
        ],
        "album2":[
            (track3, id3),
        ]
    },
    "artist2":{
        "album3":[
            (track5, id5),
            (track6, id6),
        ]
    }
}
'''

for artist in get_artists(playlist):
    playlist_dict[artist] = dict()

insert_tracks(playlist_dict)

for track_id in get_ids(playlist_dict):
    sp.playlist_add_items(playlist_to, [track_id])