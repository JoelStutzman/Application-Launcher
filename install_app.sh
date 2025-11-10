#!/bin/bash
# Installation script for Application Launcher

APP_NAME="Application Launcher.app"
SOURCE_PATH="dist/$APP_NAME"
INSTALL_PATH="/Applications/$APP_NAME"

echo "📦 Installing Application Launcher..."

# Check if the app exists in dist
if [ ! -d "$SOURCE_PATH" ]; then
    echo "❌ App not found in dist/. Please run ./build_app.sh first."
    exit 1
fi

# Remove old installation if it exists
if [ -d "$INSTALL_PATH" ]; then
    echo "🗑️  Removing old installation..."
    rm -rf "$INSTALL_PATH"
fi

# Copy to Applications
echo "📋 Copying to /Applications..."
cp -r "$SOURCE_PATH" "$INSTALL_PATH"

# Make sure it's executable
chmod -R 755 "$INSTALL_PATH"

# Clear quarantine attribute (allows running without "App is damaged" error)
echo "🔓 Removing quarantine attributes..."
xattr -cr "$INSTALL_PATH"

echo "✅ Installation complete!"
echo "📱 You can now launch '$APP_NAME' from /Applications"
echo ""
echo "To launch from command line:"
echo "  open -a \"Application Launcher\""
