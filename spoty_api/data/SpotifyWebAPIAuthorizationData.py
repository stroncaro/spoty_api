from ._DictEntity import DictEntity


class SpotifyWebAPIAuthorizationData(DictEntity):
    """
    Authorization data received from Spotify servers after successful authentication.

    Attributes:
        access_token (str): The token used to authenticate requests to the Spotify Web API.
        token_type (str): The type of token provided (typically "Bearer").
        expires_in (int): The time (in seconds) until the access token expires.
    """

    access_token: str
    token_type: str
    expires_in: int
