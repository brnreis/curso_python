# Empacotamento e desempacotamento de dicionários



# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# _______________________________________________________


# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }

# dados_pessoa = {
#     'idade': 16,
#     'altura': 1.6,
# }

# pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

#________________________________________________________


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)