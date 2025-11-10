"""Safari application launcher."""
from backend.base_app import BaseApplication
import platform


class SafariApp(BaseApplication):
    """Safari web browser (macOS only)."""
    
    def __init__(self):
        super().__init__(
            name="Safari",
            macos_name="Safari",
            windows_exe=None,
            linux_name=None,
            icon="🧭"
        )
    
    def is_available(self) -> bool:
        """Safari is only available on macOS."""
        return platform.system() == "Darwin"
    
    def launch(self) -> None:
        """Override launch to check availability."""
        if not self.is_available():
            print("✗ Safari is only available on macOS")
            return
        super().launch()
