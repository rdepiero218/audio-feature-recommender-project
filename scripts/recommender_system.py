## standard imports 
import pandas as pd 
import numpy as np

import datetime as dt

## visualizations
import matplotlib.pyplot as plt


from sklearn.metrics.pairwise import linear_kernel, cosine_similarity, pairwise_kernels

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

### Spotify Credentials - must be set in local environment to run
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


### DISPLAY FUNCTIONS


### RETRIEVAL FUNCTIONS


### MODEL FUNCTIONS