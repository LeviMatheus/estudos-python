#Projeto gerador de list_senhas
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de list_senhas!")
qtd_letras = int(input(f"Quantas letras você quer incluir na sua list_senha?\n")) 
qtd_simbolos = int(input(f"Quantos símbolos especiais?\n"))
qtd_numeros = int(input(f"E quantos números?\n"))

list_senha = []
while(qtd_letras > 0):
    list_senha.append(random.choice(letras))
    qtd_letras-=1
while(qtd_simbolos > 0):
    list_senha.append(random.choice(simbolos))
    qtd_simbolos-=1
while(qtd_numeros > 0):
    list_senha.append(random.choice(numeros))
    qtd_numeros-=1
random.shuffle(list_senha)

senha = ""
for caractere in list_senha:
    senha+= caractere

print(f"Sua list_senha gerada é: {senha}")


