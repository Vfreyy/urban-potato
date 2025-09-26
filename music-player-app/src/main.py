# filepath: music-player-app/src/main.py

from player import Player
from ui import UserInterface
from utils import load_music_files

def main():
    # Initialize the music player
    player = Player()
    
    # Load music files from a specified directory
    music_files = load_music_files("path/to/music/directory")
    
    # Set up the user interface
    ui = UserInterface(player, music_files)
    
    # Start the user interface
    ui.run()

if __name__ == "__main__":
    main()