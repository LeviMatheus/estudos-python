#CODIGO FEITO POR LEVI MATHEUS
#PEGA UMA IMAGEM E A SEPARA EM X PARTES DE FORMA MATRICIAL
#COMO USAR:
#python image-Splitter.py nome_imagem.ext qtd_linhas qtd_colunas

import PIL
import sys
import os
from PIL import Image

#PIL.Image.MAX_IMAGE_PIXELS =
PIL.Image.MAX_IMAGE_PIXELS = None

path = os.getcwd()

try:
    os.mkdir(path + "/cortadas")
except OSError:
    print("Erro ao criar pasta para as imagens cortadas")
else:
    print("Diretório das imagens separadas criado")

#pegando valor das variaveis via parametros
imgm = str(sys.argv[1])
qtd_linhas = int(str(sys.argv[2]))
qtd_colunas = int(str(sys.argv[3]))

img = Image.open(imgm, mode="r")
extensao = img.format
img = img.convert('L')
largura, altura = img.size
largura = largura/qtd_colunas
altura = altura/qtd_linhas

for l in range(qtd_linhas):#linhas
    for c in range(qtd_colunas):#colunas
        if(l==0 and c==0):
            area = (0,0,largura,altura)
        elif(c==0):
            area = (0, altura*l, largura, altura*(l+1))
        else:
            area = (largura*c, altura*l, largura*(c+1), altura*(l+1))
        img_cortada = img.crop(area)
        if(qtd_linhas<qtd_colunas):
            img_cortada = img_cortada.resize((2480,3508))
        else:
            img_cortada = img_cortada.resize((3508,2480))
        img_cortada.save("cortadas/parte_l" + str(l) + "c" + str(c) + "." + extensao)

print("Imagens separadas com sucesso...")
#input("Aperte Enter para finalizar...")