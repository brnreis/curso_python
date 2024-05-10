# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula127_a_.json'


def dump_json(dict, doc_json):
    with open(doc_json, 'w+', encoding='utf8') as arquivo:
        json.dump(
            dict,
            arquivo,
            ensure_ascii=True,
            indent=2,
        )
    return


class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura


p1 = Pessoa('Bruno', 'Reis', 31, 181)
p2 = Pessoa('Pedro', 'Martins', 22, 160)
p3 = Pessoa('Claudia', 'Silva', 35, 170)

bd = [p1.__dict__, p2.__dict__, p3.__dict__]


dump_json(bd, CAMINHO_ARQUIVO)

