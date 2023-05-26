import pygame

# Configurações da tela
WIDTH = 1280
HEIGHT = 720

# Configurações do jogador
TAM_HEIGHT = 47
TAM_WIDTH = 25
MOVMENT_SPEED = 200
ATT_SPEED = 5
dt = 0

# Cores
GREEN = (50, 169, 62)

# Inicialização do pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Sprites')

class Farmer(pygame.sprite.Sprite):
    # Construtor da classe
    def __init__(self):
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
    
    def update_pos(self, dt):
        screen.blit(self.image, self.player_pos - pygame.Vector2(self.image.get_size()) / 2)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player_pos.y -= MOVMENT_SPEED * dt
            self.direction = 'up'
            if self.atual >= len(self.sprites[self.direction]) - 1:
                self.atual = 0
            else:
                self.atual += dt * ATT_SPEED
            self.image = self.sprites[self.direction][int(self.atual)]      
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.player_pos.y += MOVMENT_SPEED * dt
            self.direction = 'down'
            if self.atual >= len(self.sprites[self.direction]) - 1:
                self.atual = 0
            else:
                self.atual += dt * ATT_SPEED
            self.image = self.sprites[self.direction][int(self.atual)]
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player_pos.x -= MOVMENT_SPEED * dt
            self.direction = 'left'
            if self.atual >= len(self.sprites[self.direction]) - 1:
                self.atual = 0
            else:
                self.atual += dt * ATT_SPEED
            self.image = self.sprites[self.direction][int(self.atual)]
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player_pos.x += MOVMENT_SPEED * dt
            self.direction = 'right'
            if self.atual >= len(self.sprites[self.direction]) - 1:
                self.atual = 0
            else:
                self.atual += dt * ATT_SPEED
            self.image = self.sprites[self.direction][int(self.atual)]
        
        self.clamp_position()
        
    def clamp_position(self):
        self.player_pos.x = max(TAM_WIDTH, min(self.player_pos.x, WIDTH - TAM_WIDTH))
        self.player_pos.y = max(TAM_HEIGHT, min(self.player_pos.y, HEIGHT - TAM_HEIGHT))

player = Farmer()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill(GREEN)
    player.update_pos(dt)

    pygame.display.flip()

    dt = clock.tick(60) / 1000