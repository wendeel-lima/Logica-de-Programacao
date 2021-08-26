class Netflix:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__like = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def like(self):
        return self.__like 


    def dar_like(self):
        self.__like += 1


class Filme(Netflix):
    def __init__(self,nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
     

    def __str__(self):
        return f'''
        Nome: {self.nome}
        Ano: {self.ano}
        Duração: {self.duracao} min
        Likes: {self.like}
         '''

   
class Serie(Netflix):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        

    def __str__(self):
        return f'''
        Nome: {self.nome}
        Ano: {self.ano}
        Temporadas: {self.temporadas}
        Likes: {self.like}
            '''


vingadores = Filme('guerra infitina', 2018, 160)
vingadores.dar_like()
print(vingadores)


