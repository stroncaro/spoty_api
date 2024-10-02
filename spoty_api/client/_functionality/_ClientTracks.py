class SpotifyClientFunctionality_Tracks:
    def get_track(self):
        raise NotImplementedError

    def get_several_tracks(self):
        raise NotImplementedError

    def get_user_saved_tracks(self):
        raise NotImplementedError

    def save_tracks_for_current_user(self):
        raise NotImplementedError

    def remove_user_saved_tracks(self):
        raise NotImplementedError

    def check_user_saved_tracks(self):
        raise NotImplementedError

    def get_several_tracks_audio_features(self):
        raise NotImplementedError

    def get_track_audio_features(self):
        raise NotImplementedError

    def get_track_audio_analysis(self):
        raise NotImplementedError

    def get_recommendations(self):
        raise NotImplementedError
