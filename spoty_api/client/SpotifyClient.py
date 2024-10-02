from base64 import b64encode
from typing import Type, Self, List

import requests

from ..data import SpotifyWebAPIAuthorizationData
from .._endpoints import TOKEN, AUTHORIZE
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

    _access_token: str

    def __init__(self, *, access_token: str) -> None:
        self._access_token = access_token

    @property
    def access_token(self) -> str:
        return self._access_token

    @staticmethod
    def _request_access_token(headers, payload):
        response = requests.post(
            TOKEN,
            headers=headers,
            data=payload,
        )
        if not response.status_code == 200:
            raise InvalidClientCredentialsException(
                f"Server response: {response.json()}"
            )
        auth_data = SpotifyWebAPIAuthorizationData(data=response.json())
        return auth_data.access_token

    @staticmethod
    def _generate_client_credentials_headers():
        return {"Content-Type": "application/x-www-form-urlencoded"}

    @staticmethod
    def _generate_client_credentials_payload(client_id, client_secret):
        return {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }

    @classmethod
    def with_client_credentials(
        cls: Type[Self], *, client_id: str, client_secret: str
    ) -> Type[Self]:
        headers = cls._generate_client_credentials_headers()
        payload = cls._generate_client_credentials_payload(client_id, client_secret)
        access_token = cls._request_access_token(headers, payload)
        return SpotifyClient(access_token=access_token)

    @staticmethod
    def _generate_authorization_code_headers(client_id, client_secret):
        return {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": 
        }

    @classmethod
    def with_authorization_code(
        cls: Type[Self],
        *,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        state: str = "",
        scope: List[str] = [],
        show_dialog: bool = False,
    ):

        payload = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri,
        }

        if state:
            payload["state"] = state

        if scope:
            payload["scope"] = " ".join(scope)

        if show_dialog:
            payload["show_dialog"] = "true"

        auth_page = requests.get(
            AUTHORIZE,
            params=payload,
        )

        # TODO: Open a browser and capture the redirection after user logs in to finish log in protocol
        # Useful libraries:
        #   Playwright - https://playwright.dev/python/docs/intro
        #   Selenium - https://www.selenium.dev/documentation/webdriver/getting_started/install_library/

        print(f"Please open the following URL and log in: {auth_page.url}")
        print("When you are done, paste the URL you've been redirected to here:")
        auth_result = input()

        if not auth_result.startswith(redirect_uri):
            raise ValueError(
                f"Input does not correspond with redirect_uri:\n  {redirect_uri = }\n  {auth_result  = }"
            )

        auth_response_query = requests.utils.urlparse(auth_result).query
        auth_response_params = dict(
            q.split("=") for q in auth_response_query.split("&")
        )
        if "error" in auth_response_params:
            raise ValueError(f"Log in failed: {auth_response_params=}")
        auth_code = auth_response_params["code"]

        raise NotImplementedError
