# Problema dos parâmetros mutáveis em funções Python


def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []             # Como lista é um parametro mutável, atribuimos
    lista.append(nome)         # None e colocamos o if para criar uma nova
    return lista               # lista sempre que nao for atribuido nada


cliente1 = adiciona_clientes('bruno')
adiciona_clientes('joana', cliente1)
print(cliente1)


cliente2 = adiciona_clientes('maria')
adiciona_clientes('clara', cliente2)
print(cliente2)