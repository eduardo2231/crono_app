import customtkinter as ctk
import time
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Cronometro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cronômetro")
        self.geometry("350x300")
        self.resizable(False, False)

        self.rodando = False
        self.tempo_inicio = 0
        self.tempo_acumulado = 0

        # Display do tempo
        self.label_tempo = ctk.CTkLabel(
            self, text="00:00:00.0",
            font=ctk.CTkFont(size=48, weight="bold")
        )
        self.label_tempo.pack(pady=40)

        # Botões
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=10)

        self.btn_iniciar = ctk.CTkButton(
            frame, text="Iniciar", width=100,
            command=self.toggle, fg_color="#2ecc71", hover_color="#27ae60"
        )
        self.btn_iniciar.grid(row=0, column=0, padx=10)

        self.btn_resetar = ctk.CTkButton(
            frame, text="Resetar", width=100,
            command=self.resetar, fg_color="#e74c3c", hover_color="#c0392b"
        )
        self.btn_resetar.grid(row=0, column=1, padx=10)

    def toggle(self):
        if not self.rodando:
            self.tempo_inicio = time.time() - self.tempo_acumulado
            self.rodando = True
            self.btn_iniciar.configure(text="Pausar", fg_color="#e67e22", hover_color="#d35400")
            threading.Thread(target=self.atualizar, daemon=True).start()
        else:
            self.rodando = False
            self.btn_iniciar.configure(text="Continuar", fg_color="#2ecc71", hover_color="#27ae60")

    def resetar(self):
        self.rodando = False
        self.tempo_acumulado = 0
        self.label_tempo.configure(text="00:00:00.0")
        self.btn_iniciar.configure(text="Iniciar", fg_color="#2ecc71", hover_color="#27ae60")

    def atualizar(self):
        while self.rodando:
            self.tempo_acumulado = time.time() - self.tempo_inicio
            h = int(self.tempo_acumulado // 3600)
            m = int((self.tempo_acumulado % 3600) // 60)
            s = int(self.tempo_acumulado % 60)
            ms = int((self.tempo_acumulado * 10) % 10)
            self.label_tempo.configure(text=f"{h:02}:{m:02}:{s:02}.{ms}")
            time.sleep(0.05)

if __name__ == "__main__":
    app = Cronometro()
    app.mainloop()