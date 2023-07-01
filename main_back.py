from random import randrange


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
            
class Imprime():
    
    def imprime(self):
        raise NotImplementedError("A classe precisa ser capaz de imprimir")
    

class Planta(Converte,Imprime):
    def __init__(self, plant,inv):
        # O atributo abaixo recebe o código de uma planta como chave e uma lista
        # com quatro ints. Os significados dos valores seguem são os seguintes:
        # 0. Dias desde que foi plantado
        # 1. Dias em que a planta pegou chuva
        # 2. Dias sem ser regada
        # 3. Dias após a planta estar pronta para ser colhida
        self.plant = plant
        self.inv = inv
        super().__init__()

    def plantar(self):
        tipo = 5
        self.inv.imprime()
        i,q = self.inv.get_inventario("Enxada",1)
        print(f"i = {i}")
        if i != "NULL":
            while tipo == 5:
                item = input("Qual item você quer utilizar(1 para sair)\n")
                if item == "1":
                    return 0
                elif item == "NULL":
                    print("Voce nao possui esse item")
                t,q = self.inv.get_inventario(item,1)
                tipo = self.c_semente(t)
                if tipo != None:
                    while self.plant.get(tipo):
                        tipo = tipo + 10
                
                    a = [0, 0, 0, 0]
                    self.plant[tipo] = a
        else:
            print("Voce nao pode plantar! Compre uma enxada para poder plantar mais")

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

    def regar(self):
        i,q = self.inv.get_inventario("Enxada",1)
        print(f"i = {i}")
        if i != "NULL":
            for i in self.plant.keys():
                self.plant[i][2] = 0

    def __verifica_colheita(self,tipo):
        if self.plant == {}:
          print("Sua plantação esta vazia")
          return False
        elif self.plant[tipo][3] == 0:
          print("Essa planta não esta pronta para ser colhida")
          return False

        else:
          return True
          

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
                print(
                    f"A {self.c_plant(i)} está perto de morrer! Lembre de regar ela!!"
                )
                continue

            if self.plant[i][3] == 2:
                print(
                    f"A {self.c_plant(i)} está apodrecendo!! Lembre de colher a sua planta!!"
                )
                continue

        for i in lista:
            self.plant.pop(i)
   
    def imprime(self):
      for i in self.plant.keys():
            print(f"i = {self.c_planta(i)}")
            print(f"{self.c_planta(i)}   Idade : {self.plant[i][0]} dias\nChuva : {self.plant[i][1]} dias\nFoi regada a {self.plant[i][2]} dias\nEstá madura a {self.plant[i][3]} dias")

class Cercado(Converte,Imprime):
    def __init__(self, cerca,inventario):
        # O atributo abaixo recebe o código de uma planta como chave e uma lista
        # com quatro ints. Os significados dos valores seguem são os seguintes:
        # 0. Dias desde que incluido
        # 1. Dias sem comida
        # 2. Dias sem água

        self.cerca = cerca
        self.inv = inventario
        super().__init__()

    def incluir(self):
        tipo = 5
        self.inv.imprime()
        while tipo == 5:
            item = input("Qual item você quer utilizar(1 para sair)\n")
            if item == "1":
                return 0
            elif item == "NULL":
                print("Voce nao possui esse item")
            t,q = self.inv.get_inventario(item,1)
            tipo = self.c_cercado(t)
        
        if tipo != None:
            while self.cerca.get(tipo):
                tipo = tipo + 10
          
            a = [0, 0, 0, 0]
            self.cerca[tipo] = a

    def atualiza(self):
        self.__verifica_vida()

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

    def recolher(self):

        for i in self.cerca.keys():
            if i % 10 == 0:
                self.inv.set_inventario("Leite",randrange(1,6))

            elif i % 10 == 1:
                self.inv.set_inventario("Ovos",randrange(1,6))

            else:
                self.inv.set_inventario("Lã",randrange(1,6))
                self.inv.set_inventario("Leite de Ovelha",randrange(1,4))

    def matar(self,t):
        if t in self.cerca.keys():
            tipo = self.carne(t)
            if t % 10 == 0:
                q = randrange(1,6)
            elif t % 10 == 1:
                q = randrange(1,3)
            else:
                q = randrange(1,5)
            print(f"Voce conseguiu {q} de {t}")
            self.inv.set_inventario(t,q)
            self.cerca.pop(t)
        else:
            print("Esse animal não esta na seu cercado")


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
        print(f"{self.c_animal(i)}   Idade : {self.cerca[i][0]} dias\nFoi alimentado a {self.cerca[i][1]} dias\nRecebeu agua a {self.cerca[i][2]} dias")


