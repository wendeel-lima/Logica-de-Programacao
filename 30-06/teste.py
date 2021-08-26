# uma classe é um molde para criação de um ou varios objetos com caracteristicas(atributos) e ações(métodos) em comum.

class Conta: 
    def __init__(self,titular, saldo=0):
        self.titular = titular
        self.saldo = saldo


    def __str__(self):#mostrar em formato de str o seu objeto
       return f'''
        Titular: {self.titular}
        Saldo: {self.saldo}       
       '''
    def depositar(self,deposito):
        self.saldo += deposito
        return f"o seu saldo atua é de {self.saldo}"
    
    def sacar(self,sacar):
        if self.saldo > 0:
            self.saldo -= sacar
            return f"Você sacou: R$ {sacar:.2f}"
        else:
            return "Você não tem saldo suficiente para essa operação"