"""Main entry point for Hotel Management System."""

import tkinter as tk
from ui.auth import LoginWindow

def main():
    """Initialize and run the hotel management system."""
    root = tk.Tk()
    root.withdraw()  # Hide main window
    LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
