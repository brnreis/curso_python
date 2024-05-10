
# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html



# Inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys
platform = 'A MINHA'
print(sys.platform)
print(platform)

# Partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
from sys import exit, platform
print(platform)

# Alias 1 - import nome_modulo as apelido
import sys as s
sys = 'alguma coisa'
print(s.platform)
print(sys)


# Alias 2 - from nome_modulo import objeto as apelido
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem
from sys import exit as ex
from sys import platform as pf
print(pf)


# Má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo sem a proteção do nome
print(platform)
exit()