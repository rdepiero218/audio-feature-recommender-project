# Daltonify: An Audio Feature Based Recommender System

A content based recommender system that recommends music based on Spotify's audio features.

---
### Motivation


Spotify examines contents of user playlists. It uses this information to recommend songs or artists to users based on how many other users have also associated those artists or songs together. This gives a serious advantage to already popular artists. What about new or local artists, especially those releasing new music?

Independent and local artists need a way to increase new streams when a new single or album has been released. One way to do this is by exploiting Spotify's algorithm which recommends new artists and songs to users. One way to do this is through playlist creation. 

By a creating a playlist which includes their track(s) along with tracks by more popular artists in their genre, get people to listen to them, and increase the likelihood that they will be recommended to users also listening to those popular artists.

### Project Goals 

* Construct a content based recommender that uses Spotify's audio features to recommend similar sounding tracks from a chosen genre.

* Create a basic web application which artists can use to generate these playlists using Spotify's API.

### Data

Spotify provides a lot of infomormation on individual tracks and albums like artwork, popularity rating, and various audio features. Data for tracks, artists and albums comes directly from the Spotify API accessed with the Spoitpy Python library.  

### The Model

The model takes in a track (via it's Spotify URI or ID) and genre from the user.
Then using a sample of 2000 tracks pulled from Spotify, the recommender uses cosine similarity to score the given track against the sample of 2000 tracks. These tracks are then ranked so that the tracks with highest popularity and highest similarity score get returned to the user.

### Results

There is an web app that implements the project using Streamlit. 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://daltonify-playlist-creator.herokuapp.com/)

### Future Work
* Deploy full web app version using React.
* Incorporate user authorization to generate playlists and import directly into Spotify
* Add album and track analysis tools.
* Test other scoring methods.
* Build more complex recommender by trying packages like Surprise.
