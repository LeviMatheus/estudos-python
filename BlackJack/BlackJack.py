import random

class jogo():

    _cartas_base = ['A','A','A','A','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10','Q','Q','Q','Q','J','J','J','J','K','K','K','K']
    _cartas = []
    
    def __init__(self):
        print("---------- Bem vindo ao Black Jack ---------- ")

    def iniciar(self):
        print("Bem vindo ao Black Jack")
        print("---------- O jogo vai começar ----------")
        self.reseta_cartas()

    def reseta_cartas(self):
        self._cartas = self._cartas_base

    def remove_carta(self, carta):
        self._cartas.remove(carta)

    @property
    def pegar_cartas(self):
        return self._cartas

    def sortear_carta(self, qtd):
        cartas = []
        while(qtd > 0):
            carta = random.choice(self._cartas)
            self.remove_carta(carta)
            qtd -= 1
        return carta

class main():
    jogo = jogo()
    jogo.iniciar()

    carta = jogo.sortear_carta()