import pygame
from random import randrange
from converte import Converte

class Cercado(Converte):
    def __init__(self, cerca):
        # O atributo abaixo recebe o código de uma planta como chave e uma lista
        # com quatro ints. Os significados dos valores seguem são os seguintes:
        # 0. Dias desde que incluido
        # 1. Dias sem comida
        # 2. Dias sem água

        self.cerca = cerca

    def incluir(self, t):
        tipo = self.c_cercado(t)
        while self.cerca.get(tipo):
            tipo = tipo + 10

        a = [0, 0, 0]
        self.cerca[tipo] = a

    def atualiza(self):
        self.verifica_vida()

        for i in self.cerca.keys():
            self.cerca[i][0] = self.cerca[i][0] + 1

            self.cerca[i][1] = self.cerca[i][1] + 1
            self.cerca[i][2] = self.cerca[i][2] + 1

    def dar_agua(self):
        for i in self.cerca.keys():
            self.cerca[i][2] = 0

    def dar_comida(self):
        for i in self.cerca.keys():
            self.cerca[i][1] = 0

    def recolher(self, t, m):
        tipo = self.c_cercado(t)

        if m == False:
            if tipo == 0:
                return "Leite", randrange(1, 6)

            elif tipo == 1:
                return "Ovos", randrange(1, 6)

            else:
                return "Lã", randrange(1, 6)

        else:
            return self.carne(tipo), randrange(1, 6)

    def __verifica_vida(self):
        lista = []

        for i in self.cerca.keys():
            if self.cerca[i][0] == 10 or self.cerca[i][1] == 3 or self.cerca[i][2] == 3:
                print(f"A sua {self.converte.c_animal(i)} morreu!!")
                lista.append(i)
                continue

            if self.cerca[i][0] == 9:
                print(
                    f"A {self.c_animal(i)} está perto de morrer de velhice !!"
                )

            if self.cerca[i][1] == 2:
                print(
                    f"A {self.c_animal(i)} está perto de morrer! Lembre de alimentar ela!!"
                )

            if self.cerca[i][2] == 2:
                print(
                    f"A {self.c_animal(i)} está com sede!! Lembre de dar água para ela!!"
                )

        for i in lista:
            self.cerca.pop(i)
    
    def imprime(self):
      for i in self.cerca.keys():
        print(f"{self.c_animal(i)}   Idade : {self.dic[i][0]} dias\nFoi alimentado a {self.dic[i][1]} dias\nRecebeu agua a {self.dic[i][2]} dias")