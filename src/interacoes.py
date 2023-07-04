import pygame
from settings import *

class Interações:
    def __init__(self):
        self.anterior = 0
    def testa_interações(self, player, casa, cercado, farm, mercado, popup, screen):
        keys = pygame.key.get_pressed()
        escolha = self.anterior

        if (player.player_pos.x + player.TAM_WIDTH + 20 > casa.rect.left and
                player.player_pos.x < casa.rect.right and
                player.player_pos.y + player.TAM_HEIGHT + 20 > casa.rect.top and
                player.player_pos.y - 20 < casa.rect.bottom):
            if keys[pygame.K_e]:
                popup.close = False
                popup.aux = 1
            if keys[pygame.K_ESCAPE]:
                popup.aux = 0
                popup.close = True
            if popup.close == False:
                popup.show_popup(screen)
                popup.handle_events()
                casa.popup_screen(screen, player)
                if keys[pygame.K_j]:
                    casa.passa_dia(farm, cercado)
                    popup.aux = 0
                    popup.close = True
###############################################################################################
        elif (player.player_pos.x + player.TAM_WIDTH + 20 > cercado.rect.left and
                player.player_pos.x - player.TAM_WIDTH - 20 < cercado.rect.right and
                player.player_pos.y + player.TAM_HEIGHT + 20 > cercado.rect.top and
                player.player_pos.y - 20 < cercado.rect.bottom):
            if keys[pygame.K_e]:
                popup.close = False
                popup.aux = 1
            if keys[pygame.K_ESCAPE]:
                popup.aux = 0
                popup.close = True
            if popup.close == False:
                popup.show_popup(screen)
                popup.handle_events()
###############################################################################################
        elif (player.player_pos.x + player.TAM_WIDTH + 20 > mercado.rect.left and
                player.player_pos.x - player.TAM_WIDTH - 20 < mercado.rect.right and
                player.player_pos.y + player.TAM_HEIGHT + 20 > mercado.rect.top and
                player.player_pos.y - 20 < mercado.rect.bottom):
            if keys[pygame.K_e]:
                popup.close = False
                popup.aux = 1
            if keys[pygame.K_ESCAPE]:
                popup.aux = 0
                popup.close = True
            if popup.close == False:
                popup.show_popup(screen)
                popup.handle_events()
                mercado.imprime(screen, player)
                if keys[pygame.K_1]:
                    mercado.faz_venda(player, 0)
                    popup.aux = 0
                    popup.close = True
                if keys[pygame.K_2]:
                    mercado.faz_venda(player, 1)
                    popup.aux = 0
                    popup.close = True
                if keys[pygame.K_3]:
                    mercado.faz_venda(player, 2)
                    popup.aux = 0
                    popup.close = True
                if keys[pygame.K_4]:
                    mercado.faz_venda(player, 3)
                    popup.aux = 0
                    popup.close = True
                if keys[pygame.K_5]:
                    mercado.faz_venda(player, 4)
                    popup.aux = 0
                    popup.close = True
                if keys[pygame.K_6]:
                    mercado.faz_venda(player, 5)
                    popup.aux = 0
                    popup.close = True
                if keys[pygame.K_7]:
                    player.tem_enxada = True
                    player.vida_da_enxada = 5
                    popup.aux = 0
                    popup.close = True
###############################################################################################
        elif (player.player_pos.x + player.TAM_WIDTH + 20 > farm.rect.left and
                player.player_pos.x - player.TAM_WIDTH - 20 < farm.rect.right and
                player.player_pos.y + player.TAM_HEIGHT + 20 > farm.rect.top and
                player.player_pos.y - 20 < farm.rect.bottom):
            if keys[pygame.K_1]:
                popup.close = False
                popup.aux = 1
                escolha = 0
            if keys[pygame.K_2]:
                popup.close = False
                popup.aux = 1
                escolha = 1
            if keys[pygame.K_3]:
                popup.close = False
                popup.aux = 1
                escolha = 2
            if keys[pygame.K_4]:
                popup.close = False
                popup.aux = 1
                escolha = 3
            if keys[pygame.K_5]:
                popup.close = False
                popup.aux = 1
                escolha = 4
            if keys[pygame.K_ESCAPE]:
                popup.aux = 0
                popup.close = True
            
            if popup.close == False:
                popup.show_popup(screen)
                popup.handle_events()
                farm.slots[escolha].imprime(screen)
                if keys[pygame.K_c]:
                    farm.verifica_colheita(escolha, player)
                    popup.aux = 0
                    popup.close = True
                if keys[pygame.K_p]:
                    screen.blit(FONTE1.render('Aperte i, j ou k', True, WHITE), (0, 0))
                    if keys[pygame.K_i]:
                        farm.coloca_semente(escolha, 'tomate', player)
                        popup.aux = 0
                        popup.close = True
                    if keys[pygame.K_j]:
                        farm.coloca_semente(escolha, 'batata', player)
                        popup.aux = 0
                        popup.close = True
                    if keys[pygame.K_k]:
                        farm.coloca_semente(escolha, 'trigo', player)
                        popup.aux = 0
                        popup.close = True
###############################################################################################
        else:
            popup.close = True
            popup.aux = 0
        self.anterior = escolha