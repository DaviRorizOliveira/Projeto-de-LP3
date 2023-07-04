import pygame
from settings import *
from local import Local

class Mercado(Local):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)