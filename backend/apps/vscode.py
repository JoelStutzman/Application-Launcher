"""Visual Studio Code application launcher."""
from backend.base_app import BaseApplication


class VSCodeApp(BaseApplication):
    """Visual Studio Code editor."""
    
    def __init__(self):
        super().__init__(
            name="Visual Studio Code",
            macos_name="Visual Studio Code",
            windows_exe="Code.exe",
            linux_name="code",
            icon="💻"
        )
