frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum'

frase = frase.lower()

i = 0
maior_letra = ''
maior_qtd = 0
qtd_atual = 0

while i < len(frase):

  if frase[i] == ' ':
    i += 1
    continue

  letra_atual = frase[i]
  # print(letra_atual, frase.count(letra_atual))
  qtd_atual = frase.count(letra_atual)

  if qtd_atual > maior_qtd:
    maior_qtd = qtd_atual
    maior_letra = letra_atual


  i += 1

print(f'A letra que aparece mais vezes é: "{maior_letra}". Ela aparece {maior_qtd}x.')
# print(maior_letra)
# print(maior_qtd)