## standard imports 
import pandas as pd 
import numpy as np
from datetime import datetime

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

### Spotify Credentials - must be set in local environment to run
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

### ------------
now = datetime.now()
tstamp = now.strftime('%Y%m%d_%H%M%S')

genre = input('Enter a genre: ')

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
genre = genre.replace(' ', '')
tracks.to_csv(f'./data/{genre}.csv', index=False)

print('We got your song sample there are ', tracks.shape[0], ' entries.')