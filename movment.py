import pygame

class Movimento(pygame.sprite.Sprite):
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
        
        # "Hit-Box" da imagem do player
        self.TAM_HEIGHT = 47
        self.TAM_WIDTH = 25
        
        # Variáveis auxiliares para a velocidade do player e velocidade de mudança das sprites
        self.MOVMENT_SPEED = 200
        self.ATT_SPEED = 5
        
        self.player_pos = pygame.Vector2(640, 360) # Posiciona o player no centro da tela

        self.direction = 'down'
        self.atual = 0
        self.image = self.sprites[self.direction][self.atual]
    
    def update_sprite(self, dt):
        self.atual = (self.atual + dt * self.ATT_SPEED) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.atual)]
    
    def update_pos(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player_pos.y -= self.MOVMENT_SPEED * dt
            self.direction = 'up'
            self.update_sprite(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.player_pos.y += self.MOVMENT_SPEED * dt
            self.direction = 'down'
            self.update_sprite(dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player_pos.x -= self.MOVMENT_SPEED * dt
            self.direction = 'left'
            self.update_sprite(dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player_pos.x += self.MOVMENT_SPEED * dt
            self.direction = 'right'
            self.update_sprite(dt)
        
        self.clamp_position()
        
    def clamp_position(self):
        self.player_pos.x = max(self.TAM_WIDTH, min(self.player_pos.x, 1280 - self.TAM_WIDTH))
        self.player_pos.y = max(self.TAM_HEIGHT, min(self.player_pos.y, 720 - self.TAM_HEIGHT))
