# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']



def teste_de_maiores(func):
    def interna(*args, **kwargs):
        qual_e_maior(*args, **kwargs)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


@teste_de_maiores
def unir_lista(lista1, lista2):
    nova_lista = []
    for i in lista1:
        x = lista1.index(i)
        nova_lista += (lista1[x], lista2[x]),
    return nova_lista
    

def qual_e_maior(lista1, lista2):
    if len(lista1) > len(lista2):
        raise IndexError('A segunda lista é maior do que a primeira, troque a ordem')


nova_lista = unir_lista(cidade, estado)
print(nova_lista)
