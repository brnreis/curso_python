# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str = field(default='MISSING', repr=False) #Field é uma função usada para configurar os campos na dataclass
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list) #Dessa forma consigo criar uma lista vazia como valor padrão


if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)