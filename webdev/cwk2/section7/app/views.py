from app import app
from flask import render_template, flash, redirect, url_for, request
from app import app, db
import os
from flask import session

import dotenv
from dotenv import load_dotenv
# import spotipy, a pythong library for the Spotify Web API
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

load_dotenv()
# get spotify credentials from the environment
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
scope = os.getenv('SPOTIFY_SCOPE')

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope= scope,
    cache_handler=cache_handler,
    show_dialog=True
)

sp = spotipy.Spotify(auth_manager=sp_oauth)

@app.route('/')
def index():
    ## homepage 
    ## explanation of the app
    ## login page 
    ## register page
    

    return render_template('home.html')

@app.route('/login')
def login():

    return "Login Page"

@app.route('/link_spotify')
def link_spotify():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    print(f"Authorization code received: {code}")
    try:
        token_info = sp_oauth.get_access_token(code)
        print(f"Token info: {token_info}")
    except spotipy.oauth2.SpotifyOauthError as e:
        print(f"Error retrieving access token: {e}")
        return f"Error: {e}"
    
    session['token_info'] = token_info
    return redirect(url_for('dashboard'))


@app.route('/register')
def register():    
    ## register page
    return "Register Page"

@app.route('/dashboard')
def dashboard():
    ## dashboard page 
    ## show cards 
    ## link to store
    ## show unopened packs
    return "Dashboard Page"

@app.route('/profile')
def profile():
    ## profile page
    ## show cards 
    return "Profile Page"

