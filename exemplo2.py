import customtkinter as ctk
from datetime import datetime

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("App com Abas")
        self.geometry("400x300")

        # --- Barra de botões (fica sempre visível) ---
        frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_botoes.pack(fill="x", padx=10, pady=(10, 0))

        ctk.CTkButton(
            frame_botoes, text="Relógio",
            command=self.mostrar_relogio
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_botoes, text="Data",
            command=self.mostrar_data
        ).pack(side="left", padx=5)

        # --- Container que vai abrigar as "páginas" ---
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)

        # --- Página: Relógio ---
        self.frame_relogio = ctk.CTkFrame(self.container, fg_color="transparent")
        self.lbl_hora = ctk.CTkLabel(self.frame_relogio, text="", font=("Arial", 48))
        self.lbl_hora.pack(expand=True)

        # --- Página: Data ---
        self.frame_data = ctk.CTkFrame(self.container, fg_color="transparent")
        self.lbl_data = ctk.CTkLabel(self.frame_data, text="", font=("Arial", 24))
        self.lbl_data.pack(expand=True)

        # Mostra a primeira aba por padrão
        self.pagina_atual = None
        self.mostrar_relogio()
        self.atualizar_relogio()

    def trocar_pagina(self, novo_frame):
        """Esconde a página atual e exibe a nova."""
        if self.pagina_atual is not None:
            self.pagina_atual.pack_forget()   # 👈 chave da técnica
        novo_frame.pack(fill="both", expand=True)
        self.pagina_atual = novo_frame

    def mostrar_relogio(self):
        self.trocar_pagina(self.frame_relogio)

    def mostrar_data(self):
        agora = datetime.now()
        self.lbl_data.configure(
            text=agora.strftime("%A, %d de %B de %Y")
        )
        self.trocar_pagina(self.frame_data)

    def atualizar_relogio(self):
        hora = datetime.now().strftime("%H:%M:%S")
        self.lbl_hora.configure(text=hora)
        self.after(1000, self.atualizar_relogio)  # atualiza a cada 1s

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = App()
    app.mainloop()