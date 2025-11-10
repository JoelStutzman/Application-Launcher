# Application Launcher

A cross-platform GUI application launcher built with Python and Tkinter that runs as a **native application** on macOS and Windows (no Python launcher required!).

## Features

✨ **Search & Filter** - Quickly find applications with the built-in search bar
🎨 **Visual Icons** - Each application has a unique emoji icon for easy identification  
🔍 **Smart Detection** - Automatically detects which applications are installed on your system
⌨️ **Keyboard Shortcuts** - Navigate efficiently with keyboard commands
📊 **Status Bar** - See at a glance how many apps are available
🎯 **Modern UI** - Clean, dark-themed interface with smooth interactions
🚀 **Standalone App** - Runs as its own native application on macOS and Windows
🌍 **Cross-Platform** - Works on macOS, Windows, and Linux

### Keyboard Shortcuts

- `Ctrl/⌘ + F` - Focus search bar
- `Esc` - Exit application
- Click app buttons to launch

## Quick Start (macOS)

### Build and Install

1. **Build the standalone app:**
   ```bash
   ./build_app.sh
   ```

2. **Install to /Applications:**
   ```bash
   ./install_app.sh
   ```

3. **Launch the app:**
   - From Finder: Open /Applications and double-click "Application Launcher.app"
   - From Spotlight: Press `Cmd + Space`, type "Application Launcher"
   - From Terminal: `open -a "Application Launcher"`

### Quick Development Cycle

To rebuild and test quickly during development:
```bash
./rebuild_and_test.sh
```

## Quick Start (Windows)

### Build Windows Executable

1. **Install PyInstaller:**
   ```bash
   pip install -r requirements-windows.txt
   ```

2. **Build the executable:**
   ```bash
   python build_windows.py
   ```

3. **Run the app:**
   - Double-click `dist/ApplicationLauncher.exe`
   - Or create a desktop shortcut

4. **(Optional) Create installer:**
   - See [BUILD_WINDOWS.md](BUILD_WINDOWS.md) for detailed instructions

## Building the Standalone App (Detailed)

### Using py2app (Recommended for macOS)

The application is configured to build as a standalone macOS application using py2app. This means:
- ✅ No Python launcher appears
- ✅ Runs like any native Mac app
- ✅ Shows in Dock with proper activation
- ✅ All dependencies bundled
- ✅ Works on other Macs without Python installed

See [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md) for complete details on:
- Build configuration
- Installation options
- Troubleshooting
- Distribution setup

### Using PyInstaller (Cross-platform alternative)

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the app:
   ```bash
   pyinstaller --name="Application Launcher" --windowed --onefile main.py
   ```

3. The app will be in the `dist` folder.

## Running from Source

```bash
python main.py
```

## Adding New Applications

1. Create a new class file in `backend/apps/`
2. Import it in `backend/apps/__init__.py`
3. Add it to `APPLICATION_INSTANCES` in `backend/programs.py`
