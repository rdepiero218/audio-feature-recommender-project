
## Script for testing functions in spotify_fcns.py which use spotipy for use in Streamlit app
import pandas as pd

import spotify_fcns as sf

import time

### give me a uri

uri = '4HJ7mSMtHAdU55lLjGE4zW'

genre = 'country'

num_tracks = 15


track_info = sf.get_track_info(uri)

# track_df = sf.get_track_audio_features(track_info)



### Test getting data set in function
genre = input('Enter a genre: ')

df = sf.get_tracks(genre)

print(df.head(2))

track_df = sf.get_track_data(uri)
print(track_df)

### CALL RECOMMENDER

# playlist = r.recommender(uri, genre, num_tracks)

# print(playlist)

# results = r.pop_track_reccommender(df, track)
# ## SELECT TOP NUMBER
# rec_tracks = r.top_recommended_tracks(results, 15)

# print(r.display_playlist(rec_tracks['track_id']))


# playlist_file = open('playlist.txt', 'r+')
# playlist = playlist_file.read().splitlines()

# ## create playlist
# df = rec.display_playlist(playlist)

# print(df)