import pygame

class Movimento(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
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
        self.TAM_HEIGHT = 47
        self.TAM_WIDTH = 25
        self.MOVMENT_SPEED = 200
        self.ATT_SPEED = 5
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.direction = 'down'
        self.atual = 0
        self.image = self.sprites[self.direction][self.atual]
    
    def update_sprite(self):
        if self.direction == 'down':
            self.atual = (self.atual + 1) % len(self.sprites[self.direction])
            self.image = self.sprites[self.direction][self.atual]
        elif self.direction == 'left':
            self.atual = (self.atual + 1) % len(self.sprites[self.direction])
            self.image = self.sprites[self.direction][self.atual]
        elif self.direction == 'right':
            self.atual = (self.atual + 1) % len(self.sprites[self.direction])
            self.image = self.sprites[self.direction][self.atual]
        elif self.direction == 'up':
            self.atual = (self.atual + 1) % len(self.sprites[self.direction])
            self.image = self.sprites[self.direction][self.atual]
    
    def update_pos(self, dt, screen, WIDTH, HEIGHT):
        screen.blit(self.image, self.player_pos - pygame.Vector2(self.image.get_size()) / 2)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player_pos.y -= self.MOVMENT_SPEED * dt
            self.direction = 'up'
            if self.atual >= len(self.sprites[self.direction]) - 1:
                self.atual = 0
            else:
                self.atual += dt * self.ATT_SPEED
            self.image = self.sprites[self.direction][int(self.atual)]      
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.player_pos.y += self.MOVMENT_SPEED * dt
            self.direction = 'down'
            if self.atual >= len(self.sprites[self.direction]) - 1:
                self.atual = 0
            else:
                self.atual += dt * self.ATT_SPEED
            self.image = self.sprites[self.direction][int(self.atual)]
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player_pos.x -= self.MOVMENT_SPEED * dt
            self.direction = 'left'
            if self.atual >= len(self.sprites[self.direction]) - 1:
                self.atual = 0
            else:
                self.atual += dt * self.ATT_SPEED
            self.image = self.sprites[self.direction][int(self.atual)]
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player_pos.x += self.MOVMENT_SPEED * dt
            self.direction = 'right'
            if self.atual >= len(self.sprites[self.direction]) - 1:
                self.atual = 0
            else:
                self.atual += dt * self.ATT_SPEED
            self.image = self.sprites[self.direction][int(self.atual)]
        
        self.clamp_position(WIDTH, HEIGHT)
        
    def clamp_position(self, WIDTH, HEIGHT):
        self.player_pos.x = max(self.TAM_WIDTH, min(self.player_pos.x, WIDTH - self.TAM_WIDTH))
        self.player_pos.y = max(self.TAM_HEIGHT, min(self.player_pos.y, HEIGHT - self.TAM_HEIGHT))