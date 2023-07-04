import pygame
from random import randrange
from converte import Converte
from local import Local

class Cercado(Local, Converte):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        super(Converte, self).__init__()

        self.pos_x = x # Posição na tela
        self.pos_y = y # Posição na tela