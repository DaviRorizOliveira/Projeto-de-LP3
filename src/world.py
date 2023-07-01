import pygame
from settings import *
from farmer import Farmer
from local import Local
from popup import Popup
from farm import Farm
from casa import Casa

class World:
    def __init__(self):
        self.player = Farmer('inventario')
        self.casa = Casa('imagens/house.png', WIDTH - 300, 0, self.player)
        self.cercado = Local('imagens/cercado.png', 0, 0)
        self.popup = Popup()
        self.farm = Farm('imagens/dirt_background.jpeg', 0, HEIGHT - 75)

    def build_screen(self, screen):
        background_image = pygame.image.load('imagens/grass_background.jpg')
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        screen.blit(background_image, (0, 0))

    def build_world(self, screen, dt):
        self.build_screen(screen)

        #tomate = pygame.image.load('imagens/batata_01.png')
        #tomate = pygame.transform.scale(tomate, (45, 75))
        #self.screen.blit(tomate, (0, 400))

        self.farm.build_local(screen)
        self.casa.build_local(screen, 300, 300)
        self.cercado.build_local(screen, 250, 250)
        self.player.build_player(screen, dt, self.casa, self.cercado, self.farm, self.popup)