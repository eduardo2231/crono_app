import customtkinter as ctk
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


        self.grid_propagate(False)
        self.configure(width=145,
                       height=752,
                       border_color='black',
                       border_width=2)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)

        # ----------------- Back Button -----------------
        img_menu = ctk.CTkImage(
            light_image=Image.open(BASE_DIR / "assets" / "menu" / "back.png"),
            dark_image=Image.open(BASE_DIR / "assets" / "menu" / "back.png"),
            size=(24, 24)
        )
        self.back_btn = ctk.CTkButton(self, image=img_menu,
                                      text='',
                                      fg_color="transparent",
                                      hover_color="#3a3a3a",
                                      width=20,
                                      height=20,
                                      command=self.master.toggle_sidebar
                                      )
        self.back_btn.grid(row=0, column=1, padx=20, pady=20, sticky="e")

        # ----------------- Options -----------------
        self.stopwatch_btn = ctk.CTkButton(self, text="cronometro",
                                      font=ctk.CTkFont(family="Terminal",
                                                       size=20,
                                                       weight="bold"),
                                      fg_color="#3A3F45",
                                      hover_color="#3a3a3a",
                                      width=10,
                                      height=40,
                                      command=lambda: self.master.show_screen("stopwatch")
                                      )
        self.stopwatch_btn.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        self.timer_btn = ctk.CTkButton(self, text="timer     ",
                                           font=ctk.CTkFont(family="Terminal",
                                                            size=20,
                                                            weight="bold"),
                                           fg_color="#3A3F45",
                                           hover_color="#3a3a3a",
                                           width=10,
                                           height=40,
                                           command=lambda: self.master.show_screen("timer")
                                           )

        self.timer_btn.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        self.analysis_btn = ctk.CTkButton(self, text="analysis  ",
                                       font=ctk.CTkFont(family="Terminal",
                                                        size=20,
                                                        weight="bold"),
                                       fg_color="#3A3F45",
                                       hover_color="#3a3a3a",
                                       width=10,
                                       height=40,
                                       command=lambda: self.master.show_screen("analysis")
                                       )

        self.analysis_btn.grid(row=3, column=1, padx=10, pady=10, sticky="e")






