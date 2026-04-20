import customtkinter as ctk
from pathlib import Path

ctk.set_appearance_mode("dark")
BASE_DIR = Path(__file__).resolve().parent.parent
icon_path = BASE_DIR / "assets" / "favicon.ico"

class App(ctk.CTk):
    """Ui of the system"""
    def __init__(self):
        super().__init__()

        icon_path = BASE_DIR / "assets" / "favicon.ico"
        if icon_path.exists():
            self.iconbitmap(str(icon_path))

        self.geometry('1200x800')
        self.resizable(False, False)

        # Display do tempo
        self.label_tempo = ctk.CTkLabel(
            self, text="00:00:00.0",
            font=ctk.CTkFont(size=48, weight="bold")
        )
        self.label_tempo.grid(row=0, column=0)
        self.grid_columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()