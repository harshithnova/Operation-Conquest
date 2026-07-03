# ==========================================================
# Operation Conquest
# Main Entry Point
# ==========================================================

import tkinter as tk

# Import Welcome Screen
from screens.welcome_screen import WelcomeScreen


def main():
    """
    Starts the Operation Conquest application.
    """

    root = tk.Tk()

    # Window Settings
    root.title("Operation Conquest")
    root.geometry("1200x1000")
    root.minsize(1000, 700)

    # Launch first screen
    WelcomeScreen(root)

    root.mainloop()


if __name__ == "__main__":
    main()