"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input('Digite o seu CPF (somente números): ')
# cpf = '74682489070'
cpf_novedigitos = cpf[:9]
cpf_multiplicacao = 0
i_regressivo1 = 10


# Usei a variável cpf_multiplicacao para somar cada numero do cpf multiplicado pela regressiva de 10 a 2
for numero in cpf_novedigitos:
    cpf_multiplicacao += (int(numero) * i_regressivo1)
    i_regressivo1 -= 1

# Calculei o resto e o primeiro digito
resto = (cpf_multiplicacao * 10) % 11
primeiro_digito = resto if resto <= 9 else 0

print(primeiro_digito)