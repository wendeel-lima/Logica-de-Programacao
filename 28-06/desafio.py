#Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."


class Contas:
    def __init__(self, titular, saldo):
        self.titularContas = titular
        self.saldoContas = saldo

    def saida(self, sacar):
        if self.saldoContas > 0:
            self.saldoContas -= sacar
            return f"Você sacou: R$ {sacar:.2f}"
        else:
            return "Você não tem saldo suficiente para essa operação"
    
    def entrada(self, depositar):
        self.saldoContas += depositar
        return f'Você depositou: R$ {depositar:.2f}'

    def extrato(self):
        return f'''
        
        titular = {self.titularContas}
        saldo = R$ {self.saldoContas:.2f}
        
        '''

titular1 = Contas("wendeel", 350)

print(titular1.extrato())

print(titular1.entrada(100))

print(titular1.extrato())

print(titular1.saida(450))

print(titular1.extrato())

print(titular1.saida(1))