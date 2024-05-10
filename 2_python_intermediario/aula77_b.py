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

# Contador de acertos
acertou = 0

# Aqui eu gerei cada uma das perguntas
for questao in perguntas:
    print('Pergunta:', questao['Pergunta'],'')
    print(f'Opções:')

 # Ainda dentro do primeiro for eu criei a lista de opções (para comparar com a resposta certa)    
    options = list(questao.get('Opções'))

 # Peguei a resposta certa dentro do dicionario    
    resposta_certa = questao.get('Resposta')

 # Abri outro for para exibir as opções
    for i, multipla in enumerate(questao['Opções']):
        print(f'{i}) {multipla}')

 # Usei o try para pegar o erro de inserir caracteres aleatórios como opção
    try:
        resposta_user = options[int(input(f'Escolha uma opção: '))]
    except ValueError:
        print(f'\nVocê errou! ❌\n\n')
        continue
    except IndexError:
        print(f'\nVocê errou! ❌\n\n')
        continue
 
 # Criando o padrão de retorno
    if resposta_user == resposta_certa:
        print(f'\nVocê acertou! ✅\n\n')
        acertou += 1
    elif resposta_user != resposta_certa:
        print(f'\nVocê errou! ❌\n\n')

if acertou == len(perguntas):
    print(f'Você acertou {acertou}\nde um total de {len(perguntas)} perguntas!\nPARABÉNS! 🎉')
elif acertou > 0 and acertou < len(perguntas):
    print(f'Você acertou {acertou}\nde um total de {len(perguntas)} perguntas!\nFoi quase 🙃')
else:
    print(f'Você acertou {acertou}\nde um total de {len(perguntas)} perguntas!\nVamos estudar? 😡')