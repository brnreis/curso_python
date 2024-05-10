# @property - um getter no modo Pythônico
# getter - um método para obter um atributo:
# cor -> get_cor()

# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente (é o código que usa seu código)
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    
    @property
    def cor(self):
        return self.cor_tinta
  

caneta = Caneta('Azul')
print(caneta.cor)


#######################################

# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor

#     def get_cor(self):        # Esse getter protege o codigo cliente pois se eu mudar o nome 'cor' no codigo oprinal, não travo os outros.
#         return self.cor


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())