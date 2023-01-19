class Objeto:

    #ATRIBUTO DE CLASSE
    _Codigo_classe = "0x07128300"
    
    #CONSTRUTOR
    def __init__(self, nome, tipo, cor, tamanho):
        self._nome = nome.title()
        self._tipo = tipo.title()
        self._cor = cor.title()
        self._tamanho = tamanho.title()

    #GETS
    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo

    @property
    def cor(self):
        return self._cor

    @property
    def tamanho(self):
        return self._tamanho

    #SETS
    @nome.setter
    def definir_nome(self, nome):
        self._nome = nome

    @tipo.setter
    def definir_tipo(self, tipo):
        self._tipo = tipo

    @cor.setter
    def definir_cor(self, cor):
        self._cor = cor

    #METODO PARA MOSTRAR INFORMACOES DO OBJETO ATRAVES DOS ATRIBUTOS DA INSTANCIA
    def mostrar_informacoes_atributos(self):
        print(f"{self._nome} é do tipo {self._tipo}, cor {self._cor} e tamanho {self._tamanho}")

    #METODO DA CLASSE ACESSANDO ATRIBUTE
    @classmethod
    def mostrar_codigo_classe(cls):
        print(f"Valor do atributo de classe 'Código da classe': {cls._Codigo_classe}")

    #METODO ESTATICO
    @staticmethod
    def mostrar_informar_estatico():
        print(f"Retorno do método estático 'show_objeto' da classe: Isto é um objeto")