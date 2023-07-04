import pygame
from settings import *
from local import Local
from pass_day import Passa_dia

class Casa(Local):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.dormir = Passa_dia()

    def popup_screen(self, screen, player):
        interação01 = FONTE1.render('J - Você deseja dormir para passar o dia?', True, BLACK)
        screen.blit(interação01, (325, 185))
        interação02 = FONTE1.render(f'Nome do jogador: {player.nome}', True, BLACK)
        screen.blit(interação02, (325, 260))
        interação03 = FONTE1.render(f'Você tem {player.dinheiro} reais', True, BLACK)
        screen.blit(interação03, (325, 285))
        interação04 = FONTE1.render(f'Você tem enxada? {player.get_inventario()}', True, BLACK)
        screen.blit(interação04, (325, 310))