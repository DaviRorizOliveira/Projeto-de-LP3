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

    def coloca_semente(self, slot, semente):
        self.slots[slot].tipo_planta = semente
        self.slots[slot].planta()
        #self.slots[slot].build_slot(screen)
        #print('Foi plantado')
        
        #tipo = 5
        #self.inv.imprime()
        #i = self.inv.get_inventario()
        #if i != False:
        #    while tipo == 5:
        #        item = input("Qual item você quer utilizar(1 para sair)\n")
        #        if item == "1":
        #            return 0
        #        elif item == "NULL":
        #            print("Voce nao possui esse item")
        #        t,q = self.inv.get_inventario(item,1)
        #        tipo = self.c_semente(t)
        #        if tipo != None:
        #            while self.plant.get(tipo):
        #                tipo = tipo + 10
        #        
        #            a = [0, 0, 0, 0]
        #            self.plant[tipo] = a
        #else:
        #    print("Voce nao pode plantar! Compre uma enxada para poder plantar mais")