'''print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("Hello " + input("What is your name?"))

a = input("Valor de a: ")
b = input("Valor de b: ")

temp = a
a = b
b = temp
print(f"a: {a}")
print(f"b: {b}")'''

print("Gerador de nome de banda")

nome_cidade = input("Qual é o nome da cidade que você nasceu? \n")
nome_animal = input("Qual o nome do seu pet favorito ? \n")

nome_banda = nome_cidade + " " + nome_animal

print(f"O nome da sua banda é: {nome_banda}")