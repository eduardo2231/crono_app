class TimerLogic:
    def __init__(self):
        self.rodando = False
        self.duracao_total = 0
        self.tempo_restante = 0

    def definir_tempo(self, horas: int, minutos: int, segundos: int):
        self.duracao_total = horas * 3600 + minutos * 60 + segundos
        self.tempo_restante = self.duracao_total

    def iniciar(self):
        if self.tempo_restante > 0:
            self.rodando = True

    def pausar(self):
        self.rodando = False

    def resetar(self):
        self.rodando = False
        self.tempo_restante = self.duracao_total

    def tick(self):
        if self.rodando and self.tempo_restante > 0:
            self.tempo_restante -= 1
            if self.tempo_restante == 0:
                self.rodando = False

    @staticmethod
    def formatar_tempo(total_segundos: int) -> str:
        h = total_segundos // 3600
        m = (total_segundos % 3600) // 60
        s = total_segundos % 60
        return f"{h:02}:{m:02}:{s:02}"