import pandas as pd 
import numpy as np

import datetime as dt


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

### Spotify Credentials - must be set in local environment to run
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_tracks(genre):
    limit = 50
    max_requests = 2000
    ### TESTING VALUES
    # limit = 5# 50
    # max_requests = 20 ## 2000

    track_df = []
    for n in range(0, max_requests, limit):
        search_results = sp.search(q=f'genre: "{genre}"', type='track', limit=limit, offset = n, market='US')['tracks']['items']

        track_list = []
        
        for i in range(len(search_results)):
            track_info = [
                search_results[i].get('name'), 
                search_results[i].get('artists')[0]['name'], 
                search_results[i].get('album')['name'],
                search_results[i].get('id'),
                search_results[i].get('popularity'),
                ]
            track_list.append(track_info)

        ## create dataframe of track info
        track_list_df = pd.DataFrame(track_list, columns=['track_name', 'artist', 'album', 'track_id', 'popularity'])
        ## get audio features for tracks
        track_audio_features = pd.DataFrame.from_dict(sp.audio_features(tracks=track_list_df['track_id'].values.tolist()))
        drop_cols = ['type', 'id', 'uri', 'track_href', 'analysis_url']
        track_audio_features.drop(columns = drop_cols, inplace=True)
        ## concat both dataframs
        track_list_df = pd.concat([track_list_df, track_audio_features], axis=1)
        track_df.append(track_list_df)

    tracks = pd.concat(track_df, ignore_index=True)
    tracks['popularity'] = np.round(tracks['popularity']/100, 2)
    # tracks.to_csv(f'../data/{genre}-{tstamp}.csv', index=False)
    # genre = genre.replace(' ', '')
    
    ## duh, don't actually need to save csv here!
    # tracks.to_csv(f'./data/{genre}.csv', index=False)
    # print('Genre: ', genre, '' tracks.shape[0], ' entries.')
    print('We got ', tracks.shape[0], 'tracks from the ', genre, 'genre.')
    # pass
    return tracks



def make_track_URIs(track_ids):
    ### reformats track ids as track URIs
    ### need text spotify:track: in front of each ID to use in Spotify
    track_URIs = []
    for track_id in track_ids:
        uri = 'spotify:track:'+ track_id
        track_URIs.append(uri)
    return track_URIs

def create_playlist_file(track_ids, og_track_id, name):
    
    ### creates text file of Spotify URIs
    # track_list = og_track_id.values.tolist() + track_ids.values.tolist()
    track_list = list(og_track_id)+ track_ids
    track_URIs = make_track_URIs(track_list)
    ### write URIs to text file
    playlist = open(fr'./playlist_{name}.txt','w')
    playlist.writelines('%s\n' % track for track in track_URIs) 
    playlist.close()
    pass

def display_playlist(playlist_tracks):
    ### displays playlist track name, artist, album
    tracks_dict = sp.tracks(playlist_tracks)['tracks']
    playlist_info = []
    for i in range(len(playlist_tracks)):
        track = [
            tracks_dict[i]['name'], 
            tracks_dict[i]['artists'][0]['name'],
            tracks_dict[i]['album']['name']
            ]
        playlist_info.append(track)
    
    playlist_df = pd.DataFrame(playlist_info, columns=['Title', 'Artist', 'Album'] )
    ### start index at 1
    playlist_df.index = np.arange(1,len(playlist_df)+1)
    return playlist_df


col_names_dict = {
       'track_name': 'Track Name', 
       'track_number': 'Track', 
       'track_uri' : 'URI', 
       'popularity': 'Popularity', 
       'danceability': 'Danceability',
       'energy' : 'Energy', 
       'key': 'Key', 
       'loudness': 'Loudness', 
       'mode': 'Mode', 
       'speechiness': 'Speechiness', 
       'acousticness': 'Acousticness',
       'instrumentalness': 'Instrumentalness', 
       'liveness': 'Liveness', 
       'valence': 'Valence', 
       'tempo': 'Tempo', 
       'duration_ms': 'Duration',
       'time_signature' : 'Time Signature'
    }

###---------------------
def album_audio_features(ID):
    album_tracks_list = sp.album_tracks(ID, market='US')['items']
    
    album_tracks_URI = [album_tracks_list[i].get('uri') for i in range(len(album_tracks_list))]

    track_list = []
    
    raw_track_list = sp.tracks(album_tracks_URI, market='US')['tracks']
    
    track_list = []
    
    for i in range(len(raw_track_list)):
        track_info = [raw_track_list[i].get('name'), raw_track_list[i].get('track_number'), raw_track_list[i].get('uri'), raw_track_list[i].get('popularity')]
        track_list.append(track_info)

    track_info_df = pd.DataFrame(track_list, columns=['track_name', 'track_number', 'track_uri', 'popularity'])

    track_audio_features = sp.audio_features(tracks=track_info_df['track_uri'].values.tolist())

    audio_features_df = pd.DataFrame.from_dict(track_audio_features)

    drop_cols = ['type', 'id', 'uri', 'track_href', 'analysis_url']

    audio_features_df.drop(columns = drop_cols, inplace=True)

    album_df = pd.concat([track_info_df, audio_features_df], axis=1)
    
    return album_df

