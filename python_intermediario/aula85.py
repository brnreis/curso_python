
# USAR DOIS FOR NA MESMA LIST COMPREHENSION

# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))


lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]


# Vai gerar 3 elementos na lista e cada elemento vai
# ser uma lista com as letras de bruno
lista = [
    [letra for letra in 'bruno']
    for x in range(3)
]

print(lista)