from pathlib import Path


caminho_projeto = Path()
print(caminho_projeto.absolute())


caminho_arquivo = Path(__file__)
print(caminho_arquivo)


print(caminho_arquivo.parent)


ideias = caminho_arquivo.parent / 'ideias'
print(ideias)


arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
arquivo.touch() # Criar arquivo
print(arquivo)
arquivo.unlink() # Deletar arquivo

