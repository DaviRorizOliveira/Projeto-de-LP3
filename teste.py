class Farmer:
    def __init__(self, inventario,stamina,dinheiro, nome):
        self._inventario = inventario
        self._stamina = stamina
        self._dinheiro = dinheiro
        self._nome = nome

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

    @property   
    def inventario(self):
        return self.inventario
    
    @property
    def stamina(self):
        return self.stamina
    
    @property
    def dinheiro(self):
        return self.dinheiro  
    
    @inventario.setter
    def inventario(self, item, quant):
        self.inventario[item] = quant
        
    @stamina.setter
    def stamina(self, valor):
        self.stamina += valor

    @dinheiro.setter 
    def dinheiro(self, valor):
        self.dinheiro += valor

    