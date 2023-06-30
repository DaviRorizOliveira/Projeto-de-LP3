import pygame
from settings import *
from local import Local
from pass_day import Passa_dia

class Casa(Local):
    def __init__(self, image, x, y, player):
        super().__init__(image, x, y)
        self.dormir = Passa_dia()

        self.mensagem01 = 'Você deseja dormir para passar o dia? Aperte J'
        self.mensagem02 = f'Nome do jogador: {player.nome}'
        self.mensagem03 = f'Você tem {player.dinheiro} reais'

    def popup_screen(self, screen):
        interação01 = FONTE1.render(self.mensagem01, True, BLACK)
        screen.blit(interação01, (325, 185))
        interação02 = FONTE1.render(self.mensagem02, True, BLACK)
        screen.blit(interação02, (325, 260))
        interação03 = FONTE1.render(self.mensagem03, True, BLACK)
        screen.blit(interação03, (325, 285))