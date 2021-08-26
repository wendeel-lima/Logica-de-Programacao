from random import randint
from time import sleep
# from function import encerrar

class Nave:
    def __init__(self, anoAtual, combustivel, planetaPartida, planetaChegada, galaxia, comunicacao, fimJogo):
        self.anoAtual = anoAtual
        self.combustivel = combustivel
        self.planetaPartida = planetaPartida
        self.planetaChegada = planetaChegada
        self.galaxia = galaxia
        self.comunicacao = comunicacao
        self.fimJogo = fimJogo

    def __str__(self):
        return f"""
                        Ano Atual: {self.anoAtual}
             Combustível restante: {self.combustivel}%
               Planeta de chegada: {self.planetaChegada}
                    Galáxia Atual: {self.galaxia}   
                      Comunicação: {self.comunicacao}   
    """

    def verificaCombustivel(self):
        if self.combustivel <= 0:
            return "                   Você ficou sem combustível."

    def gameOver(self):
        self.fimJogo = 0

    def chamaMenu(self):
        print("Para qual planeta você deseja ir? ")
        if self.galaxia == "Nova" and self.planetaChegada == "":
            print("""
                   1 - Biós (Mais promissor)
                   2 - Agnostos (Planeta similar à Terra)
                   3 - Matér (Pode não ser habitável)        
""")
        elif self.galaxia == "Nova" and self.planetaChegada == "Biós":
            print("""
            Vamos tentar outro planeta? 

                   2 - Agnostos (Planeta similar à Terra)
                   3 - Matér (Pode não ser habitável)
                   0 - Voltar para Terra       
""")
        elif self.galaxia == "Nova" and self.planetaChegada == "Agnostos":
            print("""
                   3 - Matér (Pode não ser habitável)
                   0 - Voltar para Terra           
""")
        elif self.galaxia == "Nova" and self.planetaChegada == "Matér":
            print("""
                   4 - Construir civilização no planeta usando os embriões
                   0 - Voltar para Terra         
""")

    def viajarEntrePlanetas(self, destino):
        if destino == 1:
            self.viajaPlanetaBios()
        elif destino == 2:
            self.viajaPlanetaAgnostos()
        elif destino == 3:
            self.viajaPlanetaMater()
        elif self.planetaChegada == "Biós" and destino == 0:
            while destino == 0:
                print('Coragem!! A humanidade depende de você, por favor não desista.')
                destino = 1
                # destino = int(input("Digite sua opção: "))
        elif self.planetaChegada == "Agnostos" and destino == 0:
            
            while True:
                resposta = str(input("Você quer desistir de voltar para a Terra e iniciar uma nova humanidade neste planeta? [S/N]: ")).upper().strip()[0]
                if resposta == "S":
                    print("Parabéns pela decisão, ela foi de muita astúcia. Mas tente ensinar mais amor e menos ódio para esta nova geração.")
                    self.gameOver()
                    break
                elif resposta == "N":
                    print("Você voltou para a Terra e encontrou sua filha pela última vez.")
                    self.gameOver()
                    break
                else:
                    continue
            # encerrar()
        elif self.planetaChegada == "Matér" and destino == 0:
            hist5 = ['Seu combustível acabou. É o fim da humanidade...','Espera! Surgiram seres da 5ª dimensão e resolveram nos ajudar para termos outra chance. Você aprendeu VIAGEM NO TEMPO!', ' Você conseguiu ver sua filha e salvar a humanidade!']
            for c in hist5:
                print(c)
                sleep(4)
            self.gameOver()

        elif self.planetaChegada == "Matér" and destino == 4:
            hist6 = ['Você iniciou uma nova humanidade!' , 'Ensine novos valores para essa nova humanidade!']
            self.gameOver()

    def efeitoRandom(self):
        resultado = randint(1,5)
        if resultado == 1:
            print("Pane elétrica! Você perdeu 2 anos terrestres enquanto reparava a nave.")
            self.anoAtual += 2
        if resultado == 2:
            print("Traje especial despressurizado! Você perdeu 1 ano terrestre aguardando a pressurização.")
            self.anoAtual += 1

    def mudaGalaxia(self):
        if self.galaxia == "Via Láctea":
            self.galaxia = "Nova"
        elif self.galaxia == "Nova":
            self.galaxia = "Via Láctea"
        self.planetaPartida = ""
        self.planetaChegada = ""
        self.anoAtual += 1

    def viajaPlanetaBios(self):
        self.planetaChegada = "Biós"
        self.combustivel -= 10
        self.anoAtual += 2
        print('''
        PLANETA BIÓS:
        As informações não estão corretas, o planeta não é habitável, 
        sem oxigênio. É todo coberto por gelo.
        -10% de combustível
        Se passaram 2 anos terrestres.
        ''')
        sleep(5)

    def viajaPlanetaAgnostos(self):
        self.planetaChegada = "Agnostos"
        self.combustivel -= 70
        self.anoAtual += 3
        print('''
        PLANETA AGNOSTOS:
        O planeta é todo coberto por água. Não habitável.
        -70% de combustível
        Se passaram 3 anos terrestres.
        ''')
        sleep(5)

    def viajaPlanetaMater(self):
        self.planetaChegada = "Matér"
        self.combustivel -= 20
        self.anoAtual += 14
        self.comunicacao = "Instável"
        print('''
        PLANETA MATÉR:
        Planeta muito parecido com a Terra. Habitável.
        O sistema de comunicação foi comprometido na entrada da atmosfera.
        -20% de combustível
        Se passaram 14 anos terrestres.
        ''')
        sleep(5)


