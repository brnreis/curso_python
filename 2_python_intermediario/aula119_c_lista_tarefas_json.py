import os
import json

erased = []

try:
    with open('aula119.json', 'r', encoding='utf8') as arquivo:
        task_list = list(json.load(arquivo))

except FileNotFoundError:
    lista = []
    with open('aula119.json', 'w+', encoding='utf8') as arquivo:
        json.dump(lista,
            arquivo,
            ensure_ascii=True,
            indent=2,
        )

    task_list = list(json.load(arquivo))


def dump_json(lista, doc_json):
    with open(doc_json, 'w+', encoding='utf8') as arquivo:
        json.dump(lista,
            arquivo,
            ensure_ascii=True,
            indent=2,
        )
    return


def bring_print_json(doc_json):
    with open(doc_json, 'r', encoding='utf8') as arquivo:
        bring = json.load(arquivo)
        
        for task in bring:
            print(task)
        print('')


while True:
    
    action = input(f'Comandos: listar, desfazer, refazer\nDigite uma tarefa ou comando: ')

    if action == 'listar':
        print('\nA sua lista é:')
        bring_print_json('aula119.json')

    elif action == 'desfazer':
        if len(task_list) == 0:
            print('\nNão há o que desfazer\n')
            continue

        erased.append(task_list.pop(-1))
        dump_json(task_list, 'aula119.json')
        print('')

    elif action == 'refazer':
        if len(erased) == 0:
            print('\nNão há o que refazer\n')
            continue

        task_list.append(erased.pop(-1))
        dump_json(task_list, 'aula119.json')
        print('')

    elif action == 'clear':
        os.system('cls')

    else:
        task_list.append(action)
        dump_json(task_list, 'aula119.json')
        print('')
    
    continue