# Building Application Launcher for Windows

This guide explains how to build and distribute the Application Launcher on Windows.

## Prerequisites

1. **Python 3.8+** installed on Windows
2. **PyInstaller** for creating executables
3. **(Optional) Inno Setup** for creating installers

## Method 1: Build Executable Only

### Step 1: Install PyInstaller

Open Command Prompt or PowerShell and run:

```bash
pip install pyinstaller
```

### Step 2: Build the Executable

Run the build script:

```bash
python build_windows.py
```

This will create:
- `dist/ApplicationLauncher.exe` - Standalone executable

You can now distribute this `.exe` file. Users just need to:
1. Download `ApplicationLauncher.exe`
2. Double-click to run
3. (Optional) Create a shortcut on Desktop

## Method 2: Create an Installer (Recommended)

An installer provides a better user experience with proper installation, start menu shortcuts, and uninstaller.

### Step 1: Build the Executable

First, build the executable as shown above:

```bash
python build_windows.py
```

### Step 2: Install Inno Setup

Download and install Inno Setup from: https://jrsoftware.org/isinfo.php

### Step 3: Create the Installer

1. Open Inno Setup
2. Open the file `setup_windows.iss`
3. Click "Build" → "Compile"
4. The installer will be created in `installer/ApplicationLauncher-Setup.exe`

### Step 4: Distribute

Share the `ApplicationLauncher-Setup.exe` file. Users can:
1. Download the installer
2. Run it and follow the installation wizard
3. Find "Application Launcher" in their Start Menu

## Alternative: Using NSIS

If you prefer NSIS over Inno Setup, create an NSIS script:

1. Install NSIS from: https://nsis.sourceforge.io/
2. Create an `.nsi` script file
3. Compile to create the installer

## Build Script Options

The `build_windows.py` script uses PyInstaller with these options:

- `--onefile`: Creates a single executable (no DLL dependencies)
- `--windowed`: No console window (GUI mode)
- `--clean`: Clean build cache before building
- `--add-data`: Include backend and gui folders

### Customization

You can modify `build_windows.py` to:

1. **Add an icon:**
   ```python
   '--icon=path/to/icon.ico',
   ```

2. **Include additional files:**
   ```python
   '--add-data=config;config',
   ```

3. **Change version info:**
   Add version information to the executable properties

## Distribution Methods

### Option 1: Direct Download
- Host the `.exe` file on your website or GitHub releases
- Users download and run directly

### Option 2: Installer Package
- Create installer with Inno Setup or NSIS
- Provides professional installation experience
- Adds to Programs and Features for easy uninstall

### Option 3: Microsoft Store
- Package as MSIX
- Distribute through Microsoft Store
- Requires developer account

### Option 4: Portable App
- Distribute the `.exe` in a ZIP file
- No installation required
- Users can run from USB drive or any folder

## Testing

Before distributing:

1. Test on a clean Windows machine (without Python installed)
2. Test on both Windows 10 and Windows 11
3. Test with antivirus software enabled
4. Verify all app launches work correctly

## Code Signing (Optional but Recommended)

To avoid Windows SmartScreen warnings:

1. Obtain a code signing certificate
2. Sign the executable with `signtool.exe`
3. Users won't see "Unknown Publisher" warnings

```bash
signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com ApplicationLauncher.exe
```

## Troubleshooting

### "App can't be opened" or "Windows protected your PC"

This is Windows SmartScreen. Users can click "More info" → "Run anyway" or you can code-sign your app.

### Antivirus False Positives

PyInstaller executables sometimes trigger false positives. Solutions:
- Code sign your executable
- Submit to antivirus vendors for whitelisting
- Use alternative packaging methods (e.g., py2exe)

### Missing DLL Errors

If users get DLL errors:
- Use `--onefile` mode (already default)
- Or include Visual C++ Redistributable in installer

## Updates

To release updates:

1. Update version in `setup_windows.iss`
2. Rebuild with `python build_windows.py`
3. Create new installer
4. Distribute new installer to users

## GitHub Releases

You can automate builds using GitHub Actions:

```yaml
name: Build Windows

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install pyinstaller
      - run: python build_windows.py
      - uses: actions/upload-artifact@v2
        with:
          name: ApplicationLauncher-Windows
          path: dist/ApplicationLauncher.exe
```