def get_album_info(ID):
    album = sp.album(ID)
    album_info = {
        'name' : album['name'],
        'artist' : album['artists'][0]['name'],
        'artwork_url': album['images'][1]['url'], ## 300 W 64 H
        'popularity' : album['popularity'],
        'release_date': dt.datetime.strptime(album['release_date'],'%Y-%m-%d').strftime('%B %d, %Y'),
    }
    return album_info

def get_track_info(uri):
    track = sp.track(uri)
    track_info = {
        'track_name' : track['name'],
        'artist' : track['artists'][0]['name'],
        'album' : track['album']['name'],
        'artwork_url': track['album']['images'][1]['url'], ## 300 W 64 H
        'release_date': dt.datetime.strptime(track['album']['release_date'],'%Y-%m-%d').strftime('%B %d, %Y'),
        'track_id' : track['id'],
        'popularity' : np.round(track['popularity']/100, 2),
    }
    # track_df = pd.DataFrame.from_dict(track_info)
    return track_info

def get_track_audio_features(track_info):
    ### Note: fcn can use ID, URI or URL from Spotify
    ### GET TRACK INFO FROM SPOTIFY
    
    track_info_list = [
        track_info['track_name'],
        track_info['artist'],
        track_info['album'],
        track_info['track_id'],
        track_info['popularity']
    ]
    
    ### GET TRACK AUDIO FEATURES FROM SPOTIFY
    track_audio_features = sp.audio_features(tracks=track_info['track_id'])
    
    audio_features_df = pd.DataFrame.from_dict(track_audio_features)
    drop_cols = ['type', 'id', 'uri', 'track_href', 'analysis_url']
    audio_features_df.drop(columns = drop_cols, inplace=True)

    ### create dataframe
    track_info_df = pd.DataFrame([track_info_list], columns=['track_name','artist', 'album', 'track_id', 'popularity'])
    
    track_audio_features = pd.concat([track_info_df, audio_features_df], axis=1)
    
    return track_audio_features

def get_track_data(uri):

    track_info = get_track_info(uri)

    track_df = get_track_audio_features(track_info)

    return track_df


def plot_audio_features(df, artist_name, album_name):
    df = df.iloc[::-1]
    ### Horizontal subplots
    df.plot.barh(
        x = 'track_name',
        y = ['valence','energy', 'danceability'],
        ylim = [0,1], 
        sharey = True,
        subplots = True, 
        layout = (1,3),
        figsize = (15,5),
        legend = False, 
        # title = f'{artist_name} - {album_name}', 
        xlabel = 'Track Name')
    plt.savefig('./images/album_audio_features.png')
    pass

def convert_duration(time_ms):
    secs = int((time_ms/1000)%60)
    if secs < 10:
        secs = str('0') + str(secs)
    mins = int((time_ms/(1000*60))%60)
    mins_secs = str(mins) + ':' + str(secs)
    return mins_secs

def format_display_track(track):
    ### display track features
    track['Time'] = track['duration_ms'].apply(convert_duration)
    track_feat = track[['Time','popularity', 'danceability', 'energy', 'valence', 'speechiness', 'instrumentalness','acousticness', 'liveness', 'loudness', 'tempo']]
    track_feat = track_feat.T
    track_feat.columns = ['Feature']

    return track_feat

def format_display_tracks(df_album):
    ### display track list
    df_track_list = df_album[['track_number', 'track_name']]
    df_track_list['Time'] = df_album['duration_ms'].apply(convert_duration)
    df_track_list.set_index('track_number', inplace=True)
    df_track_list.rename(columns=col_names_dict, inplace=True, errors='ignore')
    return df_track_list

def format_display_album_data(df_album):
    display_cols = [
            'track_number', 
            'track_name', 
            'popularity', 
            'danceability',
            'energy', 
            'valence',
            'speechiness', 
            'acousticness',
            'instrumentalness']

    df_album_display = df_album[display_cols]
    df_album_display.set_index('track_number', inplace=True)

    df_album_display.rename(columns=col_names_dict, inplace=True, errors='ignore')

    return df_album_display