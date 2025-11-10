"""Application classes package."""

from backend.apps.minecraft import MinecraftApp
from backend.apps.spotify import SpotifyApp
from backend.apps.firefox import FirefoxApp
from backend.apps.safari import SafariApp
from backend.apps.chrome import ChromeApp
from backend.apps.vscode import VSCodeApp
from backend.apps.notes import NotesApp
from backend.apps.calculator import CalculatorApp
from backend.apps.photos import PhotosApp

__all__ = [
    'MinecraftApp',
    'SpotifyApp',
    'FirefoxApp',
    'SafariApp',
    'ChromeApp',
    'VSCodeApp',
    'NotesApp',
    'CalculatorApp',
    'PhotosApp',
]
