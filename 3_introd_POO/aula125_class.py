# Atributos de classe

class Pessoa:
    ano_atual = 2024    # Esse é um atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('Bruno', 31)
p2 = Pessoa('Helena', 23)

print(Pessoa.ano_atual)


print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())