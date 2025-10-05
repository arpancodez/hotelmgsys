"""Dashboard UI module for main application window."""

import tkinter as tk
from tkinter import ttk

class Dashboard:
    """Main dashboard window with professional UI."""
    
    def __init__(self, root):
        """Initialize dashboard window."""
        self.window = tk.Toplevel(root)
        self.window.title("Hotel Management System - Dashboard")
        self.window.geometry("900x600")
        self.window.configure(bg="#f0f0f0")
        
        # Create UI elements
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout UI widgets."""
        # Header
        header = tk.Frame(self.window, bg="#2196F3", height=80)
        header.pack(fill=tk.X)
        
        title = tk.Label(header, text="Hotel Management Dashboard",
                        font=("Helvetica", 24, "bold"),
                        bg="#2196F3", fg="white")
        title.pack(pady=20)
        
        # Logout button
        logout_btn = tk.Button(self.window, text="Logout",
                              command=self.logout, bg="#f44336", fg="white")
        logout_btn.place(x=800, y=20)
    
    def logout(self):
        """Handle logout action."""
        self.window.destroy()
