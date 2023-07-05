import pygame
from settings import *
from imprime import Imprime

class Planta(Imprime):
    def __init__(self, x, y):
        self.sprites = {
            'tomate': [
                pygame.image.load('imagens/tomate_sprites/tomate_01.png'),
                pygame.image.load('imagens/tomate_sprites/tomate_02.png'),
                pygame.image.load('imagens/tomate_sprites/tomate_03.png'),
                pygame.image.load('imagens/tomate_sprites/tomate_04.png')
            ],
            'batata': [
                pygame.image.load('imagens/batata_sprites/batata_01.png'),
                pygame.image.load('imagens/batata_sprites/batata_02.png'),
                pygame.image.load('imagens/batata_sprites/batata_03.png'),
                pygame.image.load('imagens/batata_sprites/batata_04.png')
            ],
            'trigo': [
                pygame.image.load('imagens/trigo_sprites/trigo_01.png'),
                pygame.image.load('imagens/trigo_sprites/trigo_02.png'),
                pygame.image.load('imagens/trigo_sprites/trigo_03.png'),
                pygame.image.load('imagens/trigo_sprites/trigo_04.png')
            ],
        }
        self.tipo_planta = None # Tipo da planta (Tomate, batata, trigo ou nenhum)
        self.idade = -1 # Idade da planta, ao chegar em um valor muito alto, a planta pode morrer
        self.sprite_atual = -1 # Sprite da planta atual com base na idade da planta
        self.image = pygame.image.load('imagens/terra.png') # Imagem que vai aparecer na tela
        self.pos_x = x # Posição na tela
        self.pos_y = y # Posição na tela
        self.status = '' # Status da planta (Crescendo, madura, morrendo, etc)

    def build_slot(self, screen):
        self.image = pygame.transform.scale(self.image, (45, 75))
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def atualiza_sprite(self):
        self.sprite_atual += 1
        if self.sprite_atual > 3:
            self.sprite_atual = 3
        self.image = self.sprites[self.tipo_planta][self.sprite_atual]

    def atualiza_idade(self):
        if self.tipo_planta is not None:
            self.idade += 1
            self.atualiza_sprite()

    def planta(self):
        self.idade = 0

    def getStatus(self):
        if self.idade == -1:
            self.status = 'Não há nada plantado aqui'
        elif self.idade >= 0 and self.idade < 4:
            self.status = 'A planta está crescendo'
        elif self.idade >= 4 and self.idade < 7:
            self.status = 'A planta está madura'
        elif self.idade >= 7 and self.idade < 10:
            self.status = 'A planta está morrendo'
        else:
            self.status = 'A planta morreu'

    def imprime(self, screen):
        self.getStatus()

        screen.blit(FONTE1.render(f'Tipo da planta: {self.tipo_planta}', True, BLACK), (325, 185))
        screen.blit(FONTE1.render(f'Status da planta: {self.status}', True, BLACK), (325, 235))
        screen.blit(FONTE1.render('C - Colher plantação', True, BLACK), (325, 260))
        screen.blit(FONTE1.render('Matenha pressionado P - Plantar semente', True, BLACK), (325, 285))