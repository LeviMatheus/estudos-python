print("Bem vindo à calculadora de gorjeta")
valor_total = input("Qual a gorjeta total que o grupo dará? \n$")
porcentagem = input("Qual a porcentagem do total que vocês gostariam de dar? 10, 12 ou 15 \n%")
nro_pessoas = input("A vaquinha da gorjeta será em quantas pessoas? \n")

valor_total_gorjeta = (float(valor_total)*float(porcentagem))/100
valor_individual = round(valor_total_gorjeta/int(nro_pessoas),2)

print(f"Cada pessoa irá pagar ${valor_individual}")