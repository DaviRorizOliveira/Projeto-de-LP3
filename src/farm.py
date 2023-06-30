import pygame
from settings import *
from local import Local

class Farm(Local):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.grossura_da_borda = 35
        self.largura_do_retangulo = 225
        self.altura_do_retangulo = 75
        self.pos_x = x
        self.pos_y = y
        self.slots = []

    def build_local(self, screen):
        self.image = pygame.transform.scale(self.image, (self.largura_do_retangulo, self.altura_do_retangulo))
        screen.blit(self.image, (self.pos_x, self.pos_y))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        #pygame.draw.rect(screen, BLACK, pygame.Rect(self.pos_x, self.pos_y, self.largura_do_retangulo, self.altura_do_retangulo), self.grossura_da_borda, 0, 0, 20, 0)