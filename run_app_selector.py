#!/usr/bin/env python3
"""
Standalone launcher for the Application Selector GUI.
Run this script to open the application selector interface.
"""
import sys
import os

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Import and run the app selector
from backend.app_selector import main

if __name__ == "__main__":
    main()
