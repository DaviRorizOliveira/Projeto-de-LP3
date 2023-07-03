import pygame
from random import randrange
from settings import *
from local import Local
from converte import Converte
from imprime import Imprime

class Farm(Local, Converte, Imprime):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        super(Converte, self).__init__()


        self.largura_do_retangulo = 285
        self.altura_do_retangulo = 90
        self.pos_x = x
        self.pos_y = y

        self.terra = pygame.image.load('imagens/dirt_background.jpeg')

        self.atual = 0

        self.tipo = ['Tomate', 'Tomate', 'Batata', 'Trigo', '']
        #self.plant = plant
        #self.inv = inv

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
            ]
        }
        self.image = self.sprites['tomate'][self.atual]
###############################################################################################
    def plantar(self):
        tipo = 5
        self.inv.imprime()
        i, q = self.inv.get_inventario("Enxada", 1)
        #print(f"i = {i}")
        if i != "NULL":
            while tipo == 5:
                item = input("Qual item você quer utilizar(1 para sair)\n")
                if item == "1":
                    return 0
                elif item == "NULL":
                    print("Voce nao possui esse item")
                t, q = self.inv.get_inventario(item, 1)
                tipo = self.c_semente(t)
                if tipo != None:
                    while self.plant.get(tipo):
                        tipo = tipo + 10

                    a = [0, 0, 0, 0]
                    self.plant[tipo] = a
        else:
            print("Voce nao pode plantar! Compre uma enxada para poder plantar mais")
###############################################################################################
    def atualiza(self, chuva):
        self.__verifica_vida()

        for i in self.plant.keys():
            self.plant[i][0] = self.plant[i][0] + 1

            if self.plant[i][0] >= 5:
                self.plant[i][3] += 1
            elif chuva == 0:
                self.plant[i][1] += 1
                self.plant[i][2] = 0
            else:
                self.plant[i][2] += 1
###############################################################################################
    def regar(self):
        i, q = self.inv.get_inventario("Regador", 1)
        #print(f"i = {i}")
        if i != "NULL":
            for i in self.plant.keys():
                self.plant[i][2] = 0
###############################################################################################
    def __verifica_colheita(self, tipo):
        if self.plant == {}:
            print("Sua plantação esta vazia")
            return False
        elif self.plant[tipo][3] == 0:
            print("Essa planta não esta pronta para ser colhida")
            return False
        else:
            return True
###############################################################################################
    def colher(self):
        lista = []
        for i in self.plant.keys():
            if self.__verifica_colheita(i):
                lista.append(i)
                t = self.c_planta(i)
                q = randrange(1,6)
                print(f"Voce colheu {q} {t}")
                self.inv.set_inventario(t,q)
        for i in lista:
            self.plant.pop(i)
###############################################################################################
    def __verifica_vida(self):
        lista = []

        for i in self.plant.keys():
            if self.plant[i][1] == 3 or self.plant[i][2] == 3 or self.plant[i][3] == 3:
                print(f"A {self.c_planta(i)} morreu!!")
                lista.append(i)
                continue

            if self.plant[i][1] == 2:
                print(f"A {self.c_plant(i)} está perto de morrer!")
                continue

            if self.plant[i][2] == 2:
                print(f"A {self.c_plant(i)} está perto de morrer! Lembre de regar ela!!")
                continue

            if self.plant[i][3] == 2:
                print(f"A {self.c_plant(i)} está apodrecendo!! Lembre de colher a sua planta!!")
                continue

        for i in lista:
            self.plant.pop(i)
###############################################################################################
    def imprime(self):
      for i in self.plant.keys():
            print(f"i = {self.c_planta(i)}")
            print(f"{self.c_planta(i)}   Idade : {self.plant[i][0]} dias\nChuva : {self.plant[i][1]} dias\nFoi regada a {self.plant[i][2]} dias\nEstá madura a {self.plant[i][3]} dias")
###############################################################################################
    def build_local(self, screen):
        self.terra = pygame.transform.scale(self.terra, (self.largura_do_retangulo, self.altura_do_retangulo))
        self.rect = self.terra.get_rect(topleft=(self.pos_x, self.pos_y))
        screen.blit(self.terra, (self.pos_x, self.pos_y))
        #screen.blit('imagens/tomate_04.png', (self.pos_x, self.pos_y))
        self.slot(screen)
###############################################################################################
    def slot(self, screen):
        self.image = self.sprites['tomate'][self.atual]
        self.image = pygame.transform.scale(self.image, (45, 75))
        screen.blit(self.image, (self.pos_x + 10, self.pos_y + 5))

    def atualiza_sprite(self):
        self.atual += 1
        if self.atual > 3:
            self.atual = 0
        self.image = self.sprites['tomate'][self.atual]
###############################################################################################
    def popup_screen(self, screen):
        mensagem = [f"Slot {a + 1} - {tipo}" for a, tipo in enumerate(self.tipo)]
        interação = [FONTE1.render(msg, True, BLACK) for msg in mensagem]

        screen.blit(interação[0], (325, 185))
        screen.blit(interação[1], (325, 210))
        screen.blit(interação[2], (325, 235))
        screen.blit(interação[3], (325, 260))
        screen.blit(interação[4], (325, 285))