"""
Main entry point for the Application Launcher.
"""
import tkinter as tk
import sys
import os

# Add the application directory to the path when running as a bundled app
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

from gui.launcher import ApplicationLauncher


def main() -> None:
    """Main function to run the GUI application"""
    root = tk.Tk()
    
    # Set the app to appear in front on macOS
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    
    # Force the app to activate and come to front
    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.after(100, lambda: root.call('wm', 'attributes', '.', '-topmost', '0'))
    
    app = ApplicationLauncher(root)
    root.mainloop()


if __name__ == "__main__":
    main()
