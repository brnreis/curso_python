# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

task_list = []
erased = []

while True:
    
    action = input(f'Comandos: listar, desfazer, refazer\nDigite uma tarefa ou comando: ')

    if action == 'listar':
        print('\nA sua lista é:')
        for task in task_list:
            print(task)
        print('')

    elif action == 'desfazer':
        if len(task_list) == 0:
            print('\nNão há o que desfazer\n')
        erased.append(task_list.pop(-1))
        print('')

    elif action == 'refazer':
        if len(task_list) == 0:
            print('\nNão há o que refazer\n')
        task_list.append(erased.pop(-1))
        print('')

    elif action == 'clear':
        os.system('cls')

    else:
        task_list.append(action)
        print('')
    
    continue