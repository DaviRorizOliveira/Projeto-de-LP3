class Farmer:
    def __init__(self):
        self.inventario = None
        self.stamina = 0
        self.dinheiro = 0
        self.nome = str()

    def movement(self, mov):
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
        
    def atualiza_inventario(self, item):
        self.inventario = item
        
    def atualiza_stamina(self, valor):
        self.stamina += valor
        
    def atualiza_dinheiro(self, valor):
        self.dinheiro += valor
        
    def get_inventario(self):
        return self.inventario
    
    def get_stamina(self):
        return self.stamina
    
    def get_dinheiro(self):
        return self.dinheiro