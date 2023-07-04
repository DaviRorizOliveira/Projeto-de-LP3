import pygame
from random import randrange
from settings import *
from local import Local
from converte import Converte
from imprime import Imprime
from planta import Planta

class Farm(Local, Converte, Imprime):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        super(Converte, self).__init__()

        self.pos_x = x # Posição na tela
        self.pos_y = y # Posição na tela

        self.slots = []

        for a in range(5):
            planta = Planta(self.pos_x + a * 45, self.pos_y)
            self.slots.append(planta)

        #self.plant = plant
        #self.inv = inv
    
    def build_local(self, screen, new_tam_x=None, new_tam_y=None):
        super().build_local(screen, new_tam_x, new_tam_y)
        for a in range(5):
            self.slots[a].build_slot(screen)
        #self.slots[0].build_slot(screen)

    def coloca_semente(self, slot, semente, player):
        if player.vida_da_enxada != 0:
            self.slots[slot].tipo_planta = semente
            self.slots[slot].planta()
            player.vida_da_enxada -= 1
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