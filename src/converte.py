class Converte:
    def __init__(self):
        self.plantas = ["Batata", "Tomate", "Cenoura", "Trigo", "Morango"]
        self.animais = ["Vaca", "Galinha", "Ovelha"]

    def c_semente(self, tipo):
        match tipo:
            case "Broto de Batata":
                return 0

            case "Semente de Tomate":
                return 1

            case "Muda de Cenoura":
                return 2

            case "Semente de Trigo":
                return 3

            case "Muda de Morango":
                return 4

    def c_cercado(self, tipo):
        match tipo:
            case "Vaca":
                return 0

            case "Galinha":
                return 1

            case "Ovelha":
                return 2

    def c_planta(self, tipo):
        if tipo == None:
            return tipo
        else:
            return self.plantas[tipo % 10]

    def c_animal(self, tipo):
        return self.animais[tipo % 10]

    def carne(self, t):
        match t:
            case 0:
                return "Carne de Vaca"
            case 1:
                return "Carne de Galinha"
            case 2:
                return "Carne de Ovelha"