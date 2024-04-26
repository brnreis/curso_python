# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for questao in perguntas:
    print('Pergunta:', questao['Pergunta'],'')
    print(f'Opções:')
    options = list(questao.get('Opções'))
    resposta_certa = questao.get('Resposta')

    for i, multipla in enumerate(questao['Opções']):
        print(f'{i}) {multipla}')
 
    try:
        resposta_user = options[int(input(f'Escolha uma opção: '))]
    except ValueError:
        print(f'\nVocê errou! ❌\n\n')
        continue
    except IndexError:
        print(f'\nVocê errou! ❌\n\n')
        continue
 
    if resposta_user == resposta_certa:
        print(f'\nVocê acertou! ✅\n\n')
        acertos += 1
    elif resposta_user != resposta_certa:
        print(f'\nVocê errou! ❌\n\n')

if acertos == len(perguntas):
    print(f'Você acertou {acertos}\nde um total de {len(perguntas)} perguntas!\nPARABÉNS! 🎉')
elif acertos > 0 and acertos < len(perguntas):
    print(f'Você acertou {acertos}\nde um total de {len(perguntas)} perguntas!\nFoi quase 🙃')
else:
    print(f'Você acertou {acertos}\nde um total de {len(perguntas)} perguntas!\nVamos estudar? 😡')