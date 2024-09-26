from ..exceptions import InvalidJSONException


class SpotifyWebAPIAuthorizationData:
    @staticmethod
    def from_json(json: dict):
        """
        Instantiates SpotifyWebAPIAuthorizationData from a JSON dict.

        Extracts the "access_token", "token_type", and "expires_in" fields.
        Raises a KeyError if any required field is missing.

        Args:
            json (dict): A dictionary containing authorization data.

        Returns:
            SpotifyWebAPIAuthorizationData: An instance with the parsed data.

        Raises:
            InvalidJSONException: If required fields are missing.
        """

        required_fields = ("access_token", "token_type", "expires_in")
        missing_fields = [
            field for field in required_fields if field not in json.keys()
        ]
        if missing_fields:
            raise InvalidJSONException("Missing fields: " + ",".join(missing_fields))

        auth_data = SpotifyWebAPIAuthorizationData()
        auth_data.access_token = json["access_token"]
        auth_data.token_type = json["token_type"]
        auth_data.expires_in = json["expires_in"]
        return auth_data
