import pygame
from settings import *
from imprime import Imprime

class Animal(Imprime):
    def __init__(self, especie, produto):
        self.especie = especie # Espécie do animal: Vaca, galinha ou ovelha
        self.produto = produto # Produto que o animal vai produzir: Leite, ovos ou lã
        self.qtd_produzido = 0 # Quantidade do produto produzido
        self.alimentado = False

    # Método que imprime as interações disponíveis
    def imprime(self, screen):
        screen.blit(FONTE1.render(f'Espécie do animal: {self.especie}', True, BLACK), (325, 185))
        screen.blit(FONTE1.render(f'Quantidade de {self.produto}: {self.qtd_produzido}', True, BLACK), (325, 210))
        screen.blit(FONTE1.render('C - Colher itens', True, BLACK), (325, 235))
        screen.blit(FONTE1.render('A - alimentar', True, BLACK), (325, 260))
    
    # Método que atualiza o cercado ao passar o dia, caso os animais tenham sido alimentados
    def atualiza_cercado(self):
        if self.especie == 'vaca' and self.alimentado != False:
            self.qtd_produzido += 2
        elif self.especie == 'galinha' and self.alimentado != False:
            self.qtd_produzido += 6
        elif self.especie == 'ovelha' and self.alimentado != False:
            self.qtd_produzido += 1