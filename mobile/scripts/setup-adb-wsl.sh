#!/bin/bash
# Setup ADB bridge from WSL to Windows Android Emulator
# Run this script after Android Studio SDK setup is complete

WINDOWS_USER="jesse"
ANDROID_SDK_PATH="/mnt/c/Users/$WINDOWS_USER/AppData/Local/Android/Sdk"
ADB_PATH="$ANDROID_SDK_PATH/platform-tools/adb.exe"

echo "=== Study Buddy - Android Emulator Setup for WSL ==="
echo ""

# Check if ADB exists
if [ ! -f "$ADB_PATH" ]; then
    echo "ERROR: ADB not found at $ADB_PATH"
    echo "Please complete Android Studio setup first."
    exit 1
fi

echo "Found ADB at: $ADB_PATH"

# Add Android SDK to PATH in bashrc if not already there
if ! grep -q "ANDROID_SDK" ~/.bashrc; then
    echo "" >> ~/.bashrc
    echo "# Android SDK for WSL" >> ~/.bashrc
    echo "export ANDROID_SDK=\"$ANDROID_SDK_PATH\"" >> ~/.bashrc
    echo "export PATH=\"\$PATH:\$ANDROID_SDK/platform-tools:\$ANDROID_SDK/emulator\"" >> ~/.bashrc
    echo "Added Android SDK to PATH in ~/.bashrc"
fi

# Create alias for adb
echo ""
echo "Creating ADB wrapper script..."

cat > ~/adb-wrapper.sh << 'EOF'
#!/bin/bash
# ADB wrapper for WSL - calls Windows ADB
/mnt/c/Users/jesse/AppData/Local/Android/Sdk/platform-tools/adb.exe "$@"
EOF

chmod +x ~/adb-wrapper.sh

# Add alias if not exists
if ! grep -q "alias adb=" ~/.bashrc; then
    echo "alias adb='~/adb-wrapper.sh'" >> ~/.bashrc
    echo "Added ADB alias to ~/.bashrc"
fi

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "1. Source your bashrc: source ~/.bashrc"
echo "2. List available emulators: emulator.exe -list-avds"
echo "3. Start emulator from Windows or with: emulator.exe -avd <name>"
echo "4. Verify ADB connection: adb devices"
echo ""
echo "To run Expo on the emulator:"
echo "  cd /home/jesse/school/study-buddy/mobile"
echo "  npx expo start --android"
