import importlib

import aula98_b


print(aula98_b.variavel)

for i in range(10):
    importlib.reload(aula98_b)
    print(i)

print('Fim')