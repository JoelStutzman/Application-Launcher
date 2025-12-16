#!/bin/bash
# Complete build and package workflow

echo "🚀 Complete Build & Package Workflow"
echo "===================================="
echo ""

# Step 1: Build the app
echo "Step 1: Building application..."
./build_app.sh
if [ $? -ne 0 ]; then
    echo "❌ Build failed!"
    exit 1
fi

echo ""
echo "Step 2: Creating DMG installer..."
./create_dmg.sh
if [ $? -ne 0 ]; then
    echo "❌ DMG creation failed!"
    exit 1
fi

echo ""
echo "✅ Complete! Ready for distribution."
echo ""
echo "📦 Files created:"
echo "   - dist/Application Launcher.app"
echo "   - Application-Launcher-Installer.dmg"
echo ""
echo "🎯 Next steps:"
echo "   - Test locally: open 'dist/Application Launcher.app'"
echo "   - Install: ./install_app.sh"
echo "   - Distribute: Share Application-Launcher-Installer.dmg"
