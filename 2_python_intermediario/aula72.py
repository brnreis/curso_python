# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total 

result = multiplicacao(1, 2, 3, 4, 5, 926)
print(result)



def imp_par(x):
    if x % 2 == 0:
        return f'O número {x} é par!'
    return f'O número {x} é ímpar!'


resultado = imp_par(15)
print(resultado)