# Admin Password Protection - Quick Guide

## Overview
The Application Launcher now includes **password-protected exit functionality** to prevent unauthorized users from closing the application.

## Default Admin Password
```
admin123
```

**⚠️ IMPORTANT**: Change this password in the code for security!

## How to Change the Password

Edit `/Users/joelstutzman/Coding/Application_Program/gui/launcher.py`:

1. Find line ~24:
```python
# Admin password (you can change this)
self.admin_password = "admin123"
```

2. Change to your desired password:
```python
self.admin_password = "your_secure_password_here"
```

3. Save and restart/rebuild the app

## Features

### 🔒 Admin Quit Button
- Located in the **bottom-right corner** of the status bar
- Dark red color with lock icon
- Requires password to exit

### 🚫 Disabled Exit Methods
- **Escape key**: No longer closes the app
- **Window close button (X)**: Requires password
- **Old Exit button**: Removed

### ✅ How It Works

1. **Click "🔒 Admin Quit"** or **click the window close button (X)**
2. **Password Dialog appears**
3. **Enter password**: `admin123` (default)
4. **Confirm quit**: Click "OK" on confirmation dialog
5. **Access denied**: Wrong password shows error message

### Password Dialog Features
- ✅ Password is **hidden** (shows as dots)
- ✅ Can **cancel** by clicking Cancel or closing dialog
- ✅ Shows **error message** for incorrect password
- ✅ Requires **confirmation** after correct password

## Security Tips

1. **Change Default Password**
   - The default `admin123` is for testing only
   - Use a strong, unique password

2. **For Production Use**
   - Consider storing password securely (encrypted)
   - Consider using system authentication
   - Add password complexity requirements

3. **Multiple Admin Levels** (Future Enhancement)
   - Could add different passwords for different actions
   - Could log failed attempts

## Rebuilding the Standalone App

After changing the password, rebuild the app:

```bash
./build_app.sh
./install_app.sh
```

Or for quick testing:
```bash
./rebuild_and_test.sh
```

## Usage Example

**Normal User Attempt:**
1. User clicks 🔒 Admin Quit
2. Password dialog appears
3. User enters wrong password
4. ❌ "Access Denied" error message
5. App continues running

**Admin Exit:**
1. Admin clicks 🔒 Admin Quit
2. Password dialog appears
3. Admin enters `admin123`
4. ✅ Confirmation dialog: "Are you sure?"
5. Admin clicks OK
6. App closes

## Troubleshooting

**Q: I forgot my password!**
A: Edit `gui/launcher.py` line ~24 and change `self.admin_password`

**Q: Can users still force quit?**
A: Yes, users can force quit via Activity Monitor or `killall` command. This protection is for normal UI interaction only.

**Q: How do I add more security?**
A: Consider:
- Multiple failed attempt lockout
- Logging failed attempts
- Time-based temporary locks
- System-level authentication

**Q: Window still closes without password**
A: Make sure you've:
1. Saved the changes
2. Restarted the application
3. Check for any syntax errors

## Code Locations

- **Password Definition**: `gui/launcher.py` line ~24
- **Admin Quit Method**: `gui/launcher.py` line ~316
- **Window Close Handler**: `gui/launcher.py` line ~38
- **Admin Quit Button**: `gui/launcher.py` line ~135

## Future Enhancements

Possible improvements:
- [ ] Store password encrypted
- [ ] Multiple admin users
- [ ] Password expiration
- [ ] Failed attempt logging
- [ ] Biometric authentication
- [ ] System keychain integration
- [ ] Remote admin unlock
