import pygame
from settings import *
from imprime import Imprime
from local import Local

class Mercado(Local, Imprime):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    # Método que realiza a venda dos itens do inventário do jogador conforme a escolha (1 a 9 no popup de interações) e retorna o valor por
    # unidade de cada produto vendido, cada produto tem um valor diferente
    def faz_venda(self, player, escolha):
        if escolha == 0:
            if player.qtd_tomate != 0:
                recebido = player.qtd_tomate * CUSTO_TOMATE
                player.qtd_tomate = 0
                player.dinheiro += recebido
        elif escolha == 1:
            if player.qtd_batata != 0:
                recebido = player.qtd_batata * CUSTO_BATATA
                player.qtd_batata = 0
                player.dinheiro += recebido
        elif escolha == 2:
            if player.qtd_trigo != 0:
                recebido = player.qtd_trigo * CUSTO_TRIGO
                player.qtd_trigo = 0
                player.dinheiro += recebido
        elif escolha == 3:
            if player.qtd_leite != 0:
                recebido = player.qtd_leite * CUSTO_LEITE
                player.qtd_leite = 0
                player.dinheiro += recebido
        elif escolha == 4:
            if player.qtd_ovo != 0:
                recebido = player.qtd_ovo * CUSTO_OVO
                player.qtd_ovo = 0
                player.dinheiro += recebido
        elif escolha == 5:
            if player.qtd_la != 0:
                recebido = player.qtd_la * CUSTO_LA
                player.qtd_la = 0
                player.dinheiro += recebido
        else:
            pass
    
    # Método que realiza a compra da enxada
    def compra_enxada(self, player):
        player.tem_enxada = True
        player.vida_da_enxada = 5
        player.dinheiro -= CUSTO_ENXADA
    
    # Método que compra 2 sementes da planta escolhida
    def compra_semente(self, player, semente):
        if semente == 'tomate':
            player.s_tomate += 2
            player.dinheiro -= CUSTO_SEMENTE
        if semente == 'batata':
            player.s_batata += 2
            player.dinheiro -= CUSTO_SEMENTE
        if semente == 'trigo':
            player.s_trigo += 2
            player.dinheiro -= CUSTO_SEMENTE

    # Imprime o popup de interações
    def imprime(self, screen, player):
        screen.blit(FONTE1.render(f'1 - Tens {player.qtd_tomate} tomates, deseja vender?', True, BLACK), (325, 185))
        screen.blit(FONTE1.render(f'2 - Tens {player.qtd_batata} batatas, deseja vender?', True, BLACK), (325, 210))
        screen.blit(FONTE1.render(f'3 - Tens {player.qtd_trigo} quilos de trigo, deseja vender?', True, BLACK), (325, 235))
        screen.blit(FONTE1.render(f'4 - Tens {player.qtd_leite} litros de leite, deseja vender?', True, BLACK), (325, 260))
        screen.blit(FONTE1.render(f'5 - Tens {player.qtd_ovo} ovos, deseja vender?', True, BLACK), (325, 285))
        screen.blit(FONTE1.render(f'6 - Tens {player.qtd_la} quilos de lã, deseja vender?', True, BLACK), (325, 310))
        screen.blit(FONTE1.render(f'7 - Tens {player.s_tomate} sementes de tomate, deseja comprar 2?', True, BLACK), (325, 335))
        screen.blit(FONTE1.render(f'8 - Tens {player.s_batata} sementes de batata, deseja comprar 2?', True, BLACK), (325, 360))
        screen.blit(FONTE1.render(f'9 - Tens {player.s_trigo} sementes de trigo, deseja comprar 2?', True, BLACK), (325, 385))

        if player.tem_enxada == False:
            screen.blit(FONTE1.render('0 - Você não tem enxada para plantar,', True, BLACK), (325, 410))
            screen.blit(FONTE1.render('deseja comprar uma?', True, BLACK), (325, 435))
        else:
            pass