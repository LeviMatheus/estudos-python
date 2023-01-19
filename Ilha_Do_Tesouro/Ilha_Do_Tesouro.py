print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tesouro.")
print("Sua missão é encontrar o tesouro.")

escolha1 = input('Você está na rodovia. Aonde deseja ir? Digite "esquerda" ou "direita" \n').lower()
if escolha1 == "esquerda":
  escolha2 = input('Você chegou ao laago. Tem uma ilha no meio do lago. Digite "esperar" para esperar pelo bote. Digite "nadar" para nadar pelo lago. \n').lower()
  if escolha2 == "esperar":
    escolha3 = input("Você chega na ilha vivo. Existem 3 portas. Uma vermelha, uma amarela e outra azul. Qual cor você escolhe? \n").lower()
    if escolha3 == "vermelha":
      print("A sala está incendeia instantaneamente. Game Over.")
    elif escolha3 == "amarela":
      print("Você encontrou o tesouro! Você venceu!")
    elif escolha3 == "azul":
      print("Você entrou na sala das feras e é brutalmente atacado. Game Over.")
    else:
      print("Você escolheu a porta que não existe. Game Over.")
  else:
    print("Você foi atacado por milhares de piranhas. Game Over.")
else:
  print("Você caiu em um abismo. Game Over.")