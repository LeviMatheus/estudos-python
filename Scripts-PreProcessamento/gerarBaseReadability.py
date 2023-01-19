#ESTE CODIGO ENTRA NA PASTA textos A PARTIR DO DIRETORIO ATUAL E
#PEGA TODOS OS ARQUIVOS DENTRO DELA E GERA UM DATAFRAME CONTENDO AS ESTATISTICAS E CLASSE
#UTILIZADO PARA USAR EM ARQUIVOS DE SAIDA DO SCRIPT QUE SEPARA UM CORPUS EM DIFERENTES ARQUIVOS .TXT
#BASEADO EM: https://pypi.org/project/readability/

from numpy import compare_chararrays
#from readability import Readability
import readability
import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
import os, os.path
from pathlib import Path
from pprint import pprint
from nltk.tokenize import TweetTokenizer
#import dabl
import sweetviz as sv
import spacy

tknzr =  TweetTokenizer()
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
    nomeOrigem = bytes(nomeOrigem, 'utf-8').decode('utf-8', 'ignore')
    #print("nome arquivo: " + str(nomeOrigem) + "\n")
    arquivo = open(nomeOrigem, "r", encoding="utf8")
    linhas = arquivo.readlines()#lendo linhas do arquivo
    linhas = ''.join(linhas)#transformando lista em string
    texto = tknzr.tokenize(linhas)#tokenizando string
    #print("Linhas: " + str(linhas))
    results = readability.getmeasures(texto, lang='en')
    valor_classe = results['readability grades']['Kincaid']
    if(valor_classe <= 6):
        ef_level = "Basic"
    elif(valor_classe > 6 and valor_classe <= 12):
        ef_level = "Average"
    elif(valor_classe > 12):
        ef_level = "Skilled"
    if(results['sentence info']['words']>=10):
        #grade levels
        #kincaid = results['readability grades']['Kincaid']
        classe = ef_level#results['readability grades']['FleschReadingEase']#requere no minimo 100 palavras
        #estatisticas do texto
        characters_per_word = results['sentence info']['characters_per_word']
        syll_per_word = results['sentence info']['syll_per_word']
        words_per_sentence = results['sentence info']['words_per_sentence']
        sentences_per_paragraph = results['sentence info']['sentences_per_paragraph']
        type_token_ratio = results['sentence info']['type_token_ratio']
        characters = results['sentence info']['characters']
        syllables = results['sentence info']['syllables']
        words = results['sentence info']['words']
        wordtypes = results['sentence info']['wordtypes']
        sentences = results['sentence info']['sentences']
        paragraphs = results['sentence info']['paragraphs']
        long_words = results['sentence info']['long_words']
        complex_words = results['sentence info']['complex_words']
        complex_words_dc = results['sentence info']['complex_words_dc']
        #uso de palavras
        tobeverb = results['word usage']['tobeverb']
        auxverb = results['word usage']['auxverb']
        conjunction = results['word usage']['conjunction']
        pronoun = results['word usage']['pronoun']
        preposition = results['word usage']['preposition']
        nominalization = results['word usage']['nominalization']
        #começo de frase
        pronoun = results['sentence beginnings']['pronoun']
        interrogative = results['sentence beginnings']['interrogative']
        article = results['sentence beginnings']['article']
        subordination = results['sentence beginnings']['subordination']
        beginnings_conjunction = results['sentence beginnings']['conjunction']
        beginnings_preposition = results['sentence beginnings']['preposition']
        #criando a lista de características
        preDataframe.append({
                "Text" : str(nomeOrigem), #nome da definição
                "characters_per_word" : characters_per_word,
                "syll_per_word" : syll_per_word,
                "words_per_sentence" : words_per_sentence,
                "sentences_per_paragraph" : sentences_per_paragraph,
                "type_token_ratio" : type_token_ratio,
                "characters" : characters,
                "syllables" : syllables,
                "words" : words,
                "wordtypes" : wordtypes,
                "sentences" : sentences,
                "paragraphs" : paragraphs,
                "long_words" : long_words,
                "complex_words" : complex_words,
                "complex_words_dc" : complex_words_dc,
                "tobeverb" : tobeverb,
                "auxverb" : auxverb,
                "conjunction" : conjunction,
                "pronoun" : pronoun,
                "preposition" : preposition,
                "nominalization" : nominalization,
                "pronoun" : pronoun,
                "interrogative" : interrogative,
                "article" : article,
                "subordination" : subordination,
                "beginnings_conjunction" : beginnings_conjunction,
                "beginnings_preposition" : beginnings_preposition,
                "Classe" : classe#ToDo: Rotular classe em 3 níveis ou não, deixar isso pro programa final
            })
    else:
        print("\n Arquivo " + nomeOrigem + " não possui mais de 100 palavras. Arquivo ignorado \n")

#Dataframe sem normalização
#print("\n ### Dataframe sem tratamento ### \n")
#print("\n " + str(preDataframe) + " \n")
#gerando a dataframe
print("\n ### Gerando a base de dados ### \n")
Dataframe = pd.DataFrame(preDataframe)
#pprint(Dataframe)
#normalizando a base
#normalizar = StandardScaler()
#print("colunas antes: " + str(len(Dataframe.columns)))
#nomes = Dataframe.iloc[:,0]
classes = Dataframe.iloc[:,-1]
#print("Classes: " + str(classes[:][:]))
#pprint(Dataframe.iloc[:,24])
Dataframe = Dataframe.iloc[:,1:-1]#retirando aquilo que não for características a ser normalizada
#pprint(Dataframe)
#print("colunas depois: " + str(len(Dataframe.columns)))
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(Dataframe)
#print("\n ### Normalizando dados da base ### \n")
#dadosNormalizados = normalizar.fit_transform(Dataframe)
#print("\n ### Caracteristicas normalizadas ### \n")
#print("\n " + str(dadosNormalizados) + " \n")
base = pd.DataFrame(scaled_data,columns=Dataframe.columns)
#base.insert(0,'Text',nomes)#INSERIR NOMES DOS ARQUIVOS NA BASE DESCOMENTAR ESSA LINHA
base['classes'] = classes#INSERIR CLASSES DOS ARQUIVOS NA BASE DESCOMENTAR ESSA LINHA
#print("## Base de dados ##")
#pprint(str(base))
os.chdir('../')
print("\n ### Gerando arquivos .csv de saída ### \n")
base.to_csv('saidaCSV.csv',header=True,index=False,sep=',',encoding='utf-8-sig')
#criando vizualização
my_report = sv.analyze(base)
my_report.show_html()