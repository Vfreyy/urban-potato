def load_music_files(directory):
    import os
    music_files = []
    for filename in os.listdir(directory):
        if filename.endswith(('.mp3', '.wav', '.flac')):
            music_files.append(os.path.join(directory, filename))
    return music_files

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes}:{seconds:02d}"