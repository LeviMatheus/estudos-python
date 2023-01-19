from objeto import Objeto

class Talher(Objeto):

    #CONSTRUTOR DA CLASSE USANDO A CLASSE PAI
    def __init__(self, nome, tipo, cor, tamanho):
        super().__init__(str(nome).title(),str(tipo).title(),str(cor).title(),str(tamanho).title())

    #METODO ESPECIFICO DA CLASSE FILHA
    def pegar_talher(self):
        print(f"Você pegou o talher {self.nome}")