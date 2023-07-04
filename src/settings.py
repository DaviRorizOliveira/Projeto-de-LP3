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

# Valor de cada elemento a ser vendido / comprado
CUSTO_TOMATE = 15
CUSTO_BATATA = 10
CUSTO_TRIGO = 17

CUSTO_LEITE = 8
CUSTO_OVO = 5
CUSTO_LA = 15

CUSTO_ENXADA = 25