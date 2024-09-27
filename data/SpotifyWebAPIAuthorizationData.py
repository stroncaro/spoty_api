from ._DictEntity import DictEntity


class SpotifyWebAPIAuthorizationData(DictEntity):
    access_token: str
    token_type: str
    expires_in: int
