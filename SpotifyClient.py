import requests

from .data import AuthData


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
            "https://accounts.spotify.com/api/token",
            headers=headers,
            data=data,
        )

        if not auth_response.status_code == 200:
            raise NotImplemented

        self.auth_data = AuthData(auth_response.json())
