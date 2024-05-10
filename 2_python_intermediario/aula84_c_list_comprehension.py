
# FILTRO de dados em list comprehension

import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10  #ESSE É O IF DO FILTRO
]

# PARA USAR FILTRO EU COLOCO O IF DEPOIS DO FOR
# ELE VAI FILTRAR OS VALORES DA LISTA E RETORNAR SOMENTE O QUE EU QUERO
# A DIFERENÇA É QUE ANTES DO FOR EU MAPEIO (ALTERO)

p(novos_produtos)

# lista = [n for n in range(10) if n < 5]
# print(lista)





