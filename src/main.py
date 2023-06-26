import pygame
from settings import *
from world import World

class Game:
    def __init__(self):
        # Inicialização do Pygame
        pygame.init()
        pygame.display.set_caption('Joguinho')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.__world = World()

        self.dt = 0
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            self.__world.build_world(self.screen, self.dt)
    
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()