import pygame
from pygame import *
import os

#DOCUMENTO PARA CONFIGURAÇÕES DE VARIÁVEIS DO JOGO

#CONSTANTES
TELA_LARGURA = 800
TELA_ALTURA = 600
TITULO = 'Jean Quest 1.0'

#GERAIS
TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
RELOGIO = pygame.time.Clock()

#FONTES
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 40)

#AUDIOS
mixer.init() #inicializa o player de sons
mixer.music.set_volume(0.5) #configura o volume

#IMAGENS
IMG_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMGS_JEAN = [
    pygame.image.load(os.path.join('imgs', 'jean_base.png')),
    pygame.image.load(os.path.join('imgs', 'jean_base.png')),
    pygame.image.load(os.path.join('imgs', 'jean_base.png')),
]

#CENARIOS FUNDO
IMG_SPLASH_SCREEN = pygame.image.load(os.path.join('imgs', 'splash.png'))
IMG_SALA_FEEDBACK = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'sala_feedback.jpg')))
IMG_BACKGROUND = IMG_SALA_FEEDBACK #mudar pra IMG DE ENTRADA DA SEDE DEPOIS
