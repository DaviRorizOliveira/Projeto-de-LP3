import pygame
from setup import *

class Movimento(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Sprites do personagem
        self.sprites = {
            'down': [
                pygame.image.load('Sprites/down_01.png'),
                pygame.image.load('Sprites/down_02.png'),
                pygame.image.load('Sprites/down_03.png')
            ],
            'left': [
                pygame.image.load('Sprites/left_01.png'),
                pygame.image.load('Sprites/left_02.png'),
                pygame.image.load('Sprites/left_03.png')
            ],
            'right': [
                pygame.image.load('Sprites/right_01.png'),
                pygame.image.load('Sprites/right_02.png'),
                pygame.image.load('Sprites/right_03.png')
            ],
            'up': [
                pygame.image.load('Sprites/up_01.png'),
                pygame.image.load('Sprites/up_02.png'),
                pygame.image.load('Sprites/up_03.png')
            ]
        }
        
        # "Hit-Box" da imagem do player
        self.TAM_HEIGHT = 47
        self.TAM_WIDTH = 25
        
        # Variáveis auxiliares para a velocidade do player e velocidade de mudança das sprites
        self.MOVMENT_SPEED = 200
        self.ATT_SPEED = 5
        
        self.player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2) # Posiciona o player no centro da tela

        self.direction = 'down'
        self.atual = 0
        self.image = self.sprites[self.direction][self.atual]
    
    def build_player(self, screen, dt, local, popup):
        screen.blit(self.image, self.player_pos - pygame.Vector2(self.image.get_size()) / 2)
        self.update_pos(dt, local, popup, screen)
    
    def update_sprite(self, dt):
        self.atual = (self.atual + dt * self.ATT_SPEED) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.atual)]
    
    def clamp_position(self):
        self.player_pos.x = max(self.TAM_WIDTH, min(self.player_pos.x, WIDTH - self.TAM_WIDTH))
        self.player_pos.y = max(self.TAM_HEIGHT, min(self.player_pos.y, HEIGHT - self.TAM_HEIGHT))
    
    def update_pos(self, dt, local, popup, screen):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -self.MOVMENT_SPEED * dt
            self.direction = 'up'
            self.update_sprite(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = self.MOVMENT_SPEED * dt
            self.direction = 'down'
            self.update_sprite(dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -self.MOVMENT_SPEED * dt
            self.direction = 'left'
            self.update_sprite(dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = self.MOVMENT_SPEED * dt
            self.direction = 'right'
            self.update_sprite(dt)

        new_player_pos = self.player_pos + pygame.Vector2(dx, dy)

        self.player_pos = new_player_pos
        self.clamp_position()

        if local.is_collision(self):
            local.handle_collision(self)
        
        if (self.player_pos.x + self.TAM_WIDTH + 20 > local.rect.left and
                self.player_pos.x < local.rect.right and
                self.player_pos.y + self.TAM_HEIGHT > local.rect.top and
                self.player_pos.y - 20 < local.rect.bottom):
            
            if keys[pygame.K_e]:
                if popup.ca == 1:
                    popup.ca = 0
                    popup.close = True
                else:
                    popup.close = False
                    popup.ca = 1
            if popup.close == False:
                popup.show_popup(screen)
                popup.handle_events()
        else:
            popup.close = True
            popup.ca = 0
