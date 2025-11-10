#!/bin/bash
# Quick rebuild and test script for development

echo "🔄 Quick rebuild and test..."

# Build
./build_app.sh || exit 1

# Remove quarantine for local testing
echo "🔓 Removing quarantine attributes..."
xattr -cr "dist/Application Launcher.app"

# Launch
echo "🚀 Launching app..."
open "dist/Application Launcher.app"

echo "✅ App launched from dist/ folder (not installed)"
