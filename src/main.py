import pygame
from settings import *
from farmer import Farmer
from local import Local
from popup import Popup

class Game:
    def __init__(self):
        # Inicialização do Pygame
        pygame.init()
        pygame.display.set_caption('Joguinho')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.dt = 0

        self.player = Farmer('inventario')
        self.casa = Local('imagens/house.png', WIDTH - 300, 0)
        self.cercado = Local('imagens/cercado.png', 0, 0)
        self.popup = Popup()
    
    def build_screen(self):
        background_image = pygame.image.load('imagens/grass_background.jpg')
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        self.screen.blit(background_image, (0, 0))
    
    def build_world(self):
        self.build_screen()
        self.casa.build_local(self.screen, 300, 300)
        self.cercado.build_local(self.screen, 250, 250)
        self.player.build_player(self.screen, self.dt, self.casa, self.cercado, self.popup)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            self.build_world()
    
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()