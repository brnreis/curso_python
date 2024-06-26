"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod



class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta):
        super().__init__(nome, idade)
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia: str, numero: str, saldo: float):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo


    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de depósito deve ser positivo')
        self._saldo += valor
        print(f'Seu saldo é: {self._saldo}')

    @abstractmethod
    def sacar(self, valor: float): ...


class ContaCorrente(Conta):
    ...

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo')
        
        self._saldo -= valor

        if self._saldo < -100:
            self._saldo += valor
            return print('Seu saque ultrapassa o limite')

        
        print(f'Você realizou o saque de {valor} e seu saldo é de {self._saldo}')


class ContaPoupanca(Conta):
    ...

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo')
        
        self._saldo -= valor

        if self._saldo < 0:
            self._saldo += valor
            print('Seu saque ultrapassa o limite')
        
        print(f'Você realizou o saque de {valor} e seu saldo é de {self._saldo}')


class Banco:
    def __init__(self):
        self._contas = []
        self._clientes = []
    
    def inserir_conta(self, *conta: Conta):
        self._contas += conta

    def inserir_cliente(self, *cliente: Cliente):
        self._clientes += cliente


    def auth_conta(self):
        return user_agencia in [p._agencia for p in self._contas] and user_conta in [p._numero for p in self._contas]
    
    def auth_cliente(self):
        return user_name in [p._nome for p in self._clientes]
    

    def get(self, user_nome):
        return [vars(inst) for inst in self._clientes if inst._nome == user_nome]




conta1 = ContaCorrente('9088', '00959-3', 0)
cliente1 = Cliente('Bruno Reis', '35', conta1)
bancoitau = Banco()
bancoitau.inserir_cliente(cliente1)
bancoitau.inserir_conta(conta1)


user_name = input('Digite seu nome: ')
user_agencia = input('Digite sua agencia: ')
user_conta = input('Digite sua conta: ')

if bancoitau.auth_conta() and bancoitau.auth_cliente():
    while True:
        achar_conta = bancoitau.get('Bruno Reis')[0]
        # achar_conta['conta'].depositar(50)
        entrada = input('[D]epositar, [S]acar ou [E]xit: ')

        if entrada == 'D':
            valor_deposito = input('Valor: ')
            
            try:
                float(valor_deposito)
            except ValueError:
                print('O valor deve ser um número positivo')
                continue
            
            achar_conta['conta'].depositar(float(valor_deposito))
            continue

        elif entrada == 'S':
            valor_saque = input('Valor: ')

            try:
                float(valor_saque)
            except ValueError:
                print('O valor deve ser um número positivo')
                continue

            achar_conta['conta'].sacar(float(valor_saque))
            continue

        elif entrada == 'E':
            print('ADEUS')
            break

else:
    print('Você não está autorizado!')