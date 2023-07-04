import pygame
from settings import *

class Testes:
    def __init__(self):
        self.anterior = 0
    def faz_testes(self, player, casa, cercado, farm, mercado, popup, screen):
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