import customtkinter as ctk
from PIL import Image
from pathlib import Path
from src.logic.buttons import Button
from src.ui.stopwatch.frames.header import Header
from src.ui.stopwatch.frames.content import Content
from src.ui.stopwatch.frames.sidebar import Sidebar
from src.ui.timer.frames.content import Content as TimerContent
from src.ui.analysis.frames.content import Content as AnalysisContent

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
        self.title("Cronometro")

        # -------------- Header --------------
        self.header = Header(master=self)
        self.header.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # -------------- Content --------------
        self.main_area = ctk.CTkFrame(master=self)
        self.main_area.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.main_area.grid_rowconfigure(0, weight=1)
        self.main_area.grid_columnconfigure(0, weight=1)

        self.screens = {}

        self.screens["stopwatch"] = Content(master=self.main_area)
        self.screens["timer"] = TimerContent(master=self.main_area)
        self.screens["analysis"] = AnalysisContent(master=self.main_area)

        for screen in self.screens.values():
            screen.grid(row=0, column=0, sticky="nsew")
        self.show_screen("stopwatch")

        # -------------- Sidebar --------------
        self.sidebar = Sidebar(master=self)

    def toggle_sidebar(self):
        if self.sidebar.winfo_ismapped():
            self.sidebar.place_forget()
        else:
            self.sidebar.place(x=20, y=20)
            self.sidebar.lift()

    def show_screen(self, name: str):
        self.screens[name].tkraise()


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    app = App()
    app.mainloop()