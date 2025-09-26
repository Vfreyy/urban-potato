class Player:
    def __init__(self):
        self.current_track = None
        self.is_playing = False

    def load_track(self, track_path):
        self.current_track = track_path
        print(f"Loaded track: {track_path}")

    def play(self):
        if self.current_track:
            self.is_playing = True
            print(f"Playing track: {self.current_track}")
        else:
            print("No track loaded.")

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            print("Playback paused.")
        else:
            print("No track is currently playing.")

    def stop(self):
        if self.is_playing:
            self.is_playing = False
            print("Playback stopped.")
        else:
            print("No track is currently playing.")