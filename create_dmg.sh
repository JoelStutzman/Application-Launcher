#!/bin/bash
# Create DMG installer for Application Launcher

APP_NAME="Application Launcher"
DMG_NAME="Application-Launcher-Installer"
VERSION="1.0.0"

echo "📦 Creating DMG Installer for Application Launcher..."

# Check if app exists
if [ ! -d "dist/${APP_NAME}.app" ]; then
    echo "❌ App not found. Please run ./build_app.sh first."
    exit 1
fi

# Check if create-dmg is installed
if ! command -v create-dmg &> /dev/null; then
    echo "📥 Installing create-dmg..."
    if command -v brew &> /dev/null; then
        brew install create-dmg
    else
        echo "❌ Homebrew not found. Please install Homebrew first:"
        echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi
fi

# Remove old DMG if it exists
rm -f "${DMG_NAME}.dmg"

# Create DMG
echo "🔨 Building DMG installer..."
create-dmg \
  --volname "${APP_NAME}" \
  --volicon "dist/${APP_NAME}.app/Contents/Resources/ApplicationStub.icns" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "${APP_NAME}.app" 175 120 \
  --hide-extension "${APP_NAME}.app" \
  --app-drop-link 425 120 \
  --no-internet-enable \
  "${DMG_NAME}.dmg" \
  "dist/${APP_NAME}.app" 2>/dev/null || \
create-dmg \
  --volname "${APP_NAME}" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "${APP_NAME}.app" 175 120 \
  --hide-extension "${APP_NAME}.app" \
  --app-drop-link 425 120 \
  --no-internet-enable \
  "${DMG_NAME}.dmg" \
  "dist/${APP_NAME}.app"

if [ -f "${DMG_NAME}.dmg" ]; then
    echo "✅ DMG installer created successfully!"
    echo "📁 Location: $(pwd)/${DMG_NAME}.dmg"
    echo ""
    echo "📤 You can now distribute ${DMG_NAME}.dmg"
    echo "   Users can:"
    echo "   1. Double-click the DMG"
    echo "   2. Drag the app to Applications"
    echo "   3. Launch from Applications"
else
    echo "❌ Failed to create DMG"
    exit 1
fi
