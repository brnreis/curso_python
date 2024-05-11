# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None
    
    def listar_carro(self):
        print(f'{self.nome}, {self.motor.nome}, {self.fabricante.nome}')


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


carro1 = Carro('Fiesta')
carro2 = Carro('Focus')
carro3 = Carro('Fusca')

motor1 = Motor('Motor sinistro')
motor2 = Motor('Motor ruim')

fabricante1 = Fabricante('Ford')
fabricante2 = Fabricante('Fiat')


carro1.motor = motor1
carro1.fabricante = fabricante1
carro1.listar_carro()

carro2.motor = motor2
carro2.fabricante = fabricante1
carro2.listar_carro()

carro3.motor = motor2
carro3.fabricante = fabricante2
carro3.listar_carro()