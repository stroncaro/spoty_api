class AuthData:
    def __init__(self, json: dict):
        self.access_token = json["access_token"]
        self.token_type = json["token_type"]
        self.expires_in = json["expires_in"]
