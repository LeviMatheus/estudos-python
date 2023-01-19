#FEITO POR LEVI MATHEUS
#ESTE CODIGO ENTRA NA PASTA PRE-PROCESSAR A PARTIR DO DIRETORIO ATUAL E
#PEGA TODOS OS ARQUIVOS DENTRO DELA E RETIRA TAGS HTMLS <DOC ID="" E <\DOC>
#UTILIZADO PARA USAR EM ARQUIVOS DE SAIDA DO SCRIPT WIKIEXTRACTOR

import os
import sys
import fileinput
from pprint import pprint

path = r'pre-processar/'
os.chdir(path)

for file in os.listdir(os.getcwd()):
    filename = os.path.splitext(file)
    nomearq = filename[0]

#print(nomearq)
pprint("###### DIRETÓRIO ATUAL: " + os.getcwd() + " ######")

#nomearq = "wiki_00"
ext = ""

pprint("###### INICIANDO A LEITURA DOS ARQUIVOS ######")

arquivo = open(nomearq + ext, "r", encoding="utf8")
linhas = arquivo.readlines()
arquivo.close()

pprint("###### FIM LEITURA DOS ARQUIVOS ######")

ext = ".txt"

pprint("###### INICIANDO LIMPEZA DOS ARQUIVOS ######")

novo_arq = open(nomearq + "_" + ext, "w", encoding="utf8")
for linha in linhas:
    linha = linha.strip()
    if not '<doc id=' in linha:
        if not '</doc>' in linha:
            novo_arq.write(linha + "\n")

pprint("###### FIM PREPROCESSAMENTO ######")

novo_arq.close()