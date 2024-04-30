import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
print(next(iterator))


lista = [n for n in range(1000000)] #Essa lista é toda salva na memória
generator = (n for n in range(1000000)) #Essa lista nao é salva na memória, ela fica esperando eu pedir um valor

# O generator sabe qual é o próximo valor, mas não tem índice

print(sys.getsizeof(lista)) #Para ver o tamanho em bytes 
print(sys.getsizeof(generator))

print(next(generator))
print(generator)

# for n in generator
#     print(n)