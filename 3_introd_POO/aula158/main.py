import clientes
import contas


class Banco:
    def __init__(self):
        self._contas = []
        self._clientes = []
    
    def inserir_conta(self, *conta: contas.Conta):
        self._contas += conta

    def inserir_cliente(self, *cliente: clientes.Cliente):
        self._clientes += cliente


    def auth_conta(self):
        return user_agencia in [p._agencia for p in self._contas] and user_conta in [p._numero for p in self._contas]
    
    def auth_cliente(self):
        return user_name in [p._nome for p in self._clientes]
    

    def get(self, user_nome):
        return [vars(inst) for inst in self._clientes if inst._nome == user_nome]
    

conta1 = contas.ContaCorrente('9088', '00959-3', 0)
cliente1 = clientes.Cliente('Bruno Reis', '35', conta1)
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