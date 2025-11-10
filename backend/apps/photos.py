from backend.base_app import BaseApplication
import platform

class PhotosApp(BaseApplication):
    """Photos app (macOS) or Photos (Windows)."""
    
    def __init__(self):
        system = platform.system()
        if system == "Darwin":
            name = "Photos"
            macos_name = "Photos"
            windows_exe = None
        else:
            name = "Photos"
            macos_name = "Photos"
            windows_exe = "Microsoft.Photos.exe"
        
        super().__init__(
            name=name,
            macos_name=macos_name,
            windows_exe=windows_exe,
            linux_name="shotwell",
            icon="📷"
        )