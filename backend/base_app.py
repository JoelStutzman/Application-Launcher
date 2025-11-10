"""
Base class for all launchable applications.
"""
import subprocess
import platform
from abc import ABC, abstractmethod


class BaseApplication(ABC):
    """Abstract base class for all applications."""
    
    def __init__(self, name: str, macos_name: str = None, windows_exe: str = None, linux_name: str = None, icon: str = "📦"):
        """
        Initialize the application.
        
        Args:
            name: Display name of the application
            macos_name: Application name for macOS (used with 'open -a')
            windows_exe: Executable name for Windows
            linux_name: Application name for Linux
            icon: Emoji icon for the application
        """
        self.name = name
        self.icon = icon
        self.macos_name = macos_name or name
        self.windows_exe = windows_exe or f"{name.lower()}.exe"
        self.linux_name = linux_name or name.lower()
    
    def launch(self) -> None:
        """Launch the application on the current platform."""
        try:
            print(f"\nLaunching {self.name}...")
            system = platform.system()
            
            if system == "Darwin":  # macOS
                self._launch_macos()
            elif system == "Windows":
                self._launch_windows()
            else:  # Linux
                self._launch_linux()
            
            print(f"✓ {self.name} launched successfully!")
        except subprocess.CalledProcessError:
            print(f"✗ Error: Could not launch {self.name}. Make sure it's installed.")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def _launch_macos(self) -> None:
        """Launch on macOS."""
        subprocess.run(['open', '-a', self.macos_name], check=True)
    
    def _launch_windows(self) -> None:
        """Launch on Windows."""
        subprocess.Popen(self.windows_exe, shell=True)
    
    def _launch_linux(self) -> None:
        """Launch on Linux."""
        try:
            subprocess.Popen(['xdg-open', self.linux_name])
        except:
            subprocess.Popen(self.linux_name, shell=True)
    
    def is_available(self) -> bool:
        """Check if the application is available on the current platform."""
        import shutil
        system = platform.system()
        
        if system == "Darwin":  # macOS
            # Check if app exists in /Applications, ~/Applications, or /System/Applications
            import os
            app_locations = [
                f"/Applications/{self.macos_name}.app",
                os.path.expanduser(f"~/Applications/{self.macos_name}.app"),
                f"/System/Applications/{self.macos_name}.app"
            ]
            return any(os.path.exists(loc) for loc in app_locations)
        elif system == "Windows":
            # Check if executable is in PATH
            return shutil.which(self.windows_exe) is not None
        else:  # Linux
            # Check if command is available
            return shutil.which(self.linux_name) is not None
