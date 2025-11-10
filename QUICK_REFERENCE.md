# Application Launcher - Quick Reference

## Scripts Overview

### `build_app.sh`
**Purpose**: Build the standalone macOS application
**What it does**:
- Checks if py2app is installed (installs if needed)
- Cleans previous builds (removes build/ and dist/ folders)
- Builds the standalone .app bundle
- Shows success message with next steps

**Usage**:
```bash
./build_app.sh
```

**Output**: Creates `dist/Application Launcher.app`

---

### `install_app.sh`
**Purpose**: Install the app to /Applications folder
**What it does**:
- Removes any existing installation
- Copies the app to /Applications
- Sets proper permissions (755)
- Removes quarantine attributes (prevents "damaged app" errors)
- Shows success message with launch instructions

**Usage**:
```bash
./install_app.sh
```

**Requirements**: Must run `build_app.sh` first

---

### `rebuild_and_test.sh`
**Purpose**: Quick development cycle - rebuild and test
**What it does**:
- Runs build_app.sh
- Removes quarantine attributes
- Launches the app directly from dist/ folder (without installing)

**Usage**:
```bash
./rebuild_and_test.sh
```

**Best for**: Testing changes during development without installing

---

## Typical Workflow

### First Time Setup
```bash
./build_app.sh
./install_app.sh
```

### During Development
```bash
# Make changes to code...
./rebuild_and_test.sh
```

### Final Distribution
```bash
./build_app.sh
# Then distribute dist/Application Launcher.app
```

---

## Launching the App

After installation, launch via:

**Finder**: 
- Navigate to /Applications
- Double-click "Application Launcher.app"

**Spotlight**:
- Press `Cmd + Space`
- Type "Application Launcher"
- Press Enter

**Terminal**:
```bash
open -a "Application Launcher"
```

**Dock** (if pinned):
- Click the app icon

---

## Troubleshooting

### "Application is damaged" error
```bash
xattr -cr "/Applications/Application Launcher.app"
```

### Build fails
1. Check if py2app is installed: `pip3 list | grep py2app`
2. Install if missing: `pip3 install py2app`
3. Try again: `./build_app.sh`

### App doesn't launch
1. Check if it exists: `ls -lh "/Applications/Application Launcher.app"`
2. Check permissions: Should show `drwxr-xr-x`
3. Reinstall: `./install_app.sh`

### Python launcher appears instead
- This means you're running the Python script directly
- Make sure to build and install the .app: `./build_app.sh && ./install_app.sh`
- Launch using Finder, Spotlight, or `open -a "Application Launcher"`

---

## File Structure

```
Application_Program/
├── build_app.sh              # Build script
├── install_app.sh            # Installation script
├── rebuild_and_test.sh       # Quick dev cycle script
├── setup.py                  # py2app configuration
├── main.py                   # Application entry point
├── README.md                 # Main documentation
├── BUILD_INSTRUCTIONS.md     # Detailed build guide
├── backend/                  # Backend logic
│   ├── app_selector.py
│   ├── base_app.py
│   ├── programs.py
│   └── apps/                # Individual app definitions
└── gui/                     # GUI components
    └── launcher.py

dist/
└── Application Launcher.app  # Built application (after build_app.sh)

/Applications/
└── Application Launcher.app  # Installed app (after install_app.sh)
```

---

## Key Configuration Files

### `setup.py`
- Defines app bundle settings
- Configures app name, identifier, version
- Lists required packages
- Sets macOS-specific options (Retina support, category, etc.)

### `main.py`
- Entry point for the application
- Sets up window activation for macOS
- Creates and runs the GUI

---

## App Info

**Bundle ID**: `com.yourdomain.applicationlauncher`
**Version**: `1.0.0`
**Category**: Utilities
**Size**: ~111 MB (includes Python runtime and all dependencies)
**Retina Ready**: Yes
**Dock**: Shows in Dock by default

---

## Advanced

### Customizing the App

**Change App Name**:
Edit `setup.py`, modify `CFBundleName` and `CFBundleDisplayName`

**Add an Icon**:
1. Create an .icns file
2. Update `setup.py`: `'iconfile': 'path/to/icon.icns'`
3. Rebuild

**Hide from Dock**:
Edit `setup.py`: `'LSUIElement': True`
(App will run in menu bar only)

**Change Bundle ID**:
Edit `setup.py`: `'CFBundleIdentifier': 'com.yourcompany.yourapp'`

After any changes, rebuild:
```bash
./build_app.sh
./install_app.sh
```
