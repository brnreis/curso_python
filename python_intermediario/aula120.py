import os
import json


with open('aula_120.json', 'r', encoding='utf8') as arquivo:
    task_list = list(json.load(arquivo))

erased = []


def save_json(lista, doc_json):
    with open(doc_json, 'w+', encoding='utf8') as arquivo:
        json.dump(lista,
            arquivo,
            ensure_ascii=True,
            indent=2,
        )
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
            continue

        erased.append(task_list.pop(-1))
        save_json(task_list, 'aula_120.json')
        print('')

    elif action == 'refazer':
        if len(erased) == 0:
            print('\nNão há o que refazer\n')
            continue

        task_list.append(erased.pop(-1))
        save_json(task_list, 'aula_120.json')
        print('')

    elif action == 'clear':
        os.system('cls')

    else:
        task_list.append(action)
        save_json(task_list, 'aula_120.json')
        print('')
    
    continue