"""
Program registry for the application launcher.
Import and register new application classes here.
"""
from backend.apps import (
    MinecraftApp,
    SpotifyApp,
    FirefoxApp,
    SafariApp,
    ChromeApp,
    VSCodeApp,
    NotesApp,
    CalculatorApp,
    PhotosApp
    )


# List of all available applications
# To add a new app: 1) Create a class file in backend/apps/
#                   2) Import it above
#                   3) Add an instance to this list
APPLICATION_INSTANCES = [
    MinecraftApp(),
    SpotifyApp(),
    FirefoxApp(),
    SafariApp(),
    ChromeApp(),
    VSCodeApp(),
    NotesApp(),
    CalculatorApp(),
    PhotosApp(),
]


# Dictionary mapping program numbers to their instances
# This is auto-generated from APPLICATION_INSTANCES
PROGRAMS = {
    i + 1: (f"{app.icon} {app.name}", app.launch, app.is_available())
    for i, app in enumerate(APPLICATION_INSTANCES)
}


def get_available_programs() -> list[str]:
    """Return list of available program names."""
    return [name for name, _ in PROGRAMS.values()]


def run_program(choice: int) -> None:
    """Run the selected program."""
    if choice in PROGRAMS:
        _, program_func = PROGRAMS[choice]
        program_func()
    else:
        print("Program not found!")

