import customtkinter as ctk

class Button():
    def __init__(self, app, *args):
        self.master = app
        self.app = args[0] if args else ''

    def button_close(self):
        self.master.destroy()
