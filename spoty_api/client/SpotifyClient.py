from typing import Type, Self, List

from .._utils import access_token as AccessTokenUtils
from .._utils import client_credentials as ClientCredentialUtils
from .._utils import authorization_code as AuthorizationCodeUtils
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

    @classmethod
    def with_client_credentials(
        cls: Type[Self], *, client_id: str, client_secret: str
    ) -> Type[Self]:
        headers = ClientCredentialUtils.generate_headers()
        payload = ClientCredentialUtils.generate_payload(client_id, client_secret)
        access_token = AccessTokenUtils.request(headers, payload)
        return SpotifyClient(access_token=access_token)

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

        authorization_url = AuthorizationCodeUtils.generate_authorization_url(
            client_id, redirect_uri, state, scope, show_dialog
        )

        # TODO: Open a browser and capture the redirection after user logs in to finish log in protocol
        # Useful libraries:
        #   Playwright - https://playwright.dev/python/docs/intro
        #   Selenium - https://www.selenium.dev/documentation/webdriver/getting_started/install_library/

        print(f"Please open the following URL and log in: {authorization_url}")
        print("When you are done, paste the URL you've been redirected to here:")
        auth_redirect = input()
        code = AuthorizationCodeUtils.get_code_from_auth_redirect(
            auth_redirect, redirect_uri
        )
        headers = AuthorizationCodeUtils.generate_headers(client_id, client_secret)
        payload = AuthorizationCodeUtils.generate_payload(code, redirect_uri)
        access_token = AccessTokenUtils.request(headers, payload)
        return SpotifyClient(access_token=access_token)
