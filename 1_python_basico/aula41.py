frase = 'O Python é uma linguagem de programação' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum'


# Colocando as letras para minusculo
frase_lower = frase.lower()

# Criando o alfabeto
alfabeto = 'abcdefghijklmnopqrstuvxwyz'

# Criando o parâmetro índice e a lista para agrupar a frequência em ordem alfabética
i = 0
contagem_list = []

# Usei while e append para criar a lista
while i < len(alfabeto):
    letra = alfabeto[i]
    #print(letra, frase_lower.count(alfabeto[i]))
    contagem_list.append(frase_lower.count(alfabeto[i]))
    i += 1

# Encontrando o maior numero na lista de frequência
max_cont = max(contagem_list)

# Encontrando o index (posição) do maior número na lista de frequência
index = contagem_list.index(max_cont)

# Criando a lista com o alfabeto para encontrar a letra na mesmo index (posição)
alfabeto_list = list(alfabeto)

# Encontrando a letra final
letra_final = alfabeto_list[index]
print(f'A letra com maior frequência nesta sentença é: {letra_final}')


