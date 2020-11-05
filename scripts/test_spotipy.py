import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

### Spotify Credentials - must be set in local environment to run
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.search(q='weezer', limit=20)

for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'], track['album'])