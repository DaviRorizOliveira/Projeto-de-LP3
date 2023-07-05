import pygame
from settings import *
from world import World

# Classe main que roda o jogo
class Game:
    def __init__(self):
        # Inicialização do Pygame
        pygame.init()
        pygame.display.set_caption('Fazendinha Feliz')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # Chamada da classe World para construir o mundo no loop principal
        self.world = World()

        # Delta time
        self.dt = 0

    def run(self):
        self.world.main_menu(self.screen, self.dt, self.clock)

if __name__ == '__main__':
    game = Game()
    game.run()