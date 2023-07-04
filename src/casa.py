import pygame
from settings import *
from local import Local
from random import randrange

class Casa(Local):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        #self.dormir = Passa_dia()
        self.dia = 1

    def popup_screen(self, screen, player):
        interação01 = FONTE1.render('J - Você deseja dormir para passar o dia?', True, BLACK)
        screen.blit(interação01, (325, 185))
        interação02 = FONTE1.render(f'Nome do jogador: {player.nome}', True, BLACK)
        screen.blit(interação02, (325, 260))
        interação03 = FONTE1.render(f'Você tem {player.dinheiro} reais', True, BLACK)
        screen.blit(interação03, (325, 285))
        interação04 = FONTE1.render(f'Você tem enxada? {player.get_inventario()}', True, BLACK)
        screen.blit(interação04, (325, 310))
        interação05 = FONTE1.render(f'Quantidade de tomates: {player.qtd_tomate}', True, BLACK)
        screen.blit(interação05, (325, 335))
        interação06 = FONTE1.render(f'Quantidade de batatas: {player.qtd_batata}', True, BLACK)
        screen.blit(interação06, (325, 360))
        interação07 = FONTE1.render(f'Quantidade de trigo: {player.qtd_trigo}', True, BLACK)
        screen.blit(interação07, (325, 385))
    
    def passa_dia(self, farm, cercado):
        self.dia += 1
        for a in range(5):
            farm.slots[a].atualiza_idade()
        #for a in range(3):
        #    cercado.slots[a].atualiza_cercado()
        chuva = randrange(0,4)
        if chuva == 0:
            for a in range(5):
                farm.slots[a].atualiza_idade()
            #for a in range(3):
            #    cercado.slots[a].atualiza_cercado()