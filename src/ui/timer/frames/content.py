import customtkinter as ctk
from PIL import Image
from pathlib import Path
from src.logic.buttons import Button
import threading
import time
from src.logic.stopwatch_logic import StopwatchLogic

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Content(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.logic = StopwatchLogic()

        self.grid_propagate(False)
        self.configure(width=1160,
                       height=640,
                       border_color='black',
                       border_width=2
                       )


        # Layout centralizado
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # ----------------- Time Button -----------------
        self.label_tempo = ctk.CTkLabel(
            self,
            text_color='yellow',
            text="00:00:00",
            font=ctk.CTkFont(family="Terminal",
                             size=80,
                             weight="bold")
        )
        self.label_tempo.grid(row=0, column=0, columnspan=3, padx=20, pady=(120, 40))

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.grid(row=1, column=0, columnspan=3, pady=(10, 80))

        # ----------------- Start Button -----------------
        self.start = ctk.CTkButton(self.buttons_frame,
                                   text='START',
                                   font=ctk.CTkFont(family="Terminal",
                                                    size=40,
                                                    weight="bold"),
                                   fg_color="#1a3a2a",
                                   width=60,
                                   height=60,
                                   anchor='center',
                                   command=self.toggle
                                   )
        self.start.grid(row=1, column=0, padx=10, pady=10)

        # ----------------- Reset Button -----------------
        self.reset = ctk.CTkButton(self.buttons_frame,
                                   text='RESET',
                                   font=ctk.CTkFont(family="Terminal",
                                                    size=40,
                                                    weight="bold"),
                                   fg_color="#3a1a1a",
                                   width=60,
                                   height=60,
                                   anchor='center',
                                   command=self.resetar_cronometro
                                   )
        self.reset.grid(row=1, column=2, padx=10, pady=10)

        # ----------------- Save Button -----------------
        self.save = ctk.CTkButton(self.buttons_frame,
                                   text='SAVE',
                                   font=ctk.CTkFont(family="Terminal",
                                                    size=40,
                                                    weight="bold"),
                                   fg_color="#1a2a3a",
                                   width=60,
                                   height=60,
                                   anchor='center',
                                   command=self.inserir_volta
                                   )
        self.save.grid(row=1, column=1, padx=10, pady=10)

    def toggle(self):
        if not self.logic.rodando:
            self.logic.iniciar_ou_continuar()
            self.start.configure(text="PAUSE", fg_color="#2a3f5a")
            threading.Thread(target=self.atualizar, daemon=True).start()
        else:
            self.logic.pausar()
            self.start.configure(text="CONTINUE")

    def resetar_cronometro(self):
        self.logic.resetar()
        self.label_tempo.configure(text="00:00:00")
        self.start.configure(text="START")

    def inserir_volta(self):
        volta = self.logic.inserir_volta()
        print(f"Volta {len(self.logic.voltas)}: {volta}")

    def atualizar(self):
        while self.logic.rodando:
            segundos = self.logic.atualizar_tempo()
            self.label_tempo.configure(text=self.logic.formatar_tempo(segundos))
            time.sleep(0.05)