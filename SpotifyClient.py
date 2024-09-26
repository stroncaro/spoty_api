import requests

from .data import SpotifyWebAPIAuthorizationData
from ._endpoints import AUTHORIZATION as AUTH_ENDPOINT


class SpotifyClient:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id: str = client_id
        self.client_secret: str = client_secret

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
            raise NotImplemented

        self.auth_data = SpotifyWebAPIAuthorizationData.from_json(auth_response.json())