import pygame
from settings import *
from imprime import Imprime

class Animal(Imprime):
    def __init__(self, especie, produto):
        self.especie = especie
        self.produto = produto
        self.qtd_produzido = 0

    def imprime(self, screen):
        screen.blit(FONTE1.render(f'Espécie do animal: {self.especie}', True, BLACK), (325, 185))
        screen.blit(FONTE1.render(f'Quantidade de {self.produto}: {self.qtd_produzido}', True, BLACK), (325, 210))
        screen.blit(FONTE1.render('C - Colher itens', True, BLACK), (325, 235))
    
    def atualiza_cercado(self):
        if self.especie == 'vaca':
            self.qtd_produzido += 2
        elif self.especie == 'galinha':
            self.qtd_produzido += 6
        elif self.especie == 'ovelha':
            self.qtd_produzido += 1