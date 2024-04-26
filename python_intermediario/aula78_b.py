""" 

Sets são eficientes para remover valores duplicados
de iteráveis.

"""

l1 = [1, 2, 3, 3, 3, 3, 3, 3, 3, 1]
# s1 = {1, 2, 3, 3, 3, 3, 3, 3, 3, 1}
s1 = set(l1)
l2 = list(s1)
print(s1)
print(l2)

# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1 = {1, 2, 3}

print(3 in s1)

for numero in s1:
    print(numero)

