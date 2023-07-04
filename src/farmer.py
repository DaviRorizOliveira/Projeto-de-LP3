import pygame
from settings import *
from interacoes import Interações

# Classe que faz a construção do player
class Farmer(pygame.sprite.Sprite):
    def __init__(self, inventario):
        pygame.sprite.Sprite.__init__(self)
        # Sprites do personagem
        self.sprites = {
            'down': [
                pygame.image.load('imagens/player_sprites/down_01.png'),
                pygame.image.load('imagens/player_sprites/down_02.png'),
                pygame.image.load('imagens/player_sprites/down_03.png')
            ],
            'left': [
                pygame.image.load('imagens/player_sprites/left_01.png'),
                pygame.image.load('imagens/player_sprites/left_02.png'),
                pygame.image.load('imagens/player_sprites/left_03.png')
            ],
            'right': [
                pygame.image.load('imagens/player_sprites/right_01.png'),
                pygame.image.load('imagens/player_sprites/right_02.png'),
                pygame.image.load('imagens/player_sprites/right_03.png')
            ],
            'up': [
                pygame.image.load('imagens/player_sprites/up_01.png'),
                pygame.image.load('imagens/player_sprites/up_02.png'),
                pygame.image.load('imagens/player_sprites/up_03.png')
            ]
        }

        self.stamina = 0
        self.dinheiro = 0
        self.nome = "Pedro"
        
        # "Hit-Box" da imagem do player
        self.TAM_HEIGHT = 47
        self.TAM_WIDTH = 25
        
        # Variáveis auxiliares para a velocidade do player e velocidade de mudança das sprites
        self.MOVMENT_SPEED = 200
        self.CHANGE_SPRITE_SPEED = 5
        
        # Posiciona o player no centro da tela
        self.player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)

        # Define a posição e a sprite inicial do personagem
        self.direction = 'down'
        self.atual = 0
        self.image = self.sprites[self.direction][self.atual]

        # Ferramentas do personagem
        self.tem_enxada = True
        self.vida_da_enxada = 5

        # Inventário do personagem, 1-tomates, 2-batatas, 3-trigo, 4-leite, 5-ovos, 6-lã
        self.qtd_tomate = 0
        self.qtd_batata = 0
        self.qtd_trigo = 0
        self.qtd_leite = 0
        self.qtd_ovo = 0
        self.qtd_la = 0

        # Criação das interações que ocorrem entre o personagem e os locais do mapa
        self.interações = Interações()
###############################################################################################
    def usa_enxada(self):
        self.vida_da_enxada -= 1
        if self.vida_da_enxada == 0:
            self.tem_enxada = False
###############################################################################################
    def get_inventario(self):
        return self.tem_enxada
###############################################################################################
    def get_stamina(self):
        return self.stamina
    def get_dinheiro(self):
        return self.dinheiro 
###############################################################################################
    def __verifica_inventario(self):
        if len(self.inventario) > 9:
            return False
        else:
            return True
###############################################################################################
    def set_inventario(self, item, quant):
        if self.__verifica_inventario:
            if item in self.inventario:
                self.inventario[item] += quant
            else:
                self.inventario[item] = quant
            
        else:
            print("Oops! O seu inventário está cheio!")
    def set_stamina(self, valor):
        self.stamina += valor
    def set_dinheiro(self, valor):
        self.dinheiro += valor
###############################################################################################
    def build_player(self, screen, dt, casa, cercado, farm, mercado, popup):
        screen.blit(self.image, self.player_pos - pygame.Vector2(self.image.get_size()) / 2)
        self.update_pos(dt, casa, cercado, farm, mercado, popup, screen)
###############################################################################################
    def update_sprite(self, dt):
        self.atual = (self.atual + dt * self.CHANGE_SPRITE_SPEED) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.atual)]
###############################################################################################
    def clamp_position(self, casa, cercado, mercado, farm):
        self.player_pos.x = max(self.TAM_WIDTH, min(self.player_pos.x, WIDTH - self.TAM_WIDTH))
        self.player_pos.y = max(self.TAM_HEIGHT, min(self.player_pos.y, HEIGHT - self.TAM_HEIGHT))

        if casa.is_collision(self):
            casa.handle_collision(self)
        if cercado.is_collision(self):
            cercado.handle_collision(self)
        if farm.is_collision(self):
            farm.handle_collision(self)
        if mercado.is_collision(self):
            mercado.handle_collision(self)
###############################################################################################
    def update_pos(self, dt, casa, cercado, farm, mercado, popup, screen):
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
        
        self.clamp_position(casa, cercado, mercado, farm)
        self.interações.testa_interações(self, casa, cercado, farm, mercado, popup, screen)