#import pygame
#from pygame.locals import *
#from sys import exit

#pygame.init()

#largura = 640
#altura = 480

#tela = pygame.display.set_mode((largura, altura))
#pygame.display.set_caption('Stardew Valley')

#while True:
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            exit()
#    pygame.display.update()

import os

# limpa a tela
os.system('cls' if os.name == 'nt' else 'clear')

# leitura do caractere sem precisar pressionar enter
import msvcrt if os.name == 'nt' else import termios
def getch():
    if os.name == 'nt':
        return msvcrt.getch().decode('utf-8')
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# leitura do caractere e limpeza do buffer de entrada
char = getch()
while msvcrt.kbhit():
    msvcrt.getch()

# processamento do caractere
if char == 'a':
    print('Caractere "a" lido')
else:
    print('Outro caractere lido')
