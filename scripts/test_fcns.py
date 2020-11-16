
### Script for testing recommender system functions

import pandas as pd
# import spotify_fcns as sf
import recommender as r

# import time

### give me a uri

uri = '4HJ7mSMtHAdU55lLjGE4zW'

# uri = '17kv7O2z3dLHW0LnXaU5Pn' 

# uri = '0SuFqlCe5i30Fr75ZlPQVT'

# genre = 'popindie'

genre = input('Enter a genre: ')

num_tracks = 15



### CALL RECOMMENDER


playlist = r.recommender(uri, genre, num_tracks)

# r.create_playlist_file(playlist['track_id'])

print(playlist)

# results = r.pop_track_reccommender(df, track)
# ## SELECT TOP NUMBER
# rec_tracks = r.top_recommended_tracks(results, 15)

# print(r.display_playlist(rec_tracks['track_id']))


# playlist_file = open('playlist.txt', 'r+')
# playlist = playlist_file.read().splitlines()

# ## create playlist
# df = rec.display_playlist(playlist)

# print(df)