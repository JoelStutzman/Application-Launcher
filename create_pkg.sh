#!/bin/bash
# Create PKG installer for one-click installation

APP_NAME="Application Launcher"
PKG_NAME="Application-Launcher-Installer"
VERSION="1.0.0"
IDENTIFIER="com.yourdomain.applicationlauncher"

echo "📦 Creating PKG Installer for Application Launcher..."

# Check if app exists
if [ ! -d "dist/${APP_NAME}.app" ]; then
    echo "❌ App not found. Please run ./build_app.sh first."
    exit 1
fi

# Create temporary directories
echo "🔧 Preparing installer structure..."
rm -rf installer_build
mkdir -p installer_build/payload/Applications
mkdir -p installer_build/scripts

# Copy app to payload
cp -R "dist/${APP_NAME}.app" "installer_build/payload/Applications/"

# Create postinstall script
cat > installer_build/scripts/postinstall << 'EOF'
#!/bin/bash
# Post-installation script

# Remove quarantine attribute
xattr -cr "/Applications/Application Launcher.app"

# Set permissions
chmod -R 755 "/Applications/Application Launcher.app"

echo "Application Launcher installed successfully!"
exit 0
EOF

chmod +x installer_build/scripts/postinstall

# Build the package
echo "🔨 Building PKG installer..."
pkgbuild \
    --root installer_build/payload \
    --scripts installer_build/scripts \
    --identifier "${IDENTIFIER}" \
    --version "${VERSION}" \
    --install-location / \
    "installer_build/ApplicationLauncher.pkg"

# Create distribution file for better UI
cat > installer_build/distribution.xml << EOF
<?xml version="1.0" encoding="utf-8"?>
<installer-gui-script minSpecVersion="1">
    <title>Application Launcher</title>
    <organization>com.yourdomain</organization>
    <domains enable_localSystem="true"/>
    <options customize="never" require-scripts="false" rootVolumeOnly="true" />
    <welcome file="welcome.html" mime-type="text/html" />
    <pkg-ref id="${IDENTIFIER}">
        <bundle-version>
            <bundle id="${IDENTIFIER}" CFBundleVersion="${VERSION}" path="/Applications/${APP_NAME}.app"/>
        </bundle-version>
    </pkg-ref>
    <choices-outline>
        <line choice="default">
            <line choice="${IDENTIFIER}"/>
        </line>
    </choices-outline>
    <choice id="default"/>
    <choice id="${IDENTIFIER}" visible="false">
        <pkg-ref id="${IDENTIFIER}"/>
    </choice>
    <pkg-ref id="${IDENTIFIER}" version="${VERSION}" onConclusion="none">ApplicationLauncher.pkg</pkg-ref>
</installer-gui-script>
EOF

# Create welcome message
cat > installer_build/welcome.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
            font-size: 13px;
            padding: 20px;
        }
        h1 {
            font-size: 24px;
            font-weight: 300;
            margin-bottom: 20px;
        }
        .feature {
            margin: 10px 0;
            padding-left: 25px;
        }
        .feature:before {
            content: "✓ ";
            color: #007AFF;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Welcome to Application Launcher</h1>
    <p>This installer will install Application Launcher on your computer.</p>
    
    <div style="margin-top: 20px;">
        <div class="feature">Fullscreen kiosk-style interface</div>
        <div class="feature">Password-protected exit (admin123)</div>
        <div class="feature">Quick access to common applications</div>
        <div class="feature">Search and filter functionality</div>
    </div>
    
    <p style="margin-top: 30px;">Click <strong>Continue</strong> to begin the installation.</p>
</body>
</html>
EOF

# Build the final product
echo "📦 Creating distribution package..."
productbuild \
    --distribution installer_build/distribution.xml \
    --package-path installer_build \
    --resources installer_build \
    "${PKG_NAME}.pkg"

# Clean up
rm -rf installer_build

if [ -f "${PKG_NAME}.pkg" ]; then
    echo "✅ PKG installer created successfully!"
    echo "📁 Location: $(pwd)/${PKG_NAME}.pkg"
    echo ""
    echo "📤 Distribution ready!"
    echo "   Users can:"
    echo "   1. Double-click ${PKG_NAME}.pkg"
    echo "   2. Click Continue → Install"
    echo "   3. Done! App is in /Applications"
    echo ""
    echo "💡 No drag-and-drop needed - fully automated installation!"
else
    echo "❌ Failed to create PKG"
    exit 1
fi
