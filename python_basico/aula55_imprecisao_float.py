"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal # Opção 1: importar essa biblioteca e utilizar as funções abaixo, lembrando de botar os valores como str

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_3)

print(f'{numero_3:.2f}') # opção 2: formatar em f' (o resultado é uma str)

print(round(numero_3, 2)) #opção 3: usar a função round (o resultado é em float)