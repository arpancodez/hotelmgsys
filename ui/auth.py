"""Authentication UI module for login and signup windows."""

import tkinter as tk
from tkinter import ttk, messagebox

class LoginWindow:
    """Login window with professional UI."""
    
    def __init__(self, root):
        """Initialize login window."""
        self.window = tk.Toplevel(root)
        self.window.title("Hotel Management System - Login")
        self.window.geometry("400x500")
        self.window.configure(bg="#f0f0f0")
        
        # Create UI elements
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout UI widgets."""
        # Title
        title_label = tk.Label(self.window, text="Hotel Management System",
                              font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        title_label.pack(pady=30)
        
        # Username
        tk.Label(self.window, text="Username:", bg="#f0f0f0").pack()
        self.username_entry = tk.Entry(self.window, width=30)
        self.username_entry.pack(pady=5)
        
        # Password  
        tk.Label(self.window, text="Password:", bg="#f0f0f0").pack()
        self.password_entry = tk.Entry(self.window, width=30, show="*")
        self.password_entry.pack(pady=5)
        
        # Login button
        login_btn = tk.Button(self.window, text="Login", command=self.login,
                             width=20, bg="#4CAF50", fg="white")
        login_btn.pack(pady=20)
    
    def login(self):
        """Handle login action."""
        # Placeholder for login logic
        messagebox.showinfo("Login", "Login functionality to be implemented")
