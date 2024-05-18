from abc import ABC, abstractmethod

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

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo')
        
        self._saldo -= valor

        if self._saldo < -100:
            self._saldo += valor
            return print('Seu saque ultrapassa o limite')

        
        print(f'Você realizou o saque de {valor} e seu saldo é de {self._saldo}')
    
        

class ContaPoupanca(Conta):
    
    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo')
        
        self._saldo -= valor

        if self._saldo < 0:
            self._saldo += valor
            print('Seu saque ultrapassa o limite')
        
        print(f'Você realizou o saque de {valor} e seu saldo é de {self._saldo}')