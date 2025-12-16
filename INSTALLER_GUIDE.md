# Creating an Installer for Application Launcher

## Overview

You can package the Application Launcher as a DMG installer for easy distribution to other Mac users.

---

## Quick Start

### Option 1: One Command (Recommended)
```bash
./build_and_package.sh
```

This will:
1. Build the standalone app
2. Create a DMG installer
3. Output: `Application-Launcher-Installer.dmg`

### Option 2: Step by Step
```bash
# Step 1: Build the app
./build_app.sh

# Step 2: Create DMG installer
./create_dmg.sh
```

---

## What You Get

### DMG Installer Features:
- ✅ Professional drag-to-install interface
- ✅ Application icon visible
- ✅ Applications folder shortcut
- ✅ ~111 MB size (includes all dependencies)
- ✅ Works on any Mac (no Python needed)

### DMG Contents:
```
Application-Launcher-Installer.dmg
└── Application Launcher.app (drag to Applications)
    └── Applications (shortcut)
```

---

## Requirements

### For Building:
- macOS system
- Python 3.x installed
- py2app (`pip install py2app`)
- create-dmg (auto-installed via Homebrew)

### For End Users (Installer):
- macOS 10.13 or later
- No other requirements!

---

## Distribution

Once you have `Application-Launcher-Installer.dmg`, you can:

1. **Share via Email/Cloud**
   - Upload to Google Drive, Dropbox, etc.
   - Share download link with users

2. **USB/Network Distribution**
   - Copy DMG to USB drive
   - Share over local network

3. **Website Download**
   - Host on your website
   - Users download and install

---

## Installation Instructions (For End Users)

Send these instructions with the DMG:

### How to Install:

1. **Download** `Application-Launcher-Installer.dmg`

2. **Double-click** the DMG file
   - A window will open showing the app

3. **Drag** the "Application Launcher" icon to the Applications folder

4. **Eject** the DMG (right-click → Eject)

5. **Launch** the app:
   - Open Applications folder
   - Double-click "Application Launcher"
   - Or use Spotlight: Cmd+Space, type "Application Launcher"

### First Launch:
- macOS may show "unidentified developer" warning
- Right-click the app → Open → Confirm
- Or: System Preferences → Security → Allow anyway

### Admin Password:
- Default password: `admin123`
- Change in settings if needed

---

## Advanced Options

### Custom Volume Icon
Add a custom .icns file:
```bash
# Edit create_dmg.sh line 23:
--volicon "path/to/custom-icon.icns" \
```

### Custom Background
Add a background image:
```bash
--background "path/to/background.png" \
```

### Window Size/Position
Edit in `create_dmg.sh`:
```bash
--window-pos 200 120 \
--window-size 800 400 \
```

---

## Troubleshooting

### "create-dmg: command not found"
```bash
# Install Homebrew first:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then:
brew install create-dmg
```

### DMG creation fails
- Ensure app is built: Check `dist/Application Launcher.app` exists
- Remove old DMG: `rm Application-Launcher-Installer.dmg`
- Try again: `./create_dmg.sh`

### App not found
- Run build first: `./build_app.sh`
- Check dist folder: `ls -la dist/`

---

## File Sizes

- **Source code**: ~100 KB
- **Built app**: ~111 MB
- **DMG installer**: ~80 MB (compressed)

The DMG is compressed, so it's smaller than the app itself.

---

## Security & Code Signing

### Current Setup (Ad-hoc Signing):
- ✅ Works on your Mac
- ✅ Works on other Macs (with security override)
- ❌ Shows security warning on first launch
- ❌ Not notarized by Apple

### For Professional Distribution:
You would need:
1. Apple Developer account ($99/year)
2. Developer ID Application certificate
3. Code sign the app:
   ```bash
   codesign --deep --force --verify --verbose \
     --sign "Developer ID Application: Your Name" \
     "dist/Application Launcher.app"
   ```
4. Notarize with Apple
5. Staple notarization ticket

---

## Complete Workflow

```bash
# 1. Make code changes
vim gui/launcher.py

# 2. Test locally
python3 main.py

# 3. Build and package
./build_and_package.sh

# 4. Test the DMG
open Application-Launcher-Installer.dmg

# 5. Distribute
# Upload DMG to your distribution method
```

---

## Alternative: ZIP Distribution

If you don't want a DMG, you can also distribute as a ZIP:

```bash
# After building
cd dist
zip -r "Application-Launcher-v1.0.zip" "Application Launcher.app"
```

Users extract and drag to Applications.

---

## Summary

**To create installer:**
```bash
./build_and_package.sh
```

**Output:**
- `Application-Launcher-Installer.dmg` (ready to share)

**Users install by:**
- Double-click DMG
- Drag to Applications
- Done!
