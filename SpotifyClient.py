import requests

from .data import SpotifyWebAPIAuthorizationData
from ._endpoints import AUTHORIZATION as AUTH_ENDPOINT
from .exceptions import InvalidClientCredentialsException


class SpotifyClient:

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
