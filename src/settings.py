import pygame

# Configurações da tela
WIDTH = 1280
HEIGHT = 720

# Cores
GREEN = (50, 169, 62)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (102, 51, 0)

# Fontes
pygame.font.init()
FONTE1 = pygame.font.SysFont('arial', 25, True, False)

# Fontes do menu
def get_font(size):
    return pygame.font.Font("imagens/font.ttf", size)