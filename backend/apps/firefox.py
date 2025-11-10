"""Firefox application launcher."""
from backend.base_app import BaseApplication


class FirefoxApp(BaseApplication):
    """Firefox web browser."""
    
    def __init__(self):
        super().__init__(
            name="Firefox",
            macos_name="Firefox",
            windows_exe="firefox.exe",
            linux_name="firefox",
            icon="🦊"
        )
