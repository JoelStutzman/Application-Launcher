"""
Standalone Application Selector
A GUI app for selecting and launching approved applications installed on the device.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import platform
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.programs import APPLICATION_INSTANCES


class AppSelectorGUI:
    """GUI application for selecting and launching approved apps."""
    
    def __init__(self, root):
        """Initialize the application selector GUI."""
        self.root = root
        self.root.title("Application Selector")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Get system info
        self.system = platform.system()
        
        # Set up the UI
        self._setup_ui()
        
        # Load applications
        self._load_applications()
    
    def _setup_ui(self):
        """Set up the user interface."""
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", pady=15)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            header_frame,
            text="📱 Application Selector",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text=f"Select an approved application to launch ({self.system})",
            font=("Arial", 10),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        subtitle_label.pack()
        
        # Main content area
        content_frame = tk.Frame(self.root, padx=20, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Info label
        info_label = tk.Label(
            content_frame,
            text="Available Applications:",
            font=("Arial", 12, "bold"),
            anchor="w"
        )
        info_label.pack(fill=tk.X, pady=(0, 10))
        
        # Scrollable list frame
        list_frame = tk.Frame(content_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for applications
        self.app_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 12),
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set,
            height=12,
            activestyle='dotbox',
            selectbackground="#3498db",
            selectforeground="white"
        )
        self.app_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.app_listbox.yview)
        
        # Bind double-click to launch
        self.app_listbox.bind('<Double-Button-1>', lambda e: self._launch_selected())
        
        # Store app instances for quick access
        self.app_instances = []
        
        # Button frame
        button_frame = tk.Frame(content_frame)
        button_frame.pack(fill=tk.X, pady=(15, 0))
        
        # Launch button
        self.launch_btn = tk.Button(
            button_frame,
            text="🚀 Launch Application",
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            activebackground="#229954",
            activeforeground="white",
            command=self._launch_selected,
            cursor="hand2",
            pady=10
        )
        self.launch_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        # Refresh button
        self.refresh_btn = tk.Button(
            button_frame,
            text="🔄 Refresh",
            font=("Arial", 12),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            command=self._load_applications,
            cursor="hand2",
            pady=10
        )
        self.refresh_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        # Status bar
        self.status_frame = tk.Frame(self.root, bg="#34495e", pady=8)
        self.status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="Ready",
            font=("Arial", 9),
            bg="#34495e",
            fg="white",
            anchor="w"
        )
        self.status_label.pack(fill=tk.X, padx=10)
    
    def _load_applications(self):
        """Load and display available applications."""
        # Clear current list
        self.app_listbox.delete(0, tk.END)
        self.app_instances.clear()
        
        # Filter and add available applications
        available_count = 0
        unavailable_count = 0
        
        for app in APPLICATION_INSTANCES:
            is_available = app.is_available()
            
            if is_available:
                # Add available app to list
                display_text = f"{app.icon}  {app.name}"
                self.app_listbox.insert(tk.END, display_text)
                self.app_instances.append(app)
                available_count += 1
            else:
                unavailable_count += 1
        
        # Update status
        if available_count == 0:
            self.status_label.config(text="⚠️  No approved applications found on this device")
            self.launch_btn.config(state=tk.DISABLED)
        else:
            status_text = f"✓ {available_count} application(s) available"
            if unavailable_count > 0:
                status_text += f" • {unavailable_count} not installed"
            self.status_label.config(text=status_text)
            self.launch_btn.config(state=tk.NORMAL)
    
    def _launch_selected(self):
        """Launch the selected application."""
        selection = self.app_listbox.curselection()
        
        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select an application to launch."
            )
            return
        
        index = selection[0]
        app = self.app_instances[index]
        
        try:
            self.status_label.config(text=f"🚀 Launching {app.name}...")
            self.root.update()
            
            # Launch the application
            app.launch()
            
            self.status_label.config(text=f"✓ {app.name} launched successfully!")
            
        except Exception as e:
            error_msg = f"Failed to launch {app.name}: {str(e)}"
            self.status_label.config(text=f"✗ Error launching {app.name}")
            messagebox.showerror(
                "Launch Error",
                error_msg
            )


def main():
    """Main entry point for the application selector."""
    root = tk.Tk()
    app = AppSelectorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
