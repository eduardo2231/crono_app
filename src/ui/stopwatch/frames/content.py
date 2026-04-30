import customtkinter as ctk
import tkinter as tk
from PIL import Image
from pathlib import Path
from src.logic.buttons import Button
import threading
import time
from src.logic.timer_logic import TimerLogic

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Content(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Estado da contagem regressiva
        self.logic = TimerLogic()
        self._job = None
        self._timer_run_id = 0

        # Configuracao base do frame principal
        self.grid_propagate(False)
        self.configure(width=1160,
                       height=640,
                       border_color='black',
                       border_width=2
                       )

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Modal interno para definir o tempo HH:MM:SS
        self.selector_frame = ctk.CTkFrame(self,
                                           width=460,
                                           height=220,
                                           corner_radius=12,
                                           border_width=2,
                                           border_color="#2f2f2f")
        self.selector_frame.grid_propagate(False)
        self.selector_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.horas = 0
        self.minutos = 0
        self.segundos = 0

        # Titulos do modal
        self.selector_title = ctk.CTkLabel(self.selector_frame,
                                           text="Definir tempo",
                                           font=ctk.CTkFont(family="Terminal",
                                                            weight="bold"))
        self.selector_title.grid(row=0, column=0, columnspan=3, pady=(16, 8))

        self.label_h = ctk.CTkLabel(self.selector_frame, text="Horas", font=ctk.CTkFont(family="Terminal",
                             weight="bold"))
        self.label_h.grid(row=1, column=0, pady=(0, 4))

        self.label_m = ctk.CTkLabel(self.selector_frame, text="Minutos", font=ctk.CTkFont(family="Terminal",
                             weight="bold"))
        self.label_m.grid(row=1, column=1, pady=(0, 4))
        
        self.label_s = ctk.CTkLabel(self.selector_frame, text="Segundos", font=ctk.CTkFont(family="Terminal",
                             weight="bold"))
        self.label_s.grid(row=1, column=2, pady=(0, 4))

        # Botoes que abrem lista rolavel para escolher valores
        self.horas_btn = ctk.CTkButton(self.selector_frame,
                                       text="00",
                                       font=ctk.CTkFont(family="Terminal",
                                                        weight="bold"),
                                       width=90,
                                       command=lambda: self._abrir_lista_tempo(self.horas_btn, "h", 100))
        self.horas_btn.grid(row=2, column=0, padx=8, pady=4)

        self.min_btn = ctk.CTkButton(self.selector_frame,
                                     text="00",
                                     font=ctk.CTkFont(family="Terminal",
                                                      weight="bold"),
                                     width=90,
                                     command=lambda: self._abrir_lista_tempo(self.min_btn, "m", 60))
        self.min_btn.grid(row=2, column=1, padx=8, pady=4)

        self.seg_btn = ctk.CTkButton(self.selector_frame,
                                     text="00",
                                     font=ctk.CTkFont(family="Terminal",
                                                      weight="bold"),
                                     width=90,
                                     command=lambda: self._abrir_lista_tempo(self.seg_btn, "s", 60))
        self.seg_btn.grid(row=2, column=2, padx=8, pady=4)

        # Acoes do modal
        self.apply_time_btn = ctk.CTkButton(self.selector_frame,
                                            text="Aplicar",
                                            border_width=2,
                                            border_color="#2f2f2f",
                                            fg_color="transparent",
                                            font=ctk.CTkFont(family="Terminal",
                                                             weight="bold"),
                                            width=110,
                                            command=self.aplicar_tempo)
        self.apply_time_btn.grid(row=3, column=1, pady=(18, 8))

        self.close_selector_btn = ctk.CTkButton(self.selector_frame,
                                                text="Fechar",
                                                font=ctk.CTkFont(family="Terminal",
                                                                 weight="bold"),
                                                fg_color="transparent",
                                                border_width=2,
                                                border_color="#2f2f2f",
                                                width=110,
                                                command=self.fechar_seletor)
        self.close_selector_btn.grid(row=3, column=2, pady=(18, 8), padx=(0, 8))

        # Display principal do timer
        self.label_tempo = ctk.CTkLabel(
            self,
            text_color='yellow',
            text="00:00:00",
            font=ctk.CTkFont(family="Terminal",
                             size=120,
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
                                   hover_color="#3a3a3a",
                                   command=self.toggle,
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
                                   hover_color="#3a3a3a",
                                   command=self.resetar_timer
                                   )
        self.reset.grid(row=1, column=2, padx=10, pady=10)

        # ----------------- Insert Button -----------------
        self.insert = ctk.CTkButton(self.buttons_frame,
                                   text='INSERT',
                                   font=ctk.CTkFont(family="Terminal",
                                                    size=40,
                                                    weight="bold"),
                                   fg_color="#3a3000",
                                   width=60,
                                   height=60,
                                   anchor='center',
                                   hover_color="#3a3a3a",
                                   command=self.abrir_seletor_tempo
                                   )
        self.insert.grid(row=1, column=1, padx=10, pady=10)
        self._atualizar_estado_start()
        self._lista_popup = None

    # Abre o modal de configuracao de tempo
    def abrir_seletor_tempo(self):
        self.selector_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.selector_frame.lift()

    # Fecha o modal e fecha a lista rolavel (se existir)
    def fechar_seletor(self):
        self._fechar_lista_tempo()
        self.selector_frame.place_forget()

    # Aplica os valores escolhidos no timer
    def aplicar_tempo(self):
        self.configurar_tempo()
        self.fechar_seletor()

    # Converte HH:MM:SS para segundos e atualiza o display
    def configurar_tempo(self):
        h = self.horas
        m = self.minutos
        s = self.segundos
        self.logic.definir_tempo(h, m, s)
        self.label_tempo.configure(text=self.logic.formatar_tempo(self.logic.tempo_restante))
        self._atualizar_estado_start()

    # Inicia, pausa ou continua o timer
    def toggle(self):
        if not self.logic.rodando:
            if self.logic.tempo_restante <= 0:
                self.configurar_tempo()
            if self.logic.tempo_restante <= 0:
                return
            self._timer_run_id += 1
            self.logic.iniciar()
            self.start.configure(text="PAUSE")
            self.contar(self._timer_run_id)
        else:
            self._timer_run_id += 1
            self.logic.pausar()
            self.start.configure(text="CONTINUE")

    # Loop da contagem regressiva
    def contar(self, run_id):
        if run_id != self._timer_run_id or not self.logic.rodando:
            return

        self.logic.tick()
        self.label_tempo.configure(text=self.logic.formatar_tempo(self.logic.tempo_restante))

        if self.logic.tempo_restante > 0:
            self._job = self.after(1000, lambda: self.contar(run_id))
        else:
            self.start.configure(text="START")

    # Reseta o timer para o ultimo tempo aplicado
    def resetar_timer(self):
        self._timer_run_id += 1
        self.logic.pausar()
        if self._job is not None:
            self.after_cancel(self._job)
            self._job = None
        self.logic.resetar()
        self.label_tempo.configure(text=self.logic.formatar_tempo(self.logic.tempo_restante))
        self.start.configure(text="START")
        self._atualizar_estado_start()

    # Habilita START somente quando houver tempo > 0
    def _atualizar_estado_start(self):
        tem_tempo = self.logic.tempo_restante > 0 or self.logic.duracao_total > 0
        if tem_tempo:
            self.start.configure(state="normal")
        else:
            self.start.configure(state="disabled")

    # Abre lista rolavel com limite de altura (abre para cima)
    def _abrir_lista_tempo(self, anchor_widget, unidade, limite):
        self._fechar_lista_tempo()
        popup = ctk.CTkToplevel(self)
        popup.overrideredirect(True)
        popup.attributes("-topmost", True)
        popup.configure(fg_color="#2a2a2a")
        popup.geometry("110x180")

        x = anchor_widget.winfo_rootx()
        y = max(0, anchor_widget.winfo_rooty() - 184)
        popup.geometry(f"+{x}+{y}")

        listbox = tk.Listbox(
            popup,
            height=8,  # limite de itens visiveis
            exportselection=False,
            bg="#2a2a2a",
            fg="#f0f0f0",
            selectbackground="#3a6ea5",
            highlightthickness=0,
            relief="flat"
        )
        listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(popup, orient="vertical", command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        listbox.configure(yscrollcommand=scrollbar.set)

        for i in range(limite):
            listbox.insert("end", f"{i:02}")

        atual = self.horas if unidade == "h" else self.minutos if unidade == "m" else self.segundos
        listbox.selection_set(atual)
        listbox.see(atual)

        def selecionar(_event=None):
            selecionado = listbox.curselection()
            if not selecionado:
                return
            valor = selecionado[0]
            if unidade == "h":
                self.horas = valor
                self.horas_btn.configure(text=f"{self.horas:02}")
            elif unidade == "m":
                self.minutos = valor
                self.min_btn.configure(text=f"{self.minutos:02}")
            else:
                self.segundos = valor
                self.seg_btn.configure(text=f"{self.segundos:02}")
            self._fechar_lista_tempo()

        listbox.bind("<ButtonRelease-1>", selecionar)
        listbox.bind("<Return>", selecionar)

        self._lista_popup = popup

    # Fecha popup de selecao se estiver aberto
    def _fechar_lista_tempo(self):
        if self._lista_popup is not None and self._lista_popup.winfo_exists():
            self._lista_popup.destroy()
        self._lista_popup = None