import pygame
from setup import *

class Local(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.house = pygame.transform.scale(self.image, (250, 250))
        self.rect = self.house.get_rect(topleft=(x, y))

    def build_local(self, screen):
        screen.blit(self.house, (WIDTH - 250, 0))

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
