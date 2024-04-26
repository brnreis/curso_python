"""

Calculadora com while

"""

while True:
    
# Declarando as variáveis
    primeiro_num = input('Digite um numero: ')
    operador = input('Digite o operador: ')
    segundo_num = input('Digite outro numero: ')

# Convertendo as entradas de str para float
# Interrompendo o programa caso números errados sejam inseridos com try e except ao fim
    try:
        primeiro_num = float(primeiro_num)
        segundo_num = float(segundo_num)
        
# Declarando as operações para cada operador (+ - / *) ou informando invalidade  
        if operador == '+':
            print(f'{(primeiro_num + segundo_num):.2f}')
        elif operador == '-':
            print(f'{(primeiro_num - segundo_num):.2f}')
        elif operador == '*':
            print(f'{(primeiro_num * segundo_num):.2f}')
        elif operador == '/':
            print(f'{(primeiro_num / segundo_num):.2f}')
        else:
            print('Operador inválido')
    except:
        print('Você digitou um número inválido!')

# Inserindo a opção de sair    
    sair = input('Quer sair? [s]').lower().startswith('s')
    if sair == True:
        break

# Resposta de saída
print('Adeus!')