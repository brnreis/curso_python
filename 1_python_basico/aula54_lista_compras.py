"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""
import os

lista_compras = []

while True:
    
    acao = input(f'Selecione uma opção\n[i]nserir [a]pagar [l]istar: ')

    if acao == 'i':
        inserir = input('O que deseja inserir: ')
        lista_compras.append(inserir)
        os.system('cls')

    elif acao == 'a':
        try:
            apagar = int(input('Qual índice deseja apagar: '))
            del lista_compras[apagar]
            os.system('cls')
        except ValueError:
            print('Digite um número inteiro.')
        except IndexError:
            print('Digite um índice válido.')

    elif acao == 'l':
        os.system('cls')
        for indice, nome in enumerate(lista_compras):
            print(indice, nome)

    else:
        os.system('cls')
        print('Digite uma ação válida.')
    
    continue

