from objeto import Objeto

class Bola(Objeto):

    #CONSTRUTOR DA CLASSE USANDO A CLASSE PAI
    def __init__(self, nome, tipo, cor, tamanho):
        super().__init__(str(nome).title(),str(tipo).title(), str(cor).title(),str(tamanho).title())

    #METODO ESPECIFICO DA CLASSE FILHA
    def rolar_bola(self):
        print(f"A bola {self.nome} está rolando...")