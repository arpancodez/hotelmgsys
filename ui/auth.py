"""Authentication UI for login and sign up with professional styling.

This module provides two frames (Sign In and Sign Up) embedded in a
Tkinter Toplevel window. It integrates with the MySQL helper in
`database/db.py` for credential validation and registration.

Notes:
- Replace placeholder database operations in AuthService with real
  implementations as your schema evolves.
- All network/DB calls should ideally be off the main thread for large apps;
  kept simple here for clarity.
"""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional, Callable

# Local database helper
try:
    from database.db import DatabaseHelper
except Exception:  # pragma: no cover - during design/mock
    DatabaseHelper = object  # type: ignore


# ----------------------------- Theme and Styles ----------------------------- #
PRIMARY_BG = "#0F172A"       # slate-900
SURFACE_BG = "#111827"       # gray-900
CARD_BG = "#1F2937"          # gray-800
ACCENT = "#22C55E"           # green-500
ACCENT_HOVER = "#16A34A"     # green-600
TEXT_PRIMARY = "#E5E7EB"     # gray-200
TEXT_MUTED = "#9CA3AF"       # gray-400
ERROR = "#EF4444"            # red-500

FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_SUBTITLE = ("Segoe UI", 11)
FONT_LABEL = ("Segoe UI", 10)
FONT_INPUT = ("Segoe UI", 10)
FONT_BUTTON = ("Segoe UI", 10, "bold")


def apply_styles(root: tk.Misc) -> None:
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except Exception:
        pass

    style.configure("TFrame", background=SURFACE_BG)
    style.configure("Card.TFrame", background=CARD_BG)
    style.configure("Title.TLabel", background=SURFACE_BG, foreground=TEXT_PRIMARY, font=FONT_TITLE)
    style.configure("Muted.TLabel", background=SURFACE_BG, foreground=TEXT_MUTED, font=FONT_SUBTITLE)
    style.configure("TLabel", background=SURFACE_BG, foreground=TEXT_PRIMARY, font=FONT_LABEL)

    style.configure(
        "TEntry",
        fieldbackground="#111827",
        foreground=TEXT_PRIMARY,
        insertcolor=TEXT_PRIMARY,
        bordercolor="#374151",
        lightcolor="#374151",
        darkcolor="#111827",
        borderwidth=1,
        padding=6,
    )

    style.configure(
        "Accent.TButton",
        background=ACCENT,
        foreground="#0B1020",
        font=FONT_BUTTON,
        padding=(12, 8),
        borderwidth=0,
    )
    style.map(
        "Accent.TButton",
        background=[("active", ACCENT_HOVER)],
    )

    style.configure(
        "Ghost.TButton",
        background=CARD_BG,
        foreground=TEXT_PRIMARY,
        font=FONT_BUTTON,
        padding=(10, 6),
        borderwidth=0,
    )
    style.map("Ghost.TButton", background=[("active", "#374151")])


# ---------------------------- Auth Service Layer ---------------------------- #
class AuthService:
    """Service that uses DatabaseHelper to validate and register users.

    Replace bodies with real queries suited to your user table schema.
    """

    def __init__(self, db: Optional[DatabaseHelper] = None):
        self.db = db or DatabaseHelper()

    def ensure_ready(self) -> None:
        try:
            if hasattr(self.db, "connect"):
                self.db.connect()
            # TODO: Create users table if not exists
        except Exception as e:
            print(f"DB init error: {e}")

    def validate_credentials(self, username: str, password: str) -> bool:
        """Validate credentials against DB. TODO: Replace with hashing."""
        try:
            return bool(username and password)
        except Exception as e:
            print(f"Login validation error: {e}")
            return False

    def register_user(self, username: str, password: str) -> bool:
        """Register a new user in DB. Use hashing + uniqueness checks."""
        if not username or not password:
            return False
        try:
            return True
        except Exception as e:
            print(f"Registration error: {e}")
            return False


