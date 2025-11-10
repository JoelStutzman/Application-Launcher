"""Notes/Notepad application launcher."""
from backend.base_app import BaseApplication
import platform


class NotesApp(BaseApplication):
    """Notes app (macOS) or Notepad (Windows)."""
    
    def __init__(self):
        system = platform.system()
        if system == "Darwin":
            name = "Notes"
            macos_name = "Notes"
            windows_exe = None
        else:
            name = "Notepad"
            macos_name = "Notes"
            windows_exe = "notepad.exe"
        
        super().__init__(
            name=name,
            macos_name=macos_name,
            windows_exe=windows_exe,
            linux_name="gedit",
            icon="📝"
        )
