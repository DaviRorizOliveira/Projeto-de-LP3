import pygame
from settings import *
from imprime import Imprime
from local import Local

class Mercado(Local, Imprime):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

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

    def imprime(self, screen, player):
        screen.blit(FONTE1.render(f'1 - Você tem {player.qtd_tomate} tomates, deseja vender?', True, BLACK), (325, 185))
        screen.blit(FONTE1.render(f'2 - Você tem {player.qtd_batata} batatas, deseja vender?', True, BLACK), (325, 210))
        screen.blit(FONTE1.render(f'3 - Você tem {player.qtd_trigo} quilos de trigo, deseja vender?', True, BLACK), (325, 235))
        screen.blit(FONTE1.render(f'4 - Você tem {player.qtd_leite} litros de leite, deseja vender?', True, BLACK), (325, 260))
        screen.blit(FONTE1.render(f'5 - Você tem {player.qtd_ovo} ovos, deseja vender?', True, BLACK), (325, 285))
        screen.blit(FONTE1.render(f'6 - Você tem {player.qtd_la} quilos de lã, deseja vender?', True, BLACK), (325, 310))
        if player.tem_enxada == False:
            screen.blit(FONTE1.render('7 - Você não tem enxada para plantar,', True, BLACK), (325, 335))
            screen.blit(FONTE1.render('deseja comprar uma?', True, BLACK), (325, 360))
        else:
            pass