"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# entrada = input('Digite um número inteiro: ')
# verif_entrada = None

# try:
#     verif_entrada = int(entrada)
    
#     if verif_entrada % 2 == 0:
#         print('Este número é par')
#     else:
#         print('Este número é ímpar')

# except:
#     print('Isso não é um número inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada = input('Qual é o horário atual? ')
# hora_atual = entrada[0:2]
# dia = '0,1,2,3,4,5,6,7,8,9,10,11'
# tarde = '12,13,14,15,16,17'
# noite = '18,19,20,21,22,23'

# if hora_atual in dia:
#     print('Bom dia!')

# if hora_atual in tarde:
#     print('Boa tarde')

# if hora_atual in noite:
#     print('Boa noite')      

# else:
#     print('Não é um horário válido')


# entrada = input('Qual é o horário atual? ')
# hora_atual = entrada[0:2]

# try:
#     hora_int = int(hora_atual)

#     if hora_int >=0 and hora_int <=11:
#         print('Bom dia!')
#     elif hora_int >=12 and hora_int <=17:
#         print('Boa tarde!')
#     elif hora_int >=18 and hora_int <=23:
#         print('Boa noite!')
#     else:
#         print('Não conheço essa hora')

# except:
#     print('Não é um horário válido')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Digite seu nome: ')
tamanho_nome = len(entrada)

if tamanho_nome <=4:
    print('Seu nome é curto')
elif tamanho_nome >=5 and tamanho_nome <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')


