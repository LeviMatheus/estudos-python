#IMPORTSletras_certas
import random
import re

#VARIAVEIS
ativo = True #variavel para controle
tentativas = 10 #nro de tentativas base
list_letras_feitas = []
letras_certas = []

#FUNCOES
def mostrar_painel():
    print("\n ********* ADIVINHE A PALAVRA *********")
    separador = '*'
    print(f" A palavra secreta {separador*(len(palavra)-1)} tem {(len(palavra)-1)} letras.")
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras já digitadas: {list_letras_feitas}")
    #FALTA MOSTRAR AS LETRAS

def encontrar_indices(palavra, letra):
    pos = []
    start = 0
    end = len(palavra)-1
    while True: 
        loc = palavra.find(letra, start, end)
        if  loc == -1:
            break
        else:
            pos.append(loc)
            start = loc + len(letra)
    return pos

def revelar_letra(indices,letra):
    #ADICIONA NO VETOR letras_certas
    for indice in indices:
        letras_certas[indice] = letra
    #REVELA AS LETRAS
    print(letras_certas)
    #QUEBRA DE LINHA
    print('\n')

def ja_digitada(letra):
    if letra in list_letras_feitas:
        return True
    else:
        return False

def checar_letra(letra):
    if((letra in palavra) and not ja_digitada(letra)):
        list_letras_feitas.append(letra)
        #letras_certas.append(letra)
        return True
    else:
        print(f"A palavra não possui {letra} ou já foi digitada anteriormente. Escolha outra.")
        if(not ja_digitada(letra)):
            list_letras_feitas.append(letra)
        return False

def ganhou(letras_certas):
    if not '' in letras_certas:
        print("\n ****** VOCE GANHOU ****** \n")
        print("*********************")
        print(f"A palavra é {palavra}")
        print("*********************")
        ativo = False

def jogo():
    if tentativas > 0:
        ativo = True
        ganhou(letras_certas)
    else:
        print("\n ****** VOCE PERDEU ******")
        print("*********************")
        print(f"A palavra era {palavra}")
        print("*********************")
        ativo = False
    return ativo

#INICIANDO O JOGO
#LEITURA DO ARQUIVO
with open("Python\palavras.txt", "r") as base:
    palavras = base.readlines()
#SORTEANDO A PALAVRA
palavra = random.choice(palavras)
#CRIANDO VETOR COM VAZIOS
letras_certas = [''] * (len(palavra)-1)
#ATUALIZA NRO DE TENTATIVAS
tentativas = round((len(palavra)-1) * 1.5)
#ITERANDO
while(jogo()):
    #MOSTRAR PAINEL
    mostrar_painel()
    #SOLICITAR LETRA
    print("Digite uma letra: ")
    letra = str(input().upper())
    if not letra.isalpha() or len(letra) > 1 or len(letra) == 0:
        print('Você digitou um caracter inválido ou mais de uma letra.')
        continue
    #CHECAR LETRA
    if checar_letra(letra):
        indices = encontrar_indices(palavra,letra)
        revelar_letra(indices,letra)
    else:
        print(letras_certas)
    #DIMINUIR TENTATIVAS
    tentativas-=1




