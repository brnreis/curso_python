"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = input('Digite o seu CPF (somente números): ')

# cpf.isdigit() and len(cpf) == 11


cpf_novedigitos = cpf[:9]
cpf_multiplic_1 = 0
i_regressivo1 = 10



# Usei a variável cpf_multiplicacao para somar cada numero do cpf multiplicado pela regressiva de 10 a 2
for numero in cpf_novedigitos:
    cpf_multiplic_1 += (int(numero) * i_regressivo1)
    i_regressivo1 -= 1

# Calculei o resto e o primeiro digito
resto = (cpf_multiplic_1 * 10) % 11
primeiro_digito = resto if resto <= 9 else 0

# print(primeiro_digito)


# _________________________________________________


cpf_dezdigitos = cpf[:10]
cpf_multiplic_2 = 0
i_regressivo2 = 11


for numero in cpf_dezdigitos:
    cpf_multiplic_2 += (int(numero) * i_regressivo2)
    i_regressivo2 -= 1

resto = (cpf_multiplic_2 * 10) % 11
segundo_digito = resto if resto <= 9 else 0

# print(segundo_digito)

if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
    print('CPF válido!')

else:
    print('CPF inválido!')
