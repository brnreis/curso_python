"""
enumerate - enumera iteráveis (índices)
"""


lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


# lista_enumerada = enumerate(lista) 

# Gera um iterator que junta a posição com os itens da lista em tuplas.

for indice, nome in enumerate(lista) :
    print(indice, nome)

# Chamando o for dessa forma ele ja separa os dois valores da tupla