# ---------------------------- Tkinter UI Windows ---------------------------- #
class AuthWindow:
    """Tkinter Toplevel providing Sign In and Sign Up views with styling."""

    def __init__(self, root: tk.Misc, on_success: Optional[Callable[[str], None]] = None):
        self.root = root
        self.on_success = on_success
        self.window = tk.Toplevel(root)
        self.window.title("Hotel Management System - Authentication")
        self.window.geometry("520x560")
        self.window.configure(bg=PRIMARY_BG)
        self.window.resizable(False, False)
        self.window.grab_set()

        apply_styles(self.window)
        self.auth = AuthService()
        self.auth.ensure_ready()

        container = ttk.Frame(self.window, style="TFrame")
        container.pack(fill="both", expand=True, padx=24, pady=24)

        card = ttk.Frame(container, style="Card.TFrame")
        card.place(relx=0.5, rely=0.5, anchor="center", width=460, height=480)

        header = ttk.Label(card, text="Hotel Management System", style="Title.TLabel")
        header.place(x=24, y=24)
        subtitle = ttk.Label(card, text="Welcome. Please sign in or create an account.", style="Muted.TLabel")
        subtitle.place(x=24, y=64)

        self.btn_signin = ttk.Button(card, text="Sign In", style="Ghost.TButton", command=self.show_signin)
        self.btn_signup = ttk.Button(card, text="Sign Up", style="Ghost.TButton", command=self.show_signup)
        self.btn_signin.place(x=24, y=100, width=100)
        self.btn_signup.place(x=134, y=100, width=100)

        self.frame_signin = ttk.Frame(card, style="Card.TFrame")
        self.frame_signup = ttk.Frame(card, style="Card.TFrame")
        for f in (self.frame_signin, self.frame_signup):
            f.place(x=24, y=140, width=412, height=300)

        self._build_signin(self.frame_signin)
        self._build_signup(self.frame_signup)
        self.show_signin()

    def _labeled_entry(self, parent: tk.Misc, label: str, show: Optional[str] = None) -> ttk.Entry:
        lbl = ttk.Label(parent, text=label)
        lbl.pack(anchor="w", pady=(0, 6))
        ent = ttk.Entry(parent, show=show)
        ent.pack(fill="x", pady=(0, 12))
        return ent

    def _build_signin(self, parent: tk.Misc) -> None:
        self.si_user = self._labeled_entry(parent, "Username")
        self.si_pass = self._labeled_entry(parent, "Password", show="*")
        helper = ttk.Label(parent, text="Use your registered account to continue.", style="Muted.TLabel")
        helper.pack(anchor="w", pady=(0, 10))
        btn = ttk.Button(parent, text="Sign In", style="Accent.TButton", command=self._handle_signin)
        btn.pack(fill="x", pady=(6, 6))

    def _build_signup(self, parent: tk.Misc) -> None:
        self.su_user = self._labeled_entry(parent, "Username")
        self.su_pass = self._labeled_entry(parent, "Password", show="*")
        self.su_confirm = self._labeled_entry(parent, "Confirm Password", show="*")
        note = ttk.Label(parent, text="Password will be stored securely (hashing placeholder).", style="Muted.TLabel")
        note.pack(anchor="w", pady=(0, 10))
        btn = ttk.Button(parent, text="Create Account", style="Accent.TButton", command=self._handle_signup)
        btn.pack(fill="x", pady=(6, 6))

    def show_signin(self) -> None:
        self.frame_signup.lower()
        self.frame_signin.lift()
        self._highlight_tab(active="in")

    def show_signup(self) -> None:
        self.frame_signin.lower()
        self.frame_signup.lift()
        self._highlight_tab(active="up")

    def _highlight_tab(self, active: str) -> None:
        if active == "in":
            self.btn_signin.configure(style="Accent.TButton")
            self.btn_signup.configure(style="Ghost.TButton")
        else:
            self.btn_signin.configure(style="Ghost.TButton")
            self.btn_signup.configure(style="Accent.TButton")

    def _handle_signin(self) -> None:
        username = self.si_user.get().strip()
        password = self.si_pass.get().strip()
        if not username or not password:
            messagebox.showerror("Missing info", "Please enter both username and password.")
            return
        ok = self.auth.validate_credentials(username, password)
        if ok:
            messagebox.showinfo("Welcome", f"Signed in as {username}")
            if self.on_success:
                self.on_success(username)
            self.window.destroy()
        else:
            messagebox.showerror("Authentication failed", "Invalid username or password.")

    def _handle_signup(self) -> None:
        username = self.su_user.get().strip()
        password = self.su_pass.get().strip()
        confirm = self.su_confirm.get().strip()
        if not username or not password:
            messagebox.showerror("Missing info", "Please fill all required fields.")
            return
        if password != confirm:
            messagebox.showerror("Mismatch", "Passwords do not match.")
            return
        created = self.auth.register_user(username, password)
        if created:
            messagebox.showinfo("Success", "Account created. You can now sign in.")
            self.show_signin()
        else:
            messagebox.showerror("Could not create account", "Username may already exist or server error.")


def open_auth_window(root: tk.Misc, on_success: Optional[Callable[[str], None]] = None) -> AuthWindow:
    return AuthWindow(root, on_success=on_success)


if __name__ == "__main__":
    app = tk.Tk()
    app.withdraw()

    def _demo_success(user: str) -> None:
        print("Logged in as:", user)

    open_auth_window(app, on_success=_demo_success)
    app.mainloop()
