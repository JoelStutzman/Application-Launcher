"""
Windows build script using PyInstaller.
Run this on a Windows machine to create a Windows executable.
"""
import PyInstaller.__main__
import sys
import os

def build_windows_exe():
    """Build Windows executable using PyInstaller."""
    
    # PyInstaller arguments
    args = [
        'main.py',                          # Your main script
        '--name=ApplicationLauncher',       # Name of the executable
        '--onefile',                        # Create a single executable file
        '--windowed',                       # Don't show console window (GUI app)
        '--icon=NONE',                      # Add icon file here if you have one
        '--add-data=backend;backend',       # Include backend folder
        '--add-data=gui;gui',               # Include gui folder
        '--hidden-import=tkinter',
        '--hidden-import=backend.apps',
        '--hidden-import=backend.programs',
        '--hidden-import=gui.launcher',
        '--clean',                          # Clean PyInstaller cache
        '--noconfirm',                      # Overwrite output directory without asking
    ]
    
    print("Building Windows executable...")
    print("This may take a few minutes...\n")
    
    PyInstaller.__main__.run(args)
    
    print("\n✅ Build complete!")
    print("📁 Executable location: dist/ApplicationLauncher.exe")
    print("\nTo create an installer, you can use:")
    print("  - Inno Setup (free): https://jrsoftware.org/isinfo.php")
    print("  - NSIS (free): https://nsis.sourceforge.io/")
    print("  - Advanced Installer: https://www.advancedinstaller.com/")

if __name__ == "__main__":
    build_windows_exe()
