
# Try, except, else e finally


try:
    print('abrir arquivo')
    8/0
except ZeroDivisionError:
    print('dividiu por zero')
finally:
    print('fechar arquivo')    
    

# O bloco de código do finally vai executar de qualquer forma

# Posso botar um else depois do except para uma excessão



