# Building Application Launcher as a Standalone macOS App

This document explains how the Application Launcher has been configured to run as its own standalone macOS application instead of using the Python launcher.

## What Was Changed

### 1. **Setup Configuration** (`setup.py`)
The application is built using `py2app` to create a standalone macOS application bundle:
- **Bundle Settings**: Configured with proper macOS app metadata (CFBundleName, CFBundleDisplayName, etc.)
- **High Resolution Support**: Enabled Retina display support with `NSHighResolutionCapable`
- **Application Category**: Set as a utility application
- **Semi-Standalone**: Configured to include all Python dependencies within the app bundle

### 2. **Main Application** (`main.py`)
Enhanced window activation to ensure the app comes to the front:
- Added proper window activation for macOS
- Implemented topmost window handling to ensure visibility on launch

### 3. **Build Script** (`build_app.sh`)
Automated the build process:
- Checks for and installs `py2app` if needed
- Cleans previous builds
- Builds the standalone application
- Provides instructions for installation

### 4. **Installation Script** (`install_app.sh`)
Simplifies deployment:
- Removes old installations
- Copies app to /Applications
- Sets proper permissions
- Removes quarantine attributes to prevent "App is damaged" errors

## How to Build

1. **Build the application:**
   ```bash
   ./build_app.sh
   ```

2. **Install to /Applications:**
   ```bash
   ./install_app.sh
   ```

   Or manually:
   ```bash
   cp -r "dist/Application Launcher.app" /Applications/
   ```

## How to Run

Once installed, you can launch the application in several ways:

1. **From Finder:**
   - Open /Applications folder
   - Double-click "Application Launcher.app"

2. **From Spotlight:**
   - Press `Cmd + Space`
   - Type "Application Launcher"
   - Press Enter

3. **From Terminal:**
   ```bash
   open -a "Application Launcher"
   ```

## Application Structure

The built application includes:
- **Self-contained Python environment**: No system Python required
- **All dependencies bundled**: tkinter, backend modules, GUI components
- **Native macOS integration**: Appears in Dock, properly handles window activation
- **Framework bundles**: Includes Tk/Tcl frameworks for GUI

## Troubleshooting

### "Application is damaged" Error
If you see this error, run:
```bash
xattr -cr "/Applications/Application Launcher.app"
```

### Code Signing Warnings
The build process may show code signing warnings. These can be ignored for personal use. The app will run correctly despite these warnings.

For distribution, you would need:
- An Apple Developer account
- A signing certificate
- Notarization through Apple

### App Doesn't Appear in Dock
Make sure `LSUIElement` is set to `False` in `setup.py` (which it is by default).

## Development vs. Distribution

**Current Setup (Development):**
- Ad-hoc signing (works on your Mac)
- No notarization required
- Quick build process

**For Distribution:**
You would need to:
1. Sign with a Developer ID certificate
2. Notarize with Apple
3. Package as a DMG or PKG installer

## File Locations

- **Source code**: `/Users/joelstutzman/Coding/Application_Program/`
- **Built app**: `/Users/joelstutzman/Coding/Application_Program/dist/Application Launcher.app`
- **Installed app**: `/Applications/Application Launcher.app`

## Benefits of Standalone App

✅ No Python launcher appears
✅ Proper macOS application behavior
✅ Can be launched like any other Mac app
✅ Shows in Dock with its own icon (when icon is added)
✅ All dependencies included
✅ Works on other Macs (without Python installed)
✅ Professional appearance
