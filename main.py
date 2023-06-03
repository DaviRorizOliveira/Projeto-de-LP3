import pygame
from movment import Farmer

# Configurações da tela
WIDTH = 1280
HEIGHT = 720

# Configurações do jogador
dt = 0

# Cores
GREEN = (50, 169, 62)

# Inicialização do pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Jogo')

player = Farmer(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill(GREEN)

    player.update_pos(dt, screen, WIDTH, HEIGHT)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
