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
echo "Step 2: Creating PKG installer (one-click install)..."
./create_pkg.sh
if [ $? -ne 0 ]; then
    echo "❌ PKG creation failed!"
    exit 1
fi

echo ""
echo "✅ Complete! Ready for distribution."
echo ""
echo "📦 Files created:"
echo "   - dist/Application Launcher.app"
echo "   - Application-Launcher-Installer.pkg"
echo ""
echo "🎯 Next steps:"
echo "   - Test locally: open 'dist/Application Launcher.app'"
echo "   - Test installer: open Application-Launcher-Installer.pkg"
echo "   - Distribute: Share Application-Launcher-Installer.pkg"
echo ""
echo "💡 One-click installation - no drag-and-drop required!"
