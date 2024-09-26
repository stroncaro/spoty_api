from ..exceptions import InvalidJSONException
from .._aux import validate_json


class SpotifyWebAPIAuthorizationData:
    @staticmethod
    def from_json(json: dict):
        """
        Instantiates SpotifyWebAPIAuthorizationData from a JSON dict.

        Extracts the "access_token", "token_type", and "expires_in" fields.
        Raises a InvalidJSONException if any required field is missing.

        Args:
            json (dict): A dictionary containing authorization data.

        Returns:
            SpotifyWebAPIAuthorizationData: An instance with the parsed data.

        Raises:
            InvalidJSONException: If required fields are missing.
        """

        validate_json(
            json, required_fields=("access_token", "token_type", "expires_in")
        )

        auth_data = SpotifyWebAPIAuthorizationData()
        auth_data.access_token = json["access_token"]
        auth_data.token_type = json["token_type"]
        auth_data.expires_in = json["expires_in"]
        return auth_data
