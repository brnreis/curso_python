# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Bruno', 31)
print(p1.__dict__) # Chama os dados em forma de dict
print(vars(p1))    # Chama os dados em forma de dict


dados = {'nome': 'Pedro', 'idade': '22'}
p2 = Pessoa(**dados)      # Podemos desempacotar dict para chamar dados
print(p2.__dict__)      
print(vars(p2))