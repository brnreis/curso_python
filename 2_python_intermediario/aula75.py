"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam 
o número recebido como parametro

"""


def criar_multiplicador(multiplicador):
    def conta(parametro):
        return multiplicador * parametro
    return conta


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)



print(duplicar(4))
print(triplicar(4))
print(quadruplicar(4))