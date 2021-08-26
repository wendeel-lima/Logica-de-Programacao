# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula
# anterior, crie um lançador de dados e moedas em que o usuário deve
# escolher o objeto a ser lançado. Não esqueça que os lançamentos são
# feitos de forma randômica.
from random import randint
class Dado:
    def __init__(self,lados=randint(1,6)):
        self.lados = lados

    def play(self):
        return f"{self.lados}"

jogador1 = Dado(lados=randint(1,6))

print(jogador1.play())


class Moeda:
    def __init__(self,cara, coroa):
        self.ladoa = cara
        self.ladob = coroa

    def jogarmoeda(self,a, b):
        if self.ladoa == a:
            return f"{self.ladoa}"
        else:
            return f"{self.ladob}"

