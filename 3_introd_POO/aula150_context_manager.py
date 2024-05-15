# Context Manager com função - Criando e usando um gerenciador de contexto

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('ABRINDO ARQUIVO')
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        yield arquivo
    # except Exception as e:
    #     print('OCORREU ERRO', e)  
    finally:
        print('FECHANDO ARQUIVO')
        arquivo.close()



with my_open('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)