def cabecalho():
    print('''
        _..._		     _  _ _  ___  ___  ___  ___  ___  ___  _    _    ___  ___ 
      .'     '.      _	    | || \ ||_ _|| __>| . \/ __>|_ _|| __>| |  | |  | . || . \ 
     /    .-""-\   _/ l	    | ||   | | | | _> |   /\__ \ | | | _> | |_ | |_ |   ||   /
   .-|   /:.   |  |   |	    |_||_\_| |_| |___>|_\_\<___/ |_| |___>|___||___||_|_||_\_\ 
   |  \  |:.   /.-'-./	                     __________          *    _..----....____
   | .-'-;:__.'    =/	 *       __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
   .'=  *=|BLUE _.='	  _..-''________'   `'   `'   `'     O ``-''._   (,;') _,'
  /   _.  |    ;	,'________________                          \`-._`-','
 ;-.-'|    \   |	 `._              ```````````------...___   '-.._'-:
/   | \    _\  _1	    ```--.._      ,.                     ````--...__\ 
\__/'._;.  ==' ==1	            `.--. `-`  THE FUTURE IS BLUE   ____    |	
         \    \   |	 *   |    +    `. `.       T3C6 - GRUPO 04  ,'`````.  
         /    /   /	   - o -         `._`.        __________   `.       \ 	
         /-._/-._/    *      |	            `-:._____/______/___/____`.     \ 
         \   `\  1	                                                `.   `.___
          `-._/._/ 	                                                  `------'`
--------------------------------------------------------------------------------------''')


def fimgame():
    return '''
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                  ___   ___  __ __  ___    ___  _ _  ___  ___
         .              . /  _> | . ||  \  \| __>  | . || | || __>| . \   
          0     .         | <_/\|   ||     || _>   | | || ' || _> |   /
                 .        `____/|_|_||_|_|_||___>  `___'|__/ |___>|_\_\          .                         .
      .      \   ,
   .          o     .                 .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #  #O##\###                .                        .
   .        #*#  #\##\###                       .                     ,
        .   ##*#  #\##\##               .                     .
      .      ##*#  #o##\#         .                             ,       .
          .     *#  #\#     .                       .       .          ,
                      \          .                 .'.    .
____^/\___^--____/\____O______________/\/\---/\_   |o|  _---______________
   /\^   ^  ^    ^   ^^ ^  '\ ^                   .'o'.      ^       ---
         --           -                           |.-.|      ---  __       ^
   --  __                      ___--  ^  ^                         --  __    


    '''