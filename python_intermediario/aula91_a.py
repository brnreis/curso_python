

# Introdução as generator functions em Python
# generator = (n for n in range(10000000))

def generator(n=0):
    yield 1             # PAUSAR A FUNÇÃO 
    print('Continuando...')
    yield 2             # PAUSAR A FUNÇÃO
    print('Mais uma...')
    yield 3
    print('Vou terminar')
    return 'ACABOU'

gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
