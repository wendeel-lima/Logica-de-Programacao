class Pessoa:
    def __init__(self, nome, idade, peso): # METODO CONTRUTOR
        self.nomePessoa = nome
        self.idadePessoa = idade
        self.pesoPessoa = peso

    def comer(self,calorias):
        if self.idadePessoa >= 30:
            self.pesoPessoa += calorias*2
        else:
            self.pesoPessoa += calorias

    def malhar(self, calorias):
        if self.idadePessoa <= 30:
            self.pesoPessoa -= calorias*2
        else:
            self.pesoPessoa -= calorias

    def mostrarDados(self):
        return f'''
        Nome = {self.nomePessoa}
        Idade = {self.idadePessoa}
        peso = {self.pesoPessoa}         
        '''


pessoa1 = Pessoa('wendeel', 29, 86)
print(pessoa1.mostrarDados()) 
pessoa2 = Pessoa('Thiago', 27, 72.5)

pessoa1.comer(2)
pessoa1.malhar(3)
print(pessoa1.mostrarDados()) 
       
