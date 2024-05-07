

import os
import json




task_list = []
erased = []

def save_json(palavra, doc_json):
    with open(doc_json, 'a+', encoding='utf8') as arquivo:
        arquivo.write(f'{palavra}\n')
    return


def bring_json(doc_json):
    with open(doc_json, 'r', encoding='utf8') as arquivo:
        bring = json.load(arquivo)
        
        for task in bring:
            print(task)
        print('')



while True:
    
    action = input(f'Comandos: listar, desfazer, refazer\nDigite uma tarefa ou comando: ')

    if action == 'listar':
        print('\nA sua lista é:')
        bring_json('aula_120.json')

    elif action == 'desfazer':
        if len(task_list) == 0:
            print('\nNão há o que desfazer\n')
        erased.append(task_list.pop(-1))
        
        # save_json(task_list, 'aula_120.json')
        
        print('')

    elif action == 'refazer':
        if len(task_list) == 0:
            print('\nNão há o que refazer\n')
        task_list.append(erased.pop(-1))
        
        # save_json(task_list, 'aula_120.json')
        
        print('')

    elif action == 'clear':
        os.system('cls')

    else:
        # task_list.append(action)
        save_json(action, 'aula_120.json')
        print('')
    
    continue