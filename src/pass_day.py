from random import randrange

class Passa_dia:
    def init(self, planta, cerca, loja, farmer):
        self.planta = planta
        self.cercado = cerca
        self.loja = loja
        self.farmer = farmer

    def passa(self):
        print("Chegou o fim de mais um dia")
        chuva = randrange(0,4)
        self.planta.atualiza(chuva)
        self.cerca.atualiza()
        if self.loja != 0:
            self.farmer.set_dinheiro(self.loja.atualiza_loja())
        self.farmer.set_stamina(10)