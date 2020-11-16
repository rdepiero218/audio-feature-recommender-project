# Daltonify: An Audio Feature Based Recommender System

Recommends music based on Spotify audio features.


### Motivation

Independent and local artists need a way to increase new streams when a new single or album has been released. One way to do this is by exploiting Spotify's algorithm which recommends new artists and songs to users.

One way to do this is through playlist creation. Spotify examines contents of user playlists. It uses this information to recommend songs or artists to users based on how many other users have also associated those artists or songs together.

By a creating a playlist which includes their track(s) along with tracks by more popular artists in their genre, get people to listen to them, and increase the likelihood that they will be recommended to users also listening to those popular artists.

<!-- I created a tool that can be used by independent artists which generates a playlist that the artist can share with existing fans which includes their music along with music from popular artists in their genre.
 -->
### Goal 
Deliver a basic tool that can be used by independent artists to promote new releases on Spotify. This ideal end product will generate a playlist that the artist can share with existing fans which includes their music along with popular artists in their genre.

My personal learning goal: Coming from a predominantly academic background I 
wanted to produce something that was more than a model and some data analysis. I would like to actually be able to produce a product of some kind that could be used by someone (even if that product is super basic and catered to a super niche need). Also, I’d really like to work for Spotify.

The desired end product was a basic website/tool in which an artist can enter in a Spotify Track URI and see a playlist (or possibly just a list) of similar sounding artists along with their tracks (where these artists are more popular than the independent artist seeking the playlist).

### Data
Data will come directly from the Spotify API. Spotify provides a lot of infomormation on individual tracks and albums like artwork, popularity rating, and various audio features. 

The goal is to pull a reasonably sized set of data in which to construct a content based recommendation system.

End product: A basic website/tool in which an artist can enter in a Spotify Track ID and see a playlist (or possibly just a list) of similar sounding artists along with their tracks (where these artists are more popular than the independent artist seeking the playlist).

There is an app that implements the project.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://daltonify-playlist-creator.herokuapp.com/)