class Farmer:
    def __init__(self,nome):
        self.stamina = 10
        self.dinheiro = 10.0
        self.nome = nome

    def get_stamina(self):
        return self.stamina

    def get_dinheiro(self):
        return self.dinheiro

    def set_stamina(self, valor):
        self.stamina += valor
        if self.stamina > 10:
            self.stamina = 10

    def set_dinheiro(self, valor):
        self.dinheiro += valor

    def imprime(self):
        print(f"{self.nome} voce tem")
        print(f"\tEstamina = {self.stamina}")
        print(f"\tDinheiro = R${self.dinheiro}")

class Compras:
    def __init__(self, produtos):
        # O atributo abaixo recebe um dicionário com os produtos da loja

        self.produtos = produtos
        self.__farmer = Farmer({})

    def comprar(self,dinheiro):
        self.imprime_loja()
        nome = input("Que item você quer comprar?\n")
        if self.__verifica_nome(nome):
            quant = int(input(f"Entre com o numero de {nome} você quer: \n"))
            if self.__verifica_dinheiro(dinheiro, self.produtos[nome], quant):
                if quant < 0:
                    quant = quant * -1
                self.__farmer.set_inventario(nome, quant)

    def imprime_loja(self):
        for i in self.produtos.keys():
            print(f"{i}          R${self.produtos[i]}")

    def __verifica_dinheiro(self, dinheiro, preco, quant):
        if dinheiro < preco * quant:
            print("Você não tem dinheiro o bastante para comprar esse item")
            return False
        else:
            return True

    def __verifica_nome(self, nome):
        if nome in self.produtos.keys():
            return True
        else:
            print("Oops! Esse nome não é um nome válido!")
            return False
        

class Loja_p(Imprime):
    def __init__(self,inventario):
        self.inv = inventario
        self.produtos = {}
        self.validos = {"Broto de Batata" : 5.00, "Semente de Tomate" : 5.00, "Semente de Cenoura": 7.00, "Semente de Trigo":10.00, "Muda de Morango" : 10.00, "Batata" : 15.00, "Tomate" : 15.00, "Cenoura" : 18.00, "Trigo" : 20.00, "Morango" : 20.00, "Galinha" : 10.00, "Vaca" : 15.00, "Ovelha" : 20.00, "Leite" : 15.00, "Ovos" : 15.00, "Lã" : 20.00, "Leite de ovelha" : 20.00}

    def adiciona_item(self):
        self.inv.imprime()
        aux = input("Que item você quer adicionar a sua loja?Entre 0 para sair\n")
        if aux == "0":
            return False
        nome, q = self.inv.get_inventario(aux)
        quant = 1
        while quant != 0 and quant <= q:
            quant = int(input("Quantos intens você deseja incluir?Entre 0 para sair\n"))
        
        self.produtos[nome] = quant
        

    def atualiza_loja(self):
        lista = []
        dinheiro = 0
        for i in self.produtos.keys():
            q = randrange(0, self.produtos[i] + 1)
            if q == self.produtos[i]:
                print(f"Voce vendeu todo o estoque de {i}")
                lista.append(i)
            else:
                print(f"Voce vendeu {q} {i}")
                self.produtos[i] -= q
            dinheiro += self.validos[i] * q

        for i in lista:
            self.produtos.pop(i)
        return dinheiro

    def imprime(self):
        for i in self.produtos.keys():
            print(f"{i}          R${self.produtos[i]}")


class Inventario:
  def __init__(self):
        self.inventario = {"Semente de Tomate": 1, "Broto de Batata" : 1, "Vaca" : 1,"Regador" : 1, "Enxada" : 1}
      
  def get_inventario(self,nome,q):
        if self.__verifica_inventario(nome):
          if self.inventario[nome] >= q:
              q = self.inventario[nome]
              self.inventario.pop(nome)
              return nome, q
        else:
            return "NULL",0
  
  def __verifica_inventario(self,n):
        if len(self.inventario) > 9:
            print("O seu inventario esta cheio")
            return False
        elif n not in self.inventario.keys():
            print("Este item nao esta no seu inventario")
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

  def imprime(self):
        for i in self.inventario.keys():
            print(f"{i}     {self.inventario[i]}")


class Passa_dia:
    def init(self,planta,cerca,loja,farmer):
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
            self.farmer.set_dinheiro(self.loja_p.atualiza_loja())
        self.farmer.set_stamina(10)
            
