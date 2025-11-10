# GitHub Repository Setup Instructions

## Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Fill in the repository details:
   - **Repository name:** `Application-Launcher` (or your preferred name)
   - **Description:** "Cross-platform GUI application launcher with macOS and Windows support"
   - **Visibility:** Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

## Step 2: Push Your Code

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Application-Launcher.git

# Rename branch to main (if not already)
git branch -M main

# Push your code
git push -u origin main
```

## Alternative: Using SSH (Recommended)

If you have SSH keys set up with GitHub:

```bash
# Add the remote using SSH
git remote add origin git@github.com:YOUR_USERNAME/Application-Launcher.git

# Push
git branch -M main
git push -u origin main
```

## Quick Commands (Copy-Paste Ready)

Once you create the repo on GitHub, run:

```bash
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/Application-Launcher.git
git branch -M main
git push -u origin main
```

## Verify

After pushing, visit your repository at:
https://github.com/YOUR_USERNAME/Application-Launcher

You should see all your files, README, and documentation!

## Next Steps

Consider adding:
- [ ] Repository topics (python, tkinter, gui, launcher, cross-platform)
- [ ] A LICENSE file
- [ ] GitHub Actions for automated builds
- [ ] Releases with pre-built executables
