import pygame
from settings import *

class Popup:
    def __init__(self):
        self.background_color = BLUE
        self.text_color = BLACK
        self.border_color = BLACK

        self.largura = WIDTH / 2
        self.altura = HEIGHT / 2

        self.pos_x = (WIDTH - self.largura) / 2
        self.pos_y = (HEIGHT - self.altura) / 2

        self.surface = pygame.Surface((self.largura, self.altura))
        self.close = False

        self.aux = 0
    
    def show_popup(self, screen):
        self.surface.fill(self.background_color)
        pygame.draw.rect(self.surface, self.border_color, pygame.Rect(0, 0, self.largura, self.altura), 2)
        screen.blit(self.surface, (self.pos_x, self.pos_y))
        self.show_close_button(screen)

    def show_close_button(self, screen):
        close_button_size = 20
        close_button_pos = (self.pos_x + self.largura - close_button_size - 5, self.pos_y + 5)
        pygame.draw.line(screen, self.text_color, close_button_pos, (close_button_pos[0] + close_button_size, close_button_pos[1] + close_button_size), 2)
        pygame.draw.line(screen, self.text_color, (close_button_pos[0] + close_button_size, close_button_pos[1]), (close_button_pos[0], close_button_pos[1] + close_button_size), 2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    if self.is_close_button_clicked(mouse_pos):
                        self.close_popup()

    def is_close_button_clicked(self, mouse_pos):
        close_button_size = 20
        close_button_pos = (self.pos_x + self.largura - close_button_size, self.pos_y)
        return (
            close_button_pos[0] <= mouse_pos[0] <= close_button_pos[0] + close_button_size and
            close_button_pos[1] <= mouse_pos[1] <= close_button_pos[1] + close_button_size
        )

    def close_popup(self):
        self.close = True
        self.aux = 0