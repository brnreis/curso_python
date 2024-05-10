
# Escopo da classe e de métodos da classe


class Animal:


    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'    # Essa variavel está dentro do escopo da classe e só pode ser acessada dentro da classe
        print(variavel)
    
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'



leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('carne'))
