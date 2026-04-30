import customtkinter as ctk
from PIL import Image
from pathlib import Path
from src.logic.buttons import Button

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Content(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_propagate(False)
        self.configure(width=1160,
                       height=640,
                       border_color='black',
                       border_width=2
                       )


        self.label = ctk.CTkLabel(self, text='')
        self.label.grid(row=1, column=0, padx=20, pady=20)

        # size of rows
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)

        # size of columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)