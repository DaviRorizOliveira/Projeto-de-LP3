import pygame
from setup import *
from movment import Movimento
from local import Local
from popup import Popup

# Inicialização do pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Jogo')

player = Movimento()
casa = Local('imagens/house.png', WIDTH - 250, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill(GREEN)
    casa.build_local(screen)
    #casa.colisão(player)
    player.build_player(screen, dt, casa)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
