"""Calculator application launcher."""
from backend.base_app import BaseApplication


class CalculatorApp(BaseApplication):
    """Calculator application."""
    
    def __init__(self):
        super().__init__(
            name="Calculator",
            macos_name="Calculator",
            windows_exe="calc.exe",
            linux_name="gnome-calculator",
            icon="🧮"
        )
