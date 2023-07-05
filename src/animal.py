import pygame
from settings import *
from imprime import Imprime

class Animal(Imprime):
    def __init__(self, especie, produto):
        self.especie = especie
        self.produto = produto
        self.qtd_produzido = 0
        self.alimentado = False

    def imprime(self, screen):
        screen.blit(FONTE1.render(f'Espécie do animal: {self.especie}', True, BLACK), (325, 185))
        screen.blit(FONTE1.render(f'Quantidade de {self.produto}: {self.qtd_produzido}', True, BLACK), (325, 210))
        screen.blit(FONTE1.render('C - Colher itens', True, BLACK), (325, 235))
        screen.blit(FONTE1.render('A - alimentar', True, BLACK), (325, 260))
    
    def atualiza_cercado(self):
        if self.especie == 'vaca' and self.alimentado != False:
            self.qtd_produzido += 2
        elif self.especie == 'galinha' and self.alimentado != False:
            self.qtd_produzido += 6
        elif self.especie == 'ovelha' and self.alimentado != False:
            self.qtd_produzido += 1