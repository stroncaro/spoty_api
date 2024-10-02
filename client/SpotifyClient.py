import requests

from ..data import SpotifyWebAPIAuthorizationData
from .._endpoints import AUTHORIZATION as AUTH_ENDPOINT
from ..exceptions import InvalidClientCredentialsException

from ._functionality import *


class SpotifyClient(
    SpotifyClientFunctionality_Albums,
    SpotifyClientFunctionality_Artists,
    SpotifyClientFunctionality_Genres,
    SpotifyClientFunctionality_Markets,
    SpotifyClientFunctionality_Search,
    SpotifyClientFunctionality_Tracks,
    SpotifyClientFunctionality_Users,
):
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
