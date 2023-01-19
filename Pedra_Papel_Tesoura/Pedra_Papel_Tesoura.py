import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
escolhas_jogo = [pedra,papel,tesoura]

while(True):
    escolhas_jogador = int(input("O que você escolhe? Digite 0 para pedra, 1 para papel ou 2 para tesoura.\n"))
    if escolhas_jogador >= 3 or escolhas_jogador < 0: 
        print("Você digitou um número inválido, Você perdeu!") 
    else:
        print(escolhas_jogo[escolhas_jogador])

        escolhas_pc = random.randint(0, 2)
        print("Escolha do pc:")
        print(escolhas_jogo[escolhas_pc])

        if escolhas_jogador == 0 and escolhas_pc == 2:
            print("Você ganhou!")
        elif escolhas_pc == 0 and escolhas_jogador == 2:
            print("Você perdeu")
        elif escolhas_pc > escolhas_jogador:
            print("Você perdeu")
        elif escolhas_jogador > escolhas_pc:
            print("Você ganhou!")
        elif escolhas_pc == escolhas_jogador:
            print("Empate!")
