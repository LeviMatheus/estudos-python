import pygame
from pygame import *
import os
import random
import Game_Config
from Game_Control import *

#region Jean
class Jean:
    IMGS = Game_Config.IMGS_JEAN
    # animações da rotação

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.imagem = self.IMGS[0]
        self.mover(pygame.K_UP)
        self.falar(2)

    def falar(self, fala):
        if fala == 1:
            mixer.music.load('mp3/hahaha-pnc.mp3')
        elif fala == 2:
            mixer.music.load('mp3/hoje_eu_perco_reu_primario.mp3')
        elif fala == 3:
            mixer.music.load('mp3/n_aguento_mais.mp3')
        elif fala == 4:
            mixer.music.load('mp3/tem_coisas_que_enchem.mp3')
        elif fala == 5:
            mixer.music.load('mp3/tongo.mp3')
        elif fala == 6:
            mixer.music.load('mp3/levi_esses_audios.mp3')
        else:
            mixer.music.load('mp3/n_aguento_mais.mp3')
        mixer.music.play()

    def pular(self):
        self.velocidade = -10
        self.altura = self.y

    def mover(self, tecla): 
        if tecla == pygame.K_UP:
            self.pular()
        if tecla == pygame.K_DOWN:
            pass#self.coletar_item() #IMPLEMENTAR
        if tecla == pygame.K_RIGHT:
            self.x += 10
        if tecla == pygame.K_LEFT:
            self.x -= 10
        self.mudar_sprite()

    def mudar_sprite(self):
        # definir qual vai usar
        self.imagem = self.IMGS[0]
        # desenhar a imagem
        Game_Config.TELA.blit(self.imagem, (self.x, self.y))
        #atualiza tela
        pygame.display.update()

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)
#endregion

#region método desenhar na tela
def desenhar_tela(controlador):
    #Desenhar HUD na tela
    texto = Game_Config.FONTE_PONTOS.render(f"Pontuação: {controlador.pontos}", 1, (255, 255, 255))
    Game_Config.TELA.blit(texto, (Game_Config.TELA_LARGURA - 10 - texto.get_width(), 10))
    pygame.display.update()
#endregion

#region EVENTOS DO USUARIO
def iterar_eventos(jean,controlador):
    for evento in pygame.event.get():#itera eventos

        if evento.type == pygame.QUIT: #caso for fechar o jogo
            controlador.fim_de_jogo()

        if evento.type == pygame.KEYDOWN: #eventos de tecla
            if evento.key == pygame.K_SPACE: # ESPAÇO = pular
                jean.pular()
            if evento.key == pygame.K_UP or pygame.K_DOWN or pygame.K_LEFT or pygame.K_RIGHT: #MOVER
                jean.mover(evento.key)
            if evento.key == pygame.K_F1: #F1 = reproduzir som 1
                jean.falar(1)
            if evento.key == pygame.K_F2: #F2 = reproduzir som 2
                jean.falar(2)
            if evento.key == pygame.K_F3: #F3 = reproduzir som 3
                jean.falar(3)
            if evento.key == pygame.K_F4: #F4 = reproduzir som 4
                jean.falar(4)
            if evento.key == pygame.K_F5: #F5 = reproduzir som 5
                jean.falar(5)
            if evento.key == pygame.K_F6: #F6 = reproduzir som 6
                jean.falar(6)
            
#endregion

#region main
def main():
    #objeto para controles principais do jogo
    controlador = Game_Control()
    controlador.novo_jogo()
    #configura o novo personagem principal
    jean = Jean(230, 420)

    #controla o estado do jogo
    if not controlador.jogador_vivo:
        controlador.fim_de_jogo()
    else:#JOGO
        while controlador.jogador_vivo:
            #configura relógio 30 segundos
            Game_Config.RELOGIO.tick(30) 
            #iterar eventos de interacao do usuario
            iterar_eventos(jean, controlador)
            #atualiza a UI
            desenhar_tela(controlador)
#endregion

#region chamada do main
if __name__ == '__main__':
    main()
#endregion
