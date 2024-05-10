"""
Criando arquivos com Python + Context Manager with
Usamos a função open para abrir
um arquivo em Python (ele pode ou não existir)

Modos:
r (leitura), w (escrita e também apaga tudo que ja tinha), x (para criação)
a (escreve ao final), b (binário)
t (modo texto), + (leitura e escrita)

Context manager - with (abre e fecha)

Métodos úteis:
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)

Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load

"""

caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Atenção\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))
    arquivo.seek(0, 0)
    print(arquivo.read())

print('#' * 10)

with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    print(arquivo.read())