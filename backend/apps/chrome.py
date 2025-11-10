"""Google Chrome application launcher."""
from backend.base_app import BaseApplication


class ChromeApp(BaseApplication):
    """Google Chrome web browser."""
    
    def __init__(self):
        super().__init__(
            name="Google Chrome",
            macos_name="Google Chrome",
            windows_exe="chrome.exe",
            linux_name="google-chrome",
            icon="🌐"
        )
