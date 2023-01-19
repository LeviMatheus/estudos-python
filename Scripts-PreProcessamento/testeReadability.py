#ESTE CODIGO ENTRA NA PASTA textos A PARTIR DO DIRETORIO ATUAL E
#PEGA TODOS OS ARQUIVOS DENTRO DELA E GERA UM DATAFRAME CONTENDO AS ESTATISTICAS E CLASSE
#UTILIZADO PARA USAR EM ARQUIVOS DE SAIDA DO SCRIPT QUE SEPARA UM CORPUS EM DIFERENTES ARQUIVOS .TXT

from numpy import compare_chararrays
from readability import Readability
import pandas as pd
from sklearn.preprocessing import normalize, StandardScaler
import os, os.path
import json, csv, sys
from pathlib import Path
from pprint import pprint

preDataframe = []
extensoes_validas = [".txt"] #extensao valida das imagens a serem usadas no processamento
caminhoTextos = r'textos/' #pasta que contem os textos
#print(os.getcwd()) #checar se o projeto esta no diretorio correto
os.chdir(caminhoTextos)
#texto = "The wolf (Canis lupus) is a mammal of the order Carnivora. It is sometimes called timber wolf or grey wolf, It is the ancestor of the domestic dog. A recent study found that the domestic dog is descended from wolves tamed less than 16,300 years ago south of the Yangtze River in China, There are many different wolf subspecies, such as the Arctic wolf. Some subspecies are listed on the endangered species list, but overall, Canis lupus is IUCN graded as 'least concern'. Adult wolves are usually 1.4 to 1.8 metres (4.6 to 5.9 ft) in length from nose to tail depending on the subspecies.[3] Wolves living in the far north tend to be larger than those living further south"

print("\n ### Extraindo as características dos textos ### \n")
#pegando todas os arquivos.txt do diretório
for im in os.listdir(os.getcwd()):
    filename = os.path.splitext(im)#separa o nome da extensao
    ext = filename[1]#pega a extensao
    if ext.lower() not in extensoes_validas:#checa se esta dentro das extensoes validas
        continue
    nomeOrigem = filename[0] + ext #nome original da imagem
    #print("nome arquivo: " + str(nomeOrigem) + "\n")
    arquivo = open(nomeOrigem, "r", encoding="utf8")
    linhas = arquivo.readlines()
    #print("Linhas: " + str(linhas))
    r = Readability(str(linhas))
    if(r._statistics.num_words>=100):
        #grade levels
        classe = r.flesch_kincaid()#requere no minimo 100 palavras
        '''fk = r.flesch_kincaid()
        f = r.flesch()
        gf = r.gunning_fog()
        cl = r.coleman_liau()
        dc = r.dale_chall()
        ari = r.ari()
        lw = r.linsear_write()
        spa = r.spache()'''
        #smg = r.smog(all_sentences=True) #só funciona para nro de sentenças >= 30
        # Mostrando valores das grade levels
        '''print("\n # Grade Levels # \n")
        print("Flesch Kincaid Grade Level: " + str(fk.grade_level))
        print("Flesch Reading Ease: " + str(f.grade_levels))
        print("Gunning Fog: " + str(gf.grade_level))
        print("Coleman Liau Index: " + str(cl.grade_level))
        print("Dale Chall Readability: " + str(dc.grade_levels))
        print("Automated Readability Index: " + str(ari.grade_levels))
        print("Linsear Write: " + str(lw.grade_level))
        print("Spache: " + str(spa.grade_level))'''
        #print("SMOG: " + str(smg.grade_level))
        #print("\n")
        #estatisticas do texto
        silabasXpalavra = r._statistics.avg_syllables_per_word
        palavrasXsentencas = r._statistics.avg_words_per_sentence
        complexoDaleChall = r._statistics.num_dale_chall_complex
        complexoGunning = r._statistics.num_gunning_complex
        complexoSpache = r._statistics.num_spache_complex
        qtdLetras = r._statistics.num_letters
        polySilabasXpalavras = r._statistics.num_poly_syllable_words
        numSentencas = r._statistics.num_sentences
        qtdSilabas = r._statistics.num_syllables
        qtdPalavras = r._statistics.num_words
        # Mostrando valores das estatísticas
        #print("\n ### Gerando as estatísticas ### \n")
        '''print("Média de sílabas por palavra: " + str(silabasXpalavra))
        print("Média de palavras por sentença: " + str(palavrasXsentencas))
        print("Complexo de Dale Chall: " + str(complexoDaleChall))
        print("Complexo de Gunning: " + str(complexoGunning))
        print("Complexo de Spache: " + str(complexoSpache))
        print("Número de letras: " + str(qtdLetras))
        print("Número de polisílabas por palavras: " + str(polySilabasXpalavras))
        print("Número de sentenças: " + str(numSentencas))
        print("Quantidade de sílabas: " + str(qtdSilabas))
        print("Quantiade de palavras: " + str(qtdPalavras))
        print("\n")'''
        #criando a lista de características
        preDataframe.append({
                "Texto" : str(nomeOrigem), #nome da definição
                "Média de sílabas por palavra: " : str(silabasXpalavra),
                "Média de palavras por sentença: " : str(palavrasXsentencas),
                "Complexo de Dale Chall: " : str(complexoDaleChall),
                "Complexo de Gunning: " : str(complexoGunning),
                "Complexo de Spache: " : str(complexoSpache),
                "Número de letras: " : str(qtdLetras),
                "Número de polisílabas por palavras: " : str(polySilabasXpalavras),
                "Número de sentenças: " : str(numSentencas),
                "Quantidade de sílabas: " : str(qtdSilabas),
                "Quantiade de palavras: " : str(qtdPalavras),
                "Classe" : str(classe.grade_level)#ToDo: Rotular classe em 3 níveis ou não, deixar isso pro programa final
            })
    else:
        print("\n Arquivo " + nomeOrigem + " não possui mais de 100 palavras. Arquivo ignorado \n")

#Dataframe sem normalização
#print("\n ### Dataframe sem tratamento ### \n")
#print("\n " + str(preDataframe) + " \n")
#gerando a dataframe
print("\n ### Gerando a base de dados ### \n")
Dataframe = pd.DataFrame(preDataframe)
#normalizando a base
normalizar = StandardScaler()
nomes = Dataframe.iloc[:,0]
classes = Dataframe.iloc[:,-1]
#print("Classes: " + str(classes[:][:]))
Dataframe = Dataframe.iloc[:,1:10]#retirando aquilo que não for características a ser normalizada
dadosNormalizados = normalizar.fit_transform(Dataframe)
#print("\n ### Caracteristicas normalizadas ### \n")
#print("\n " + str(dadosNormalizados) + " \n")
base = pd.DataFrame(dadosNormalizados)
#base['a'] = nomes
base.insert(0,'nome_arquivo',nomes)
base['z'] = classes
#print("## Base de dados ##")
#pprint(str(base))
os.chdir('../')
base.to_csv('saidaCSV.csv',header=False,index=False,sep=',',encoding='utf-8-sig')