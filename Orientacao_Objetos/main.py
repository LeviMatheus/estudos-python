from bola import Bola
from talher import Talher

garfo_normal = Talher('Garfo',1,'Prata','Médio')
bola_jabulani = Bola('Jabulani','Copa Oficial','Branca','Normal')

#print(f"{garfo_normal.nome} é do tipo {garfo_normal.tipo}, cor {garfo_normal.cor} e tamanho {garfo_normal.tamanho}")
#print(f"{bola_jabulani.nome} é do tipo {bola_jabulani.tipo}, cor {bola_jabulani.cor} e tamanho {bola_jabulani.tamanho}")

#CHAMANDO METODO ESPECIFICO DA CLASSE FILHA PELA INSTANCIA 
garfo_normal.pegar_talher()

#CHAMANDO METODO DA CLASSE PAI QUE USA ATRIBUTO DE CLASSE
garfo_normal.mostrar_codigo_classe()

#CHAMANDO METODO ESTATICO DA CLASSE PAI DIRETO PELA CLASSE e PELA INSTANCIA
Talher.mostrar_informar_estatico()
garfo_normal.mostrar_informar_estatico()

#CHAMANDO METODO DA CLASSE PAI PELA INSTANCIA
garfo_normal.mostrar_informacoes_atributos()
#bola_jabulani.rolar_bola()