"""Spotify application launcher."""
from backend.base_app import BaseApplication


class SpotifyApp(BaseApplication):
    """Spotify music player."""
    
    def __init__(self):
        super().__init__(
            name="Spotify",
            macos_name="Spotify",
            windows_exe="spotify.exe",
            linux_name="spotify",
            icon="🎵"
        )
