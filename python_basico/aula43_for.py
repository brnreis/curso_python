"""
For 

"""


texto = 'Python'
novo_texto = ''

# A variável letra é criada aqui mesmo, ela não vem de lugar nenhum
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

