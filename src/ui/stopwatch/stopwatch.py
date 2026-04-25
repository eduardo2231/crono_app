import customtkinter as ctk
from PIL import Image
from pathlib import Path
from src.logic.buttons import Button
from src.ui.stopwatch.frames.header import Header
from src.ui.stopwatch.frames.sidebar import Sidebar
from src.ui.stopwatch.frames.content import Content

BASE_DIR = Path(__file__).resolve().parent.parent.parent
icon_path = BASE_DIR / "assets" / "favicon.ico"

class App(ctk.CTk):
    """Ui of the system"""
    def __init__(self):
        super().__init__()

        if icon_path.exists():
            self.iconbitmap(str(icon_path))

        self.geometry('1200x800')
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=0)

        button = Button(self)

        # Display do tempo
        self.label_tempo = ctk.CTkLabel(
            self,
            text="00:00:00.0",
            font=ctk.CTkFont(family="Terminal",
                             size=48,
                             weight="bold")
        )
        self.label_tempo.grid(row=1, column=1)

        img_menu = ctk.CTkImage(
            light_image=Image.open(BASE_DIR / "assets" / "menu" / "menu.png" ),
            dark_image=Image.open(BASE_DIR / "assets" / "menu" / "menu.png" ),
            size=(24, 24)
        )

        self.options = ctk.CTkButton(self, image=img_menu,
                                     text='',
                                     fg_color="transparent",
                                     hover_color="#3a3a3a",
                                     width=20,
                                     height=20,
                                     )

        self.options.grid(row=0, column=0, padx=10, pady=10)


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    app = App()
    app.mainloop()