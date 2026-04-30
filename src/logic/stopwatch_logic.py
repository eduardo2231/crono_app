import time
class StopwatchLogic:
    def __init__(self):
        self.rodando = False
        self.tempo_inicio = 0.0
        self.tempo_acumulado = 0.0
        self.voltas = []

    def iniciar_ou_continuar(self):
        if not self.rodando:
            self.tempo_inicio = time.time() - self.tempo_acumulado
            self.rodando = True

    def pausar(self):
        self.rodando = False

    def resetar(self):
        self.rodando = False
        self.tempo_inicio = 0.0
        self.tempo_acumulado = 0.0
        self.voltas.clear()

    def atualizar_tempo(self):
        if self.rodando:
            self.tempo_acumulado = time.time() - self.tempo_inicio
        return self.tempo_acumulado

    def inserir_volta(self):
        tempo = self.formatar_tempo(self.tempo_acumulado)
        self.voltas.append(tempo)
        return tempo

    @staticmethod
    def formatar_tempo(segundos):
        h = int(segundos // 3600)
        m = int((segundos % 3600) // 60)
        s = int(segundos % 60)
        ds = int((segundos * 10) % 10)
        return f"{h:02}:{m:02}:{s:02}.{ds}"