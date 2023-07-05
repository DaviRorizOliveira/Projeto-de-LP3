import pygame
from converte import Converte
from local import Local
from animal import Animal

class Cercado(Local):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.slots = []

        for a in range(3):
            animal = Animal(Converte.animal(a), Converte.produto(a))
            self.slots.append(animal)
    
    def colheita(self, slot, player):
        if self.slots[slot].especie == 'vaca':
            player.qtd_leite += self.slots[slot].qtd_produzido
        elif self.slots[slot].especie == 'galinha':
            player.qtd_ovo += self.slots[slot].qtd_produzido
        elif self.slots[slot].especie == 'ovelha':
            player.qtd_la += self.slots[slot].qtd_produzido
        self.slots[slot].qtd_produzido = 0
        self.slots[slot].alimentado = False
    
    def alimentar(self, slot, player):
        if self.slots[slot].especie == 'vaca':
            self.slots[slot].alimentado = True
            player.qtd_trigo -= 1
        elif self.slots[slot].especie == 'galinha':
            self.slots[slot].alimentado = True
            player.qtd_tomate -= 1
        elif self.slots[slot].especie == 'ovelha':
            self.slots[slot].alimentado = True
            player.qtd_batata -= 1