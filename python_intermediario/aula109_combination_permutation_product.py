# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
# permutations, product
from itertools import combinations, permutations, product
import pprint as pp



pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

pp.pprint(list(combinations(pessoas, 2)))
print()
pp.pprint(list(permutations(pessoas, 2)))
print()
pp.pprint(list(product(*camisetas)))