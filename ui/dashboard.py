"""Dashboard UI module for main application window with professional styling.

Provides a comprehensive hotel management dashboard with navigation to:
- Room Management
- Bookings
- Guests
- Staff
- Billing
- Reports
- Logout

Matches the professional dark theme from auth.py.
"""
from __future__ import annotations
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional, Callable

# ----------------------------- Theme and Styles ----------------------------- #
PRIMARY_BG = "#0F172A"       # slate-900
SURFACE_BG = "#111827"       # gray-900
CARD_BG = "#1F2937"          # gray-800
ACCENT = "#22C55E"           # green-500
ACCENT_HOVER = "#16A34A"     # green-600
DANGER = "#EF4444"           # red-500
DANGER_HOVER = "#DC2626"     # red-600
TEXT_PRIMARY = "#E5E7EB"     # gray-200
TEXT_MUTED = "#9CA3AF"       # gray-400

FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_HEADING = ("Segoe UI", 16, "bold")
FONT_LABEL = ("Segoe UI", 10)
FONT_BUTTON = ("Segoe UI", 11, "bold")


def apply_dashboard_styles(root: tk.Misc) -> None:
    """Apply consistent TTK styling for dashboard."""
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except Exception:
        pass

    # Frame styles
    style.configure("TFrame", background=SURFACE_BG)
    style.configure("Card.TFrame", background=CARD_BG)
    style.configure("Header.TFrame", background=PRIMARY_BG)

    # Label styles
    style.configure(
        "Title.TLabel",
        background=PRIMARY_BG,
        foreground=TEXT_PRIMARY,
        font=FONT_TITLE,
    )
    style.configure(
        "Heading.TLabel",
        background=SURFACE_BG,
        foreground=TEXT_PRIMARY,
        font=FONT_HEADING,
    )
    style.configure(
        "Info.TLabel",
        background=SURFACE_BG,
        foreground=TEXT_MUTED,
        font=FONT_LABEL,
    )

    # Button styles
    style.configure(
        "Nav.TButton",
        background=CARD_BG,
        foreground=TEXT_PRIMARY,
        font=FONT_BUTTON,
        padding=(20, 15),
        borderwidth=0,
    )
    style.map(
        "Nav.TButton",
        background=[("active", "#374151")],
    )

    style.configure(
        "Accent.TButton",
        background=ACCENT,
        foreground="#0B1020",
        font=FONT_BUTTON,
        padding=(16, 10),
        borderwidth=0,
    )
    style.map(
        "Accent.TButton",
        background=[("active", ACCENT_HOVER)],
    )

    style.configure(
        "Danger.TButton",
        background=DANGER,
        foreground="white",
        font=FONT_BUTTON,
        padding=(12, 8),
        borderwidth=0,
    )
    style.map(
        "Danger.TButton",
        background=[("active", DANGER_HOVER)],
    )


