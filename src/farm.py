import pygame
from settings import *
from local import Local
from planta import Planta

class Farm(Local):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.pos_x = x # Posição na tela
        self.pos_y = y # Posição na tela

        self.slots = []

        for a in range(5):
            planta = Planta(self.pos_x + 70 + a * 110, self.pos_y)
            self.slots.append(planta)
    
    def build_local(self, screen, new_tam_x=None, new_tam_y=None):
        super().build_local(screen, new_tam_x, new_tam_y)
        for a in range(5):
            self.slots[a].build_slot(screen)

    def coloca_semente(self, slot, semente, player):
        if player.vida_da_enxada != 0:
            if semente == 'tomate' and player.s_tomate > 0:
                self.slots[slot].tipo_planta = semente
                self.slots[slot].planta()
                player.usa_enxada()
                player.s_tomate -= 1
            elif semente == 'batata' and player.s_batata > 0:
                self.slots[slot].tipo_planta = semente
                self.slots[slot].planta()
                player.usa_enxada()
                player.s_batata -= 1
            elif semente == 'trigo' and player.s_trigo > 0:
                self.slots[slot].tipo_planta = semente
                self.slots[slot].planta()
                player.usa_enxada()
                player.s_trigo -= 1
            else:
                pass
        else:
            pass

    def colher(self, slot, player):
        if self.slots[slot].tipo_planta == 'tomate':
            player.qtd_tomate += 3
        elif self.slots[slot].tipo_planta == 'batata':
            player.qtd_batata += 3
        elif self.slots[slot].tipo_planta == 'trigo':
            player.qtd_trigo += 3
        self.slots[slot].tipo_planta = None
        self.slots[slot].idade = -1
        self.slots[slot].sprite_atual = -1
        self.slots[slot].status = ''
        self.slots[slot].image = pygame.Surface((45, 75))

    def verifica_colheita(self, slot, player):
        if self.slots[slot].idade >= 4:
            self.colher(slot, player)
        else:
            pass