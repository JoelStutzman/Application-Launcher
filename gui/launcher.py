"""
GUI Application Launcher class.
"""
import tkinter as tk
from tkinter import messagebox
from backend import programs


class ApplicationLauncher:
    """GUI Application Launcher"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Application Launcher")
        self.root.geometry("700x800")
        self.root.configure(bg='#2b2b2b')
        
        # Make window resizable
        self.root.resizable(True, True)
        
        # Get available programs
        self.program_dict = programs.PROGRAMS
        
        # Count available apps
        self.total_apps = len(self.program_dict)
        self.available_apps = sum(1 for _, _, is_available in self.program_dict.values() if is_available)
        
        # Store all button frames for filtering
        self.app_buttons = {}
        
        # Setup keyboard shortcuts
        self.root.bind('<Escape>', lambda e: self.exit_app())
        self.root.bind('<Control-f>', lambda e: self.search_entry.focus())
        self.root.bind('<Command-f>', lambda e: self.search_entry.focus())
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        """Create all UI widgets"""
        
        # Title Frame
        title_frame = tk.Frame(self.root, bg='#1e1e1e', height=80)
        title_frame.pack(fill=tk.X, padx=0, pady=0)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="🚀 Application Launcher",
            font=('Helvetica', 24, 'bold'),
            bg='#1e1e1e',
            fg='#ffffff'
        )
        title_label.pack(pady=20)
        
        # Instructions
        instructions_label = tk.Label(
            self.root,
            text="Select an application to launch:",
            font=('Helvetica', 12),
            bg='#2b2b2b',
            fg='#cccccc'
        )
        instructions_label.pack(pady=(20, 10))
        
        # Search Frame
        search_frame = tk.Frame(self.root, bg='#2b2b2b')
        search_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
        
        search_icon = tk.Label(
            search_frame,
            text="🔍",
            font=('Helvetica', 16),
            bg='#2b2b2b',
            fg='#cccccc'
        )
        search_icon.pack(side=tk.LEFT, padx=(0, 10))
        
        self.search_var = tk.StringVar()
        
        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=('Helvetica', 12),
            bg='#3c3c3c',
            fg='#ffffff',
            insertbackground='white',
            relief=tk.FLAT,
            bd=0
        )
        self.search_entry.pack(fill=tk.X, expand=True, ipady=8, side=tk.LEFT)
        
        # Clear button
        clear_btn = tk.Button(
            search_frame,
            text="✕",
            font=('Helvetica', 14),
            bg='#3c3c3c',
            fg='#888888',
            activebackground='#505050',
            activeforeground='#ffffff',
            relief=tk.FLAT,
            cursor='hand2',
            padx=10,
            command=self.clear_search
        )
        clear_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # Add placeholder behavior
        self.search_entry.insert(0, "Search applications...")
        self.search_entry.bind('<FocusIn>', self.on_search_focus_in)
        self.search_entry.bind('<FocusOut>', self.on_search_focus_out)
        self.search_entry.config(fg='#888888')
        
        # Status bar
        status_frame = tk.Frame(self.root, bg='#1e1e1e')
        status_frame.pack(fill=tk.X, padx=0, pady=(0, 5))
        
        self.status_label = tk.Label(
            status_frame,
            text=f"📊 {self.available_apps} of {self.total_apps} apps available",
            font=('Helvetica', 10),
            bg='#1e1e1e',
            fg='#888888',
            pady=5
        )
        self.status_label.pack()
        
        # Now setup the search trace after status_label exists
        self.search_var.trace('w', self.filter_apps)
        
        # Create scrollable frame for buttons
        scroll_container = tk.Frame(self.root, bg='#2b2b2b')
        scroll_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create canvas for scrolling
        self.canvas = tk.Canvas(scroll_container, bg='#2b2b2b', highlightthickness=0)
        scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#2b2b2b')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Make scrollable frame match canvas width
        def configure_scrollable_frame(event):
            self.canvas.itemconfig(canvas_window, width=event.width)
        
        self.canvas.bind('<Configure>', configure_scrollable_frame)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)  # Windows/macOS
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)    # Linux
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)    # Linux
        
        # Create custom styled buttons for each application
        for num, (app_name, app_func, is_available) in self.program_dict.items():
            btn_frame = self.create_custom_button(self.scrollable_frame, app_name, app_func, is_available)
            # Remove icon from the search key
            search_key = app_name.split(' ', 1)[1].lower() if ' ' in app_name else app_name.lower()
            self.app_buttons[search_key] = btn_frame
        
        # Bottom Frame for Exit button
        bottom_frame = tk.Frame(self.root, bg='#2b2b2b', height=100)
        bottom_frame.pack(fill=tk.X, padx=20, pady=(10, 20))
        bottom_frame.pack_propagate(False)
        
        # Keyboard shortcuts hint
        shortcuts_label = tk.Label(
            bottom_frame,
            text="Shortcuts: Ctrl/⌘+F (Search) • Esc (Exit)",
            font=('Helvetica', 9),
            bg='#2b2b2b',
            fg='#888888'
        )
        shortcuts_label.pack(pady=(0, 10))
        
        exit_btn = tk.Button(
            bottom_frame,
            text="Exit",
            font=('Helvetica', 12, 'bold'),
            bg='#d13438',
            fg='white',
            activebackground='#a02d30',
            activeforeground='white',
            relief=tk.FLAT,
            cursor='hand2',
            padx=20,
            pady=10,
            command=self.exit_app
        )
        exit_btn.pack(fill=tk.X)
        
        # Hover effect for exit button
        exit_btn.bind('<Enter>', lambda e: exit_btn.config(bg='#a02d30'))
        exit_btn.bind('<Leave>', lambda e: exit_btn.config(bg='#d13438'))
    
    def create_custom_button(self, parent, app_name, app_func, is_available=True):
        """Create a custom styled button using Canvas for better color control"""
        # Create container frame
        btn_frame = tk.Frame(parent, bg='#2b2b2b')
        btn_frame.pack(fill=tk.X, pady=5, padx=5)
        
        # Determine colors based on availability
        if is_available:
            base_color = '#0078d4'
            hover_color = '#005a9e'
        else:
            base_color = '#505050'
            hover_color = '#404040'
        
        # Create canvas for the button
        canvas = tk.Canvas(
            btn_frame,
            height=50,
            bg=base_color,
            highlightthickness=0
        )
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Add text to canvas - use dynamic positioning
        def update_text_position(event=None):
            canvas.delete("text")
            display_text = app_name if is_available else f"{app_name} (Not Installed)"
            canvas.create_text(
                canvas.winfo_width() // 2, 25,
                text=display_text,
                font=('Helvetica', 14, 'bold'),
                fill='white',
                tags="text"
            )
        
        # Bind resize event
        canvas.bind('<Configure>', update_text_position)
        
        # Initial text placement
        canvas.update_idletasks()
        display_text = app_name if is_available else f"{app_name} (Not Installed)"
        canvas.create_text(
            240, 25,
            text=display_text,
            font=('Helvetica', 14, 'bold'),
            fill='white',
            tags="text"
        )
        
        # Bind click event
        def on_click(e):
            if is_available:
                self.launch_app(app_func, app_name)
            else:
                messagebox.showwarning(
                    "App Not Available",
                    f"{app_name.split(' ', 1)[1] if ' ' in app_name else app_name} is not installed on your system."
                )
        
        # Bind hover events
        def on_enter(e):
            canvas.configure(bg=hover_color)
        
        def on_leave(e):
            canvas.configure(bg=base_color)
        
        canvas.bind('<Button-1>', on_click)
        canvas.bind('<Enter>', on_enter)
        canvas.bind('<Leave>', on_leave)
        canvas.config(cursor='hand2')
        
        return btn_frame
    
    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")
    
    def launch_app(self, app_func, app_name):
        """Launch the selected application"""
        try:
            app_func()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch {app_name}:\n{str(e)}")
    
    def exit_app(self):
        """Exit the application"""
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()
    
    def on_search_focus_in(self, event):
        """Handle search entry focus in"""
        if self.search_entry.get() == "Search applications...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg='#ffffff')
    
    def on_search_focus_out(self, event):
        """Handle search entry focus out"""
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search applications...")
            self.search_entry.config(fg='#888888')
    
    def filter_apps(self, *args):
        """Filter applications based on search text"""
        search_text = self.search_var.get().lower()
        
        # Skip filtering if showing placeholder
        if search_text == "search applications...":
            search_text = ""
        
        visible_count = 0
        for app_name, btn_frame in self.app_buttons.items():
            if search_text in app_name:
                btn_frame.pack(fill=tk.X, pady=5, padx=5)
                visible_count += 1
            else:
                btn_frame.pack_forget()
        
        # Update status if searching
        if search_text:
            self.status_label.config(text=f"🔍 Showing {visible_count} of {self.total_apps} apps")
        else:
            self.status_label.config(text=f"📊 {self.available_apps} of {self.total_apps} apps available")
    
    def clear_search(self):
        """Clear the search field"""
        self.search_var.set("")
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, "Search applications...")
        self.search_entry.config(fg='#888888')
        self.root.focus()
