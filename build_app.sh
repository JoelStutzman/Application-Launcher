#!/bin/bash
# Build script for creating a standalone macOS application

echo "🚀 Building Application Launcher..."

# Check if py2app is installed
if ! python3 -c "import py2app" 2>/dev/null; then
    echo "📦 Installing py2app..."
    pip3 install py2app
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build dist

# Build the application (disable automatic code signing)
echo "🔨 Building application..."
export PY2APP_CODESIGN_IDENTITY="-"
python3 setup.py py2app 2>&1 | grep -v "warning: changes being made to the file will invalidate the code signature"

# Check if build was successful
if [ -d "dist/Application Launcher.app" ]; then
    echo "✅ Build successful!"
    echo "📁 Application created at: dist/Application Launcher.app"
    echo ""
    echo "To install, run:"
    echo "  ./install_app.sh"
    echo ""
    echo "To test locally, run:"
    echo "  open \"dist/Application Launcher.app\""
else
    echo "❌ Build failed!"
    exit 1
fi
