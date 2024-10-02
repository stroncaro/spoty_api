import requests

from .._endpoints import TOKEN
from ..data import SpotifyWebAPIAuthorizationData
from ..exceptions import InvalidClientCredentialsException


def request(headers, payload):
    response = requests.post(TOKEN, headers=headers, data=payload)
    _validate_response(response)
    auth_data = SpotifyWebAPIAuthorizationData(data=response.json())
    return auth_data.access_token


def _validate_response(response: requests.Response):
    if not response.status_code == 200:
        raise InvalidClientCredentialsException(f"Server response: {response.json()}")
