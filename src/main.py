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

        # Chamada da classe World para construir o mundo no loop principal
        self.world = World()

        # Delta time
        self.dt = 0

    def run(self):
        # Loop principal do jogo
        while True:
            # Caso o jogador queira encerrar o jogo clicando no X da janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Construção do mundo com a chamada do build_world, passando como parâmetros a tela (screen) e o delta time (dt)
            self.world.build_world(self.screen, self.dt)

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()