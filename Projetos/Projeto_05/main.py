# -------------------------------- Libs -------------------------------------
from ast import increment_lineno
from time import sleep #Biblioteca para efeitos de transição
from tqdm import tqdm # Biblioteca para barra de progresso
from os import system
import pygame # Biblioteca para uso de efeitos sonoros
import os
from classe1 import Nave
from classe1 import cabecalho
from classe1 import fimgame

fimDeJogo = 0

# ------------------------------- Programa Principal -------------------------
if(__name__ == "__main__"):
    system("cls")
    cabecalho()

    for p in tqdm(range(100)):
        sleep(0.001)
    sleep(4)
    system("cls")
    cabecalho()
    hist1 =['Durante um período de escassez de alimentos\n', 'cientistas descobrem que a Terra tem uma data concreta para acabar em...\n', '20 anos!!!']
    for c in hist1:
        print(f'{c: ^90}')
        sleep(4)

    system("cls")
    cabecalho()
    hist2 = ['Um piloto decide deixar sua filha de apenas 10 anos\n', 'para se arriscar em uma viagem através do universo\n','juntamente com 3 cientistas para identificar um planeta similar à Terra.']
    for c in hist2:
        print(f'{c: ^90}')    
        sleep(4)

    system("cls")
    cabecalho()
    hist3 = ['Sua viagem só é possível através de um BURACO DE MINHOCA !\n','O percurso durará 1 ano e nessa nova galáxia você encontrará 3 planetas promissores.\n','Na nave teremos 4 tripulantes. Você e 3 cientistas.\n']
    for c in hist3:
        print(f'{c: ^90}')
        sleep(4)

    system("cls")
    cabecalho()
    hist4 = ['Você terá que decidir entre seguir o\n', 'Plano A: Encotrar um planeta colonizável e buscar os sobreviventes\n', 'na Terra.\n', 'Ou Plano B: Caso algo dê errado e seu retorno não seja possível\n', 'Sua nave está transportando embriões humanos para a criação de\n','uma nova sociedade.\n']
    for c in hist4:
        print(f'{c: ^90}')
        sleep(4)

    print("Você agora é este piloto e deve escolher as ações corretas para SALVAR A HUMANIDADE !\n")
    sleep(2)
    piloto = str(input("                     Digite seu nome para continuar: \n  ")).title()

    system("cls")
    cabecalho()

    nave = Nave(2021, 100, "Terra", "", "Via Láctea", "Estável", 1 )
    
    lancarNave = str(input(f"                 Vamos lançar nossa nave, {piloto}? [S/N]: ")).upper()[0]
    while lancarNave not in 'SN':
        lancarNave = str(input(f"                 Vamos lançar nossa nave, {piloto}? [S/N]: ")).upper()[0]

    if lancarNave == "S":
        print(f"{'Lançamento em: ': ^90}")
        for c in range(5 , 0, -1):
            print(f'{c: ^90}')
            sleep(1)
        system("cls")
        print('''

 .      -*- +          ________________________________         
         .   . *      /                 -*- +    |      "-_ . *   .    +    '`  .   . *   .    +            
  -*-                /      : \ | / :          - o -      \         
                    /        '-___-'             |          \      `  .   . *   .    +   
         |         /_________________________________________ \      
       - o -            _______| |________________________--""-L                  .     -*-
         |            /        F J       . *   .    +           \ 
                     /        F   J                              L `  .   . *   .    +    ' 
                    /       :'     ':    '`  .   . *   .    +   F
                   /_________________________________________--"       

.      -*-              +  `  .   . *   .    +    '`  .   . *   .    +    

 .      -*-              +           .'.                       MMM8&&&.
*   .         '       .   *          |o|                 _...MMMMM88&&&&..._                  .     -*-
 +         .    +       .           .'o'.          .::''     MMMMM88&&&&&&' '::.   .   `  .   . *   .    +    ' 
                   .     -*-        |.-.|          ::        MMMMM88&&&&&&      ::    
   `  .   . *   .    +    '         '   '             '::....MMMMM88&&&&&&....::'  '  
                         _____                            `''''MMMMM88&&&&''''`
                      ,-:` \;',`'-,                            'MMM8&&&'
  `  .   . *       .'-;_,;  ':-;_,'.        
                   /;   '/    ,  _`.-\        `  .   . *   .    +    
                  | '`. (`     /` ` \`|                  .     -*- 
                  |:.  `\`-.   \_   / |
                  |     (   `,  .`\ ;'|            '       .   * 
                   \     | .'     `-'/
                    `.   ;/        .'
                       `'-._____. '' 
''')

        sleep(3)
        
        print(f"{'Se dirigindo ao buraco de minhoca!': ^90}")
        sleep(5)
        system("cls")
        print("Você atravessou o buraco de minhoca!")
        print('''
            *   '*
                      *
                           *
                                   *
                           *
                                *

                     .                      .
                    .                       ;
                     :                  - --+- -
                     !           .          !
                     |        .             .
                     |_         +
                  ,  | `.
        --  --- --+-<#>-+- ---  --  -
                  `._|_,'
                     T
                     |
                     !
                     :         . : 
                     .       *       
        
''')
        sleep(2)
        system("cls")
    #     print(f"\nO ano atual é 2021 e sua nave está transportando embriões \
    # humanos para caso a volta não seja possível.")
    #     sleep(3)
        cabecalho()
        print(nave)
        sleep(2)

        
        nave.mudaGalaxia()
        print(nave)
        sleep(2)

    # nave.chamaMenu()
    # escolhaPlaneta = int(input("Digite sua opção: "))

        while fimDeJogo != nave.fimJogo:
            system("cls")
            cabecalho()
            nave.chamaMenu()
            escolhaPlaneta = int(input('Digite a opção: '))
            nave.efeitoRandom()
            nave.viajarEntrePlanetas(escolhaPlaneta)
            print(nave)
            sleep(3)
    
    else:
        print("Você agiu conforme seu coração mandou e desistiu de sua missão.Lançamento cancelado! E você viverá o resto de seus dias ao lado de sua família até que chegue o FIM DA HUMANIDADE !")
    print(fimgame())

    pygame.init()
    if os.path.exists('David_Bowie_-_Starman-192k.mp3'):
      pygame.mixer.music.load('David_Bowie_-_Starman-192k.mp3')
      pygame.mixer.music.play()
      pygame.mixer.music.set_volume(1)

      clock = pygame.time.Clock()
      clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
    else:
          print('O arquivo musica.mp3 não está no diretório do script Python')