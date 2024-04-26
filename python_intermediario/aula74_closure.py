"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao): # o que está na definição na função é lembrado
    def saudar(nome): # O que está dentro é dinâmico
        return f'{saudacao}, {nome}'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Bruno'))
print(falar_boa_noite('Bruno'))


# Crio uma função dentro de outra função
