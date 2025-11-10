"""
Setup script for creating a standalone macOS application.
Run with: python setup.py py2app
"""
from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['tkinter', 'backend', 'gui'],
    'includes': ['jaraco', 'jaraco.text', 'jaraco.functools', 'jaraco.context', 'jaraco.collections'],
    'iconfile': None,  # You can add an .icns file here if you have one
    'plist': {
        'CFBundleName': 'Application Launcher',
        'CFBundleDisplayName': 'Application Launcher',
        'CFBundleGetInfoString': 'Launch your favorite applications',
        'CFBundleIdentifier': 'com.yourdomain.applicationlauncher',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHumanReadableCopyright': '© 2025',
        'LSUIElement': False,  # Set to True to hide from Dock
        'NSHighResolutionCapable': True,
        'LSApplicationCategoryType': 'public.app-category.utilities',
    },
    'semi_standalone': True,
    'site_packages': True,
}

setup(
    name='Application Launcher',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
