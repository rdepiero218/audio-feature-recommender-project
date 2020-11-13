## standard imports 
import pandas as pd 
import numpy as np

import datetime as dt

import spotify_fcns as sf

## visualizations
import matplotlib.pyplot as plt


from sklearn.metrics.pairwise import linear_kernel, cosine_similarity, pairwise_kernels
# clientID = 'c85f43a5a7004946996bc22659dd8de6'
# clientSecret = '9f6e5b2d26af429ba2c3a77624f85a2d'

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clientID,
#                                                            client_secret=clientSecret))


def format_data(uri, genre):
    df = pd.read_csv(f'./data/{genre}.csv')
    track = sf.get_track_audio_features(uri)
    drop_cols = ['key', 'mode', 'time_signature', 'duration_ms']
    df.drop(columns=drop_cols, inplace=True)
    track.drop(columns=drop_cols, inplace=True)  ### not present in test set using here
    return df, track


def add_track_data(df, track):
    ### Create X data
    data = pd.concat([df, track], ignore_index=True)
    ### desired features for model (may change later)
    features = ['acousticness', 'danceability', 'energy', 'speechiness', 'valence']
    X = data[features]
    return X, data

def pop_track_recommender(df, track):
    '''uses cosine similarity to recommend tracks'''
    
    ID = track['track_id'].values[0]
    ### calculate data 
    X, data = add_track_data(df, track)
    
    ### calculate similarity matrix
    similarity_matrix = cosine_similarity(X, X)
    
    ### create mapping bwtn track ids and index
    track_id_map = pd.Series(data.index, index=data['track_id'])
    ## find index of track in dataframe
    track_index = track_id_map[ID]
    
    ### find the correct column for the track in the similarity matrix
    similarity_scores = pd.Series(similarity_matrix[track_index])
    similarity_scores.sort_values(ascending=False, inplace=True)

    ### CREATE DF OF ALL SCORES
    scores_ids = data['track_id'].loc[similarity_scores.index]
    
    ### CREATE DF OF ALL SCORES
    rec_tracks_df = data[data['track_id'].isin(scores_ids.values)].copy()
    rec_tracks_df['score'] = similarity_scores
    rec_tracks_df.sort_values(by=['score', 'popularity'], ascending=False, inplace=True)

    return rec_tracks_df

def top_tracks_recommended(results, num_tracks):
    '''returns most popular songs for given number of tracks'''
    top_half = results[results['score'] >= results['score'].median()].copy()
    top_half.sort_values(by='popularity', ascending=False, inplace=True)  
    top_tracks = top_half[:num_tracks]
    return top_tracks


def make_track_URIs(track_ids):
    ### reformats track ids as track URIs
    ### need text spotify:track: in front of each ID to use in Spotify
    track_URIs = []
    for track_id in track_ids:
        uri = 'spotify:track:'+ track_id
        track_URIs.append(uri)
    return track_URIs

def create_playlist_file(track_ids, uri):
    
    ### creates text file of Spotify URIs
    # track_list = og_track_id.values.tolist() + track_ids.values.tolist()
    track_list = list(uri) + track_ids
    track_URIs = make_track_URIs(track_list)
    ### write URIs to text file
    playlist = open(fr'./playlist.txt','w')
    playlist.writelines('%s\n' % track for track in track_URIs) 
    playlist.close()
    pass

def recommender(uri, genre, num_tracks):
    df, track_df = format_data(uri, genre)

    results = pop_track_recommender(df, track_df)

    top_tracks = top_tracks_recommended(results, num_tracks)

    # create_playlist_file(top_tracks['track_id'], uri)

    return top_tracks


