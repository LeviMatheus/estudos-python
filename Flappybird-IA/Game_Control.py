import pygame
import os
import random
import Game_Config

class Game_Control:

    def __init__(self):
        pygame.display.set_caption(Game_Config.TITULO)
        # CHAMA SLASH SCREEN
        self.abertura_jogo()

    def abertura_jogo(self):
        #APRESENTA A SPLASH
        self.altera_cenario(Game_Config.IMG_SPLASH_SCREEN)
        #AGUARDA 5SEG
        pygame.time.wait(5000)
        #VAI PRO CENARIO INICIAL
        self.altera_cenario(Game_Config.IMG_SALA_FEEDBACK)

    def novo_jogo(self):
        # configurações de um novo jogo
        print(f"Iniciando um novo jogo.")
        self._pontos = 0
        self._rodando = True
        self._jogador_vivo = True

    @property
    def pontos(self):
        return self._pontos

    @pontos.setter
    def pontos(self, quantidade):
        self._pontos += quantidade

    @property
    def jogador_vivo(self):
        return self._jogador_vivo

    def fim_de_jogo(self):
        pygame.quit()   #finaliza o jogo
        quit()          #finaliza o script

    @staticmethod
    def altera_cenario(cenario):
        if not cenario == Game_Config.IMG_BACKGROUND: #só altera se for diferente do cenário atual
            Game_Config.IMG_BACKGROUND = cenario # altera o fundo
            Game_Config.TELA.blit(Game_Config.IMG_BACKGROUND, (0, 0)) #desenha o fundo
            pygame.display.update()