# ---------------------------- Dashboard Window ------------------------------ #
class Dashboard:
    """Main dashboard window with professional UI and navigation."""

    def __init__(
        self,
        root: tk.Misc,
        username: str = "User",
        on_logout: Optional[Callable[[], None]] = None,
    ):
        """Initialize dashboard window.

        Args:
            root: Parent Tkinter widget
            username: Logged-in user's name for display
            on_logout: Callback to execute on logout (before window closes)
        """
        self.root = root
        self.username = username
        self.on_logout = on_logout

        # Create toplevel window
        self.window = tk.Toplevel(root)
        self.window.title("Hotel Management System - Dashboard")
        self.window.geometry("1000x700")
        self.window.configure(bg=SURFACE_BG)
        self.window.resizable(True, True)

        # Apply styling
        apply_dashboard_styles(self.window)

        # Build UI
        self._create_header()
        self._create_welcome_section()
        self._create_navigation_grid()

    def _create_header(self) -> None:
        """Create top header bar with title and logout button."""
        header_frame = ttk.Frame(self.window, style="Header.TFrame", height=80)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)

        # Title
        title_label = ttk.Label(
            header_frame,
            text="Hotel Management System",
            style="Title.TLabel",
        )
        title_label.pack(side=tk.LEFT, padx=30, pady=20)

        # Logout button
        logout_btn = ttk.Button(
            header_frame,
            text="Logout",
            style="Danger.TButton",
            command=self._handle_logout,
        )
        logout_btn.pack(side=tk.RIGHT, padx=30, pady=20)

    def _create_welcome_section(self) -> None:
        """Create welcome message area below header."""
        welcome_frame = ttk.Frame(self.window, style="TFrame")
        welcome_frame.pack(fill=tk.X, padx=40, pady=(30, 20))

        heading = ttk.Label(
            welcome_frame,
            text=f"Welcome, {self.username}!",
            style="Heading.TLabel",
        )
        heading.pack(anchor="w")

        info = ttk.Label(
            welcome_frame,
            text="Select an option below to manage your hotel operations.",
            style="Info.TLabel",
        )
        info.pack(anchor="w", pady=(8, 0))

    def _create_navigation_grid(self) -> None:
        """Create grid of navigation buttons for main features."""
        # Container for navigation buttons
        nav_container = ttk.Frame(self.window, style="TFrame")
        nav_container.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

        # Define navigation items (label, command)
        nav_items = [
            ("Room Management", self._open_room_management),
            ("Bookings", self._open_bookings),
            ("Guests", self._open_guests),
            ("Staff", self._open_staff),
            ("Billing", self._open_billing),
            ("Reports", self._open_reports),
        ]

        # Create 3x2 grid of navigation cards
        for idx, (label, command) in enumerate(nav_items):
            row = idx // 3
            col = idx % 3

            # Card frame for each button
            card = ttk.Frame(nav_container, style="Card.TFrame")
            card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

            # Navigation button
            btn = ttk.Button(
                card,
                text=label,
                style="Nav.TButton",
                command=command,
            )
            btn.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

        # Configure grid weights for responsiveness
        for i in range(3):
            nav_container.columnconfigure(i, weight=1, uniform="nav_col")
        for i in range(2):
            nav_container.rowconfigure(i, weight=1, uniform="nav_row")

    # -------------------------- Navigation Handlers ------------------------- #

    def _open_room_management(self) -> None:
        """Open Room Management module (placeholder)."""
        print("[Dashboard] Room Management - Not yet implemented")
        messagebox.showinfo(
            "Room Management",
            "Room Management module is under development.\nThis will allow you to:"
            "\n• Add/edit/delete rooms\n• View room status\n• Set room rates",
        )

    def _open_bookings(self) -> None:
        """Open Bookings module (placeholder)."""
        print("[Dashboard] Bookings - Not yet implemented")
        messagebox.showinfo(
            "Bookings",
            "Bookings module is under development.\nThis will allow you to:"
            "\n• Create new bookings\n• View existing bookings\n• Modify/cancel bookings",
        )

    def _open_guests(self) -> None:
        """Open Guests module (placeholder)."""
        print("[Dashboard] Guests - Not yet implemented")
        messagebox.showinfo(
            "Guests",
            "Guests module is under development.\nThis will allow you to:"
            "\n• Manage guest profiles\n• View guest history\n• Track preferences",
        )

    def _open_staff(self) -> None:
        """Open Staff module (placeholder)."""
        print("[Dashboard] Staff - Not yet implemented")
        messagebox.showinfo(
            "Staff",
            "Staff module is under development.\nThis will allow you to:"
            "\n• Manage staff records\n• Assign roles\n• Track schedules",
        )

    def _open_billing(self) -> None:
        """Open Billing module (placeholder)."""
        print("[Dashboard] Billing - Not yet implemented")
        messagebox.showinfo(
            "Billing",
            "Billing module is under development.\nThis will allow you to:"
            "\n• Generate invoices\n• Process payments\n• View transaction history",
        )

    def _open_reports(self) -> None:
        """Open Reports module (placeholder)."""
        print("[Dashboard] Reports - Not yet implemented")
        messagebox.showinfo(
            "Reports",
            "Reports module is under development.\nThis will allow you to:"
            "\n• Generate occupancy reports\n• View revenue analytics\n• Export data",
        )

    def _handle_logout(self) -> None:
        """Handle logout action - calls callback and closes window."""
        print(f"[Dashboard] User '{self.username}' logging out")
        if self.on_logout:
            self.on_logout()
        self.window.destroy()


# ------------------------------ Public API ---------------------------------- #
def open_dashboard(
    root: tk.Misc,
    username: str = "User",
    on_logout: Optional[Callable[[], None]] = None,
) -> Dashboard:
    """Open the main dashboard window.

    Args:
        root: Parent Tkinter widget
        username: Logged-in user's name
        on_logout: Callback function to execute on logout

    Returns:
        Dashboard instance
    """
    return Dashboard(root, username=username, on_logout=on_logout)


if __name__ == "__main__":
    # Demo/testing
    app = tk.Tk()
    app.withdraw()

    def _demo_logout() -> None:
        print("Logout callback triggered")
        app.quit()

    open_dashboard(app, username="Demo User", on_logout=_demo_logout)
    app.mainloop()
