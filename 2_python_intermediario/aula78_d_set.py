# Set

# Operadores úteis:
# união | união (union) - Une
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)

# intersecção & (intersection) - Itens presentes em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 & s2
print(s3)


# diferença - Itens presentes apenas no set da esquerda
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 - s2
print(s3)


# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 ^ s2
print(s3)