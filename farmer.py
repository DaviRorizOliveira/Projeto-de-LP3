class Farmer:
    def __init__(self, inventario):
        self.inventario = inventario
        self.stamina = 0
        self.dinheiro = 0.0
        self.nome = "Pedro"
 
    def get_inventario(self):
        return self.inventario
    
    
    def get_stamina(self):
        return self.stamina
    

    def get_dinheiro(self):
        return self.dinheiro 

    def __verifica_inventario(self):
        if len(self.inventario) > 9:
            return False
        else:
            return True
    
    
    def set_inventario(self, item, quant):
        if self.__verifica_inventario:
            if item in self.inventario:
                self.inventario[item] += quant
            else:
                self.inventario[item] = quant
            
        else:
            print("Oops! O seu inventário está cheio!")
        

    def set_stamina(self, valor):
        self.stamina += valor

     
    def set_dinheiro(self, valor):
        self.dinheiro += valor


    
