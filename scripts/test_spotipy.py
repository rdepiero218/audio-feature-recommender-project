import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

clientID = 'c85f43a5a7004946996bc22659dd8de6'
clientSecret = '9f6e5b2d26af429ba2c3a77624f85a2d'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clientID,
                                                           client_secret=clientSecret))

results = sp.search(q='weezer', limit=20)

for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'], track['album'])