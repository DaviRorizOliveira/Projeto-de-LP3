class Farmer:
    def __init__(self, inventario,stamina,dinheiro, nome):
        self._inventario = inventario
        self._stamina = stamina
        self._dinheiro = dinheiro
        self._nome = nome

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

    
