"""Minecraft application launcher."""
from backend.base_app import BaseApplication


class MinecraftApp(BaseApplication):
    """Minecraft game launcher."""
    
    def __init__(self):
        super().__init__(
            name="Minecraft",
            macos_name="Minecraft",
            windows_exe="minecraft.exe",
            linux_name="minecraft-launcher",
            icon="⛏️"
        )
