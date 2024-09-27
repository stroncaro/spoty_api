import requests

from .data import SpotifyWebAPIAuthorizationData
from ._endpoints import AUTHORIZATION as AUTH_ENDPOINT
from .exceptions import InvalidClientCredentialsException


class SpotifyClient:
    """
    Client for authenticating with the Spotify Web API and making authorized queries to various endpoints.

    This client handles the OAuth 2.0 Client Credentials Flow to authenticate the app with Spotify and
    obtain an access token, which is required to make requests to the Spotify Web API.

    Attributes:
        client_id (str): The Spotify client ID provided for the app.
        client_secret (str): The Spotify client secret associated with the app.
        auth_data (SpotifyWebAPIAuthorizationData): Stores the authorization data, including access token, token type, and expiration time.

    Methods:
        __init__(client_id, client_secret):
            Initializes the client with the provided credentials and requests an access token.
        _request_access_token():
            Handles the token request using the Client Credentials Flow and raises an error if authentication fails.
    """

    client_id: str
    client_secret: str
    auth_data: SpotifyWebAPIAuthorizationData

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self._request_access_token()

    def _request_access_token(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        auth_response = requests.post(
            AUTH_ENDPOINT,
            headers=headers,
            data=data,
        )

        if not auth_response.status_code == 200:
            raise InvalidClientCredentialsException(
                f"Server response: {auth_response.json()}"
            )

        self.auth_data = SpotifyWebAPIAuthorizationData(data=auth_response.json())

    # Albums
    def get_album(self):
        raise NotImplementedError

    def get_several_albums(self):
        raise NotImplementedError

    def get_album_tracks(self):
        raise NotImplementedError

    def get_user_saved_albums(self):
        raise NotImplementedError

    def remove_user_saved_albums(self):
        raise NotImplementedError

    def check_user_saved_albums(self):
        raise NotImplementedError

    def get_new_releases(self):
        raise NotImplementedError

    # Artists
    def get_artist(self):
        raise NotImplementedError

    def get_several_artists(self):
        raise NotImplementedError

    def get_artist_albums(self):
        raise NotImplementedError

    def get_artist_top_tracks(self):
        raise NotImplementedError

    def get_artist_related_artists(self):
        raise NotImplementedError

    # Genres
    def get_available_genre_seeds(self):
        raise NotImplementedError

    # Markets
    def get_available_markets(self):
        raise NotImplementedError

    # Search
    def search(self):
        raise NotImplementedError

    # Tracks
    def get_track(self):
        raise NotImplementedError

    def get_several_tracks(self):
        raise NotImplementedError

    def get_user_saved_tracks(self):
        raise NotImplementedError

    def save_tracks_for_current_user(self):
        raise NotImplementedError

    def remove_user_saved_tracks(self):
        raise NotImplementedError

    def check_user_saved_tracks(self):
        raise NotImplementedError

    def get_several_tracks_audio_features(self):
        raise NotImplementedError

    def get_track_audio_features(self):
        raise NotImplementedError

    def get_track_audio_analysis(self):
        raise NotImplementedError

    def get_recommendations(self):
        raise NotImplementedError

    # Users
    def get_current_user_profile(self):
        raise NotImplementedError

    def get_user_top_items(self):
        raise NotImplementedError

    def get_user_profile(self):
        raise NotImplementedError

    def follow_playlist(self):
        raise NotImplementedError

    def unfollow_playlist(self):
        raise NotImplementedError

    def get_followed_artists(self):
        raise NotImplementedError

    def follow_artists_or_users(self):
        raise NotImplementedError

    def unfollow_artists_or_users(self):
        raise NotImplementedError

    def check_if_user_follows_artists_or_users(self):
        raise NotImplementedError

    def check_if_current_user_follows_playlist(self):
        raise NotImplementedError
