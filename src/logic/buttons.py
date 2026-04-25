import customtkinter as ctk


class Button():
    def __init__(self, app):
        self.app = app

    def button_close(self):
        self.app.destroy()
