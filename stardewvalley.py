import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

TAM = 7
parada = 0
status = 0
# 0 - espaço livre // 1 - cerca // 2 - casa // 3 - planta // 4 - mercado
mapa = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 3, 0, 0, 0, 2, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 4, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]
x = 2
y = 2

while parada > -1:
    for a in range(TAM):
        for b in range(TAM):
            if y == a and x == b:
                print("[]", end = '')
            elif mapa[a][b] == 1:
                print("\033[7;49;97m__\033[0m", end = '')
            elif mapa[a][b] == 0:
                print("  ", end='')
            elif mapa[a][b] == 2:
                print("\033[7;49;32m  \033[0m", end = '')
            elif mapa[a][b] == 3:
                print("\033[7;49;34m  \033[0m", end = '')
            elif mapa[a][b] == 4:
                print("\033[7;49;91m  \033[0m", end = '')
        print()
    print()
    if status == 1:
        print("Esta tecla não consta em nosso banco de dados")
        status -= 1

    mov = input()
    if mov == 'w' or mov == 'W':
        y -= 1
        if mapa[y][x] == 1:
            y += 1
    elif mov == 'a' or mov == 'A':
        x -= 1
        if mapa[y][x] == 1:
            x += 1
    elif mov == 's' or mov == 'S':
        y += 1
        if mapa[y][x] == 1:
            y -= 1
    elif mov == 'd' or mov == 'D':
        x += 1
        if mapa[y][x] == 1:
            x -= 1
    else:
        status += 1
    clear()