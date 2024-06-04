
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'teste1.csv'


with open(CAMINHO_CSV, 'r') as arquivo:
    lista_aulas = csv.DictReader(arquivo, delimiter=';')
    nome_colunas = ['titulo_aula',
                    'descricao_aula',
                    'titulo_objeto',
                    'descricao_objeto',
                    'tipo',
                    'conteudo_objeto']

    disciplina_anterior = ''
    linha1 = {}

    for linha in lista_aulas:

        if linha['titulo_aula'] != disciplina_anterior:
            disciplina_anterior = linha['titulo_aula']
            arquivo_novo = Path(__file__).parent / f'{disciplina_anterior}.csv'
            arquivo_novo.touch()

            with open(arquivo_novo, 'w', newline='') as arquivo:
                escritor = csv.DictWriter(
                    arquivo, fieldnames=nome_colunas, delimiter=';')
                escritor.writeheader()

                if bool(linha1) is True:
                    escritor.writerow(linha1)
                escritor.writerow(linha)

                for linha1 in lista_aulas:
                    if linha1['titulo_aula'] == disciplina_anterior:
                        escritor.writerow(linha1)
                    else:
                        break

        else:
            continue
