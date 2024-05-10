nome = 'Bruno'
altura = 1.81
peso = 65
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.3f}'
print(linha_1)
print(linha_2)
print(linha_3)


print(nome, "tem", altura, "de altura, pesa", peso, "quilos e seu IMC é", imc)