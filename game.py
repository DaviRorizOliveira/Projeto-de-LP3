import pygame

width = 1280 # Largura da tela
height = 720 # Altura da tela
TAM_HEIGHT = 47 # Altura da personagem
TAM_WIDTH = 25 # Largura da personagem
mov = 200 # Velocidade de movimentação
dt = 0 # Variável que controla a velocidade de movimentação do personagem
att = 5 # Variável que controla a velocidade de mudança de sprites da movimentação

GREEN = (50, 169, 62) # Definição da cor verde

# Cabeçalho inicial do pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Sprites')

# Define a posição incial do jogador no centro da tela
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) # Posição inicial do player

# Classe teste que futuramente será excluída do main e implenetada na classe do Farmer
class Teste(pygame.sprite.Sprite):
    # Construtor da classe
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Define a direção inicial do personagem
        self.direction = 'down'
        # Dicionário que guarda as imagens a serem utilizadas no sprite de animação da movimentação
        self.sprites = {
            'down': [ # Para baixo
                pygame.image.load('Sprites/down_01.png'),
                pygame.image.load('Sprites/down_02.png'),
                pygame.image.load('Sprites/down_03.png')
            ],
            'left': [ # Para a esquerda
                pygame.image.load('Sprites/left_01.png'),
                pygame.image.load('Sprites/left_02.png'),
                pygame.image.load('Sprites/left_03.png')
            ],
            'right': [ # Para a direita
                pygame.image.load('Sprites/right_01.png'),
                pygame.image.load('Sprites/right_02.png'),
                pygame.image.load('Sprites/right_03.png')
            ],
            'up': [ # Para cima
                pygame.image.load('Sprites/up_01.png'),
                pygame.image.load('Sprites/up_02.png'),
                pygame.image.load('Sprites/up_03.png')
            ]
        }
        # Define a imagem inicial do personagem (Primeira imagem voltada para baixo)
        self.atual = 0
        self.image = self.sprites[self.direction][self.atual]
    # Método que faz a atualização das imagens conforme a direção
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

player = Teste() # Chamada da classe para a construção do personagem

# Loop principal
while True:
    # Encerra o jogo ao fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # Cor do background
    screen.fill(GREEN)
    # Desenho do player
    screen.blit(player.image, player_pos - pygame.Vector2(player.image.get_size()) / 2)
    
    # Movimentação do player
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] or keys[pygame.K_UP]: # Movimentação para cima
        player_pos.y -= mov * dt
        player.direction = 'up' # Atualiza a direção do player
        # Se for a última imagem da direção que o personagem está voltado, ele retorna para a primeira imagem
        if player.atual >= len(player.sprites[player.direction]) - 1:
            player.atual = 0
        else:
            player.atual += dt * att # Aumenta o fator para diminuir a velocidade da animação
        player.image = player.sprites[player.direction][int(player.atual)]
    
    if keys[pygame.K_s] or keys[pygame.K_DOWN]: # Movimentação para baixo
        player_pos.y += mov * dt
        player.direction = 'down' # Atualiza a direção do player
        # Se for a última imagem da direção que o personagem está voltado, ele retorna para a primeira imagem
        if player.atual >= len(player.sprites[player.direction]) - 1:
            player.atual = 0
        else:
            player.atual += dt * att # Aumenta o fator para diminuir a velocidade da animação
        player.image = player.sprites[player.direction][int(player.atual)]
    
    if keys[pygame.K_a] or keys[pygame.K_LEFT]: # Movimentação para a esquerda
        player_pos.x -= mov * dt
        player.direction = 'left' # Atualiza a direção do player
        # Se for a última imagem da direção que o personagem está voltado, ele retorna para a primeira imagem
        if player.atual >= len(player.sprites[player.direction]) - 1:
            player.atual = 0
        else:
            player.atual += dt * att # Aumenta o fator para diminuir a velocidade da animação
        player.image = player.sprites[player.direction][int(player.atual)]
    
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # Movimentação para a direita
        player_pos.x += mov * dt
        player.direction = 'right' # Atualiza a direção do player
        # Se for a última imagem da direção que o personagem está voltado, ele retorna para a primeira imagem
        if player.atual >= len(player.sprites[player.direction]) - 1:
            player.atual = 0
        else:
            player.atual += dt * att # Aumenta o fator para diminuir a velocidade da animação
        player.image = player.sprites[player.direction][int(player.atual)]
    
    # Limita a posição do player na tela
    if player_pos.x <= TAM_WIDTH:
        player_pos.x = TAM_WIDTH
    if player_pos.y <= TAM_HEIGHT:
        player_pos.y = TAM_HEIGHT
    if player_pos.x >= width - TAM_WIDTH:
        player_pos.x = width - TAM_WIDTH
    if player_pos.y >= height - TAM_HEIGHT:
        player_pos.y = height - TAM_HEIGHT

    pygame.display.flip()

    # Variável para limitar a velocidade do player em 60 FPS
    dt = clock.tick(60) / 1000