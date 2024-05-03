"""
LAMBDA
"""

# Foi criada para chamar a função lambda
def executa(funcao, *args):
    return funcao(*args)


# Abaixo tem essa mesma função na forma de lambda, mas ja com os parâmetros definidos
def soma(x, y):          
    return x + y


# Essa forma é a mesma coisa que usar as formas de baixo
print(executa(lambda x, y: x + y, 2, 3)) 
print(executa(soma, 2, 3))
print(soma(2,3))


# Abaixo tem essa mesma função na forma de lambda, mas ja com os parâmetros definidos
def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# Chamando a função de cima
duplica = cria_multiplicador(2)
print(duplica(3))

# Fazendo a mesma coisa só que com lambda (má prática: muito dificil de ler)
duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(3))


# A função lambda é mais utilizada para coisas simples tipo essa de baixo
# Não é indicado quando dificulta muito a leitura do código
print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7))