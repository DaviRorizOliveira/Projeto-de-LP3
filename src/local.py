import pygame
from settings import *

class Local(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.pos_x = x
        self.pos_y = y

    def build_local(self, screen, new_tam_x = None, new_tam_y = None):
        if new_tam_x != None:
            self.image = pygame.transform.scale(self.image, (new_tam_x, new_tam_y))
            screen.blit(self.image, (self.pos_x, self.pos_y))
            self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        else:
            screen.blit(self.image, (self.pos_x, self.pos_y))
            self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

    def is_collision(self, player):
        if (player.player_pos.x + player.TAM_WIDTH > self.rect.left and
                player.player_pos.x < self.rect.right and
                player.player_pos.y + player.TAM_HEIGHT > self.rect.top and
                player.player_pos.y < self.rect.bottom):
            return True
        return False

    def handle_collision(self, player):
        if player.player_pos.x < self.rect.left:
            player.player_pos.x = self.rect.left - player.TAM_WIDTH
        elif player.player_pos.x + player.TAM_WIDTH > self.rect.right:
            player.player_pos.x = self.rect.right
        if player.player_pos.y < self.rect.top:
            player.player_pos.y = self.rect.top - player.TAM_HEIGHT
        elif player.player_pos.y + player.TAM_HEIGHT > self.rect.bottom:
            player.player_pos.y = self.rect.bottom