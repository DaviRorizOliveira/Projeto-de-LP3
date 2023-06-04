import pygame
from movment import Movimento

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

player = Movimento()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(GREEN)
    screen.blit(player.image, player.player_pos - pygame.Vector2(player.image.get_size()) / 2)
    player.update_pos(dt)
    pygame.display.flip()
    dt = clock.tick(60) / 1000
