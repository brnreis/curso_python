
# Dictionary Comprehension e Set Comprehension

# DICT COMPREHENSION
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor #MAPEAMENTO(só vira upper se for str)
    for chave, valor
    in produto.items()
    if chave != 'categoria' #FILTRO(só vou incluir onde a chave for diferente de categoria)
}

# PODE FAZER A PARTIR DE LISTAS DE TUPLAS TAMBEM
lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

print(dc)

# SET COMPREHENSION
s1 = {2 ** i for i in range(10)}
print(s1)