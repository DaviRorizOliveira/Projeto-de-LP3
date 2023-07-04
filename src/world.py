import pygame
from settings import *
from farmer import Farmer
from popup import Popup
from farm import Farm
from casa import Casa
from button import Button
from cercado import Cercado
from mercado import Mercado

class World:
    def __init__(self):
        self.player = Farmer('inventario')
        self.popup = Popup()

        self.casa = Casa('imagens/house.png', WIDTH - 300, 0)
        self.cercado = Cercado('imagens/cercado.png', 0, 0)
        self.farm = Farm('imagens/dirt_background.jpeg', 10, HEIGHT - 100)
        self.mercado = Mercado('imagens/mercado.png', WIDTH / 2 - 150, 0)

        self.lista_de_locais = []
        self.lista_de_locais.append(self.casa)
        self.lista_de_locais.append(self.cercado)
        self.lista_de_locais.append(self.farm)
###############################################################################################
    def build_screen(self, screen):
        background_image = pygame.image.load('imagens/grass_background.jpg')
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        screen.blit(background_image, (0, 0))
###############################################################################################
    def build_world(self, screen, dt):
        self.farm.build_local(screen)
        self.casa.build_local(screen, 300, 300)
        self.cercado.build_local(screen, 300, 300)
        self.mercado.build_local(screen, 300, 300)
        self.player.build_player(screen, dt, self.casa, self.cercado, self.farm, self.mercado, self.popup)

        screen.blit(FONTE1.render(f'Dia atual: {self.casa.dia}', True, WHITE), (WIDTH - 150, HEIGHT - 30))
###############################################################################################
    def play(self, screen, dt, clock):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            self.build_screen(screen)
            self.build_world(screen, dt)

            pygame.display.flip()
            dt = clock.tick(60) / 1000
###############################################################################################
    def main_menu(self, screen, dt, clock):
        while True:
            screen.fill(WHITE)
            mouse_pos = pygame.mouse.get_pos()
            main_text = get_font(75).render("FAZENDINHA FELIZ", True, BLACK)
            main_rect = main_text.get_rect(center=(640, 100))
            
            play_button = Button('imagens/play_rect.png', (640, 250), "PLAY", get_font(75), BLACK, WHITE)
            tutorial_button = Button('imagens/tutorial_rect.png', (640, 400), "TUTORIAL", get_font(75), BLACK, WHITE)
            quit_button = Button('imagens/quit_rect.png', (640, 550), "QUIT", get_font(75), BLACK, WHITE)

            screen.blit(main_text,main_rect)

            for button in [play_button, tutorial_button, quit_button]:
                button.changeColor(mouse_pos)
                button.update(screen)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(mouse_pos):
                        self.play(screen, dt, clock)
                    if tutorial_button.checkForInput(mouse_pos):
                        self.tutorial(screen, dt, clock)
                    if quit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        quit()

            pygame.display.update()
###############################################################################################
    def tutorial(self, screen, dt, clock):
        while True:
            screen.fill(WHITE)
            mouse_pos = pygame.mouse.get_pos()

            tutorial_text = get_font(45).render("This is the OPTIONS screen.", True, "Black")
            tutorial_rect = tutorial_text.get_rect(center=(640, 260))
            screen.blit(tutorial_text, tutorial_rect)

            back_button = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

            back_button.changeColor(mouse_pos)
            back_button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.checkForInput(mouse_pos):
                        self.main_menu(screen, dt, clock)

            pygame.display.update()
###############################################################################################