class SpotifyClientFunctionality_Users:
    def get_current_user_profile(self):
        raise NotImplementedError

    def get_user_top_items(self):
        raise NotImplementedError

    def get_user_profile(self):
        raise NotImplementedError

    def follow_playlist(self):
        raise NotImplementedError

    def unfollow_playlist(self):
        raise NotImplementedError

    def get_followed_artists(self):
        raise NotImplementedError

    def follow_artists_or_users(self):
        raise NotImplementedError

    def unfollow_artists_or_users(self):
        raise NotImplementedError

    def check_if_user_follows_artists_or_users(self):
        raise NotImplementedError

    def check_if_current_user_follows_playlist(self):
        raise NotImplementedError