if __name__ == '__main__':
  nome = input("Entre com o seu nome\n")
  farmer = Farmer(nome)
  inventario = Inventario()
  planta = Planta({},inventario)
  cerca = Cercado({},inventario)
  lojap = 0
  loja_sementes = Compras({"Broto de Batata" : 5.00, "Semente de Tomate" : 5.00, "Semente de Cenoura": 7.00, "Semente de Trigo":10.00, "Muda de Morango" : 10.00})
  loja_animais = Compras({"Galinha" : 10.00, "Vaca" : 15.00, "Ovelha" : 20.00})
  loja_ferramentas = Compras({"Regador" : 15, "Enxada" : 20})
  print("Seu avô morreu recentemente deixando para trás uma fazenda")
  print("Você decidi sair da cidade grande onde mora para cuidar dessa fazenda")
  quit = 0
  x = 1
  while quit != 1:
    option = 1
    quit = int(input("Entre 1 para sair.\n"))
    if quit != 1:
      while (option != 4) and x > 0:
        x = farmer.get_stamina()
        option = int(input("O que você quer fazer\n1.Olhar a sua plantação\n2.Olhar o seu cercado\n3.Ir para a cidade\n4.Dormir\n"))
        print(f"option = {option}")

        if option == 1:
          aux = 1
          while (aux != 0) and (x > 0):
            aux = int(input("O que você quer fazer na sua plantação?\n1.Ver Status das Plantas\n2.Plantar\n3.Regar\n4.Colher\nEntre 0 para sair\n"))
            if aux == 1:
              planta.imprime()
            elif aux == 2:
              planta.plantar()
              inventario.imprime()
              planta.imprime()
            elif aux == 3:
              planta.regar()
              planta.imprime()
            elif aux == 4:
              planta.colher()
              planta.imprime()
            farmer.set_stamina(-1)
            x = farmer.get_stamina()
            farmer.imprime()


        elif option == 2:
          aux = 1
          while aux != 0 and x > 0:
            aux = int(input("O que você quer fazer no seu cercado?\n1.Ver Status dos animais\n2.Adicionar animais\n3.Dar água\n4.Dar Comida\n5.Recolher itens\n6.Matar\n Entre 0 para sair\n"))
            if aux == 1:
              cerca.imprime()
            elif aux == 2:
              cerca.incluir()
              cerca.imprime()
              inventario.imprime()
            elif aux == 3:
              cerca.dar_agua()
              cerca.imprime()
            elif aux == 4:
              cerca.dar_comida()
              cerca.imprime()
            elif aux == 5:
              cerca.recolher()
              inventario.imprime()
            elif aux == 6:
              cerca.imprime()
              m = int(input("Qual animal você quer matar?\n"))
              cerca.matar(m)
              cerca.imprime()
            farmer.set_stamina (- 1)
            x = farmer.get_stamina()
            farmer.imprime()
        
        elif option == 3 :
          aux = 1
          while aux != 0 and x > 0:
            aux = int(input("O que você quer fazer na cidade?\n1.Comprar\n2.Vender\nEntre 0 para sair\n"))
            if aux == 1:
              beta = 1
              while beta != 0:
                beta = int(input("O que você quer comprar?\n1.Loja de Sementes\n2. Loja de animais\nEntre 0 para sair\n"))
                alpha = 1
                if beta == 1:
                  while alpha != 0:
                    loja_sementes.comprar(farmer.get_dinheiro)
                    inventario.imprime()
                    alpha = int(input("Deseja continuar comprando?1 para continuar e 0 para sair\n"))
                if beta == 2:
                  while alpha != 0:
                    loja_animais.comprar(farmer.get_dinheiro)
                    inventario.imprime()
                    alpha = int(input("Deseja continuar comprando?1 para continuar e 0 para sair\n"))
              farmer.set_stamina(-1)
              x = farmer.get_stamina()
              farmer.imprime()
            elif aux == 2:
              while aux != 0 and x > 0:
                if lojap == 0:
                  print("Bem vindo a sua loja!")
                  loja_p = Loja_p(inventario)
                else:
                  aux = int(input("O que você deseja fazer?\n1.Adicionar itens\n2.Mostrar itens\nEntre 0 para sair\n"))
                  if aux == 1:
                    loja_p.adiciona_item()
                  else:
                    loja_p.imprime()
                farmer.set_stamina(-1)
                x = farmer.get_stamina()
    print("Chegou o fim de mais um dia")
    chuva = randrange(0,4)
    planta.atualiza(chuva)
    cerca.atualiza()
    if lojap != 0:
      farmer.set_dinheiro(lojap.atualiza_loja())
    farmer.set_stamina(10)





