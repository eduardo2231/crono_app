import customtkinter as ctk
from PIL import Image
from pathlib import Path
from src.logic.buttons import Button

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
class Header(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_propagate(False)
        self.configure(width=1160,
                       height=73,
                       border_color='black',
                       border_width=2
                       )
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.label = ctk.CTkLabel(self, text='')
        self.label.grid(row=0,
                        column=0,
                        padx=20,
                        pady=15,
                        )

        button = Button(master, self)

        img_menu = ctk.CTkImage(
            light_image=Image.open(BASE_DIR / "assets" / "menu" / "menu.png"),
            dark_image=Image.open(BASE_DIR / "assets" / "menu" / "menu.png"),
            size=(24, 24)
        )

        # ----------------- Menu Button -----------------
        self.options = ctk.CTkButton(self, image=img_menu,
                                     text='',
                                     fg_color="transparent",
                                     hover_color="#3a3a3a",
                                     width=20,
                                     height=20,
                                     command=self.master.toggle_sidebar
                                     )

        self.options.grid(row=0, column=0, padx=20, pady=20, sticky='w')

        # ----------------- App Name -----------------
        self.appname = ctk.CTkLabel(self,
                                   text='..\CRONOMETRO',
                                   font=ctk.CTkFont(family="Terminal",
                                                    size=50,
                                                    weight="bold"),
                                   width=50,
                                   height=50,
                                   anchor='center',
                                   )
        self.appname.grid(row=0, column=1, sticky="e", padx=10, pady=10)

