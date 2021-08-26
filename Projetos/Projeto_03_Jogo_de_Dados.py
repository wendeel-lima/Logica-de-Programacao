from random import randint  #IMPORTAR DA BIBLIOTECA RANDOM A FUNÇÃO RANDINT PARA GERAR OS NUMEROS ALEATORIOS PARA AS JOGADAS
import os                   #IMPORTAR OS COMANDOS DO SISTEMA PARA ACRESCENTAR O COMANDO CLS AO JOGO
from time import sleep      #IMPORTAR DA BIBIOTECA TIME A FUNÇÃO SLEEP PARA ACRESCENTAR UM ATRASO NA EXECUÇÃO DOS COMANDOS

# DICIONARIO PARA ARMAZENAR A QUANTIDADE DE VITORIAS
round_game = {
    "Player_01": 0,
    "Player_02": 0,
    "Player_03": 0,
    "Player_04": 0
    }
#COLETAR DO USUARIO A QUANTIDADE DE RODADAS
play = int(input("How many rounds?: "))

for p in range(play):
    #CABEÇALHO + PLACAR
    print(f'''
****************************************************************************
****************************************************************************
-----------------         DICE GAMES / BLUE EDTECH         -----------------
****************************************************************************
****************************************************************************                         
                          .-------.    ______               
                         /   o   /|   /\     \    
                        /_______/o|  /o \  o  \        
                        | o     | | /   o\_____\         
                        |   o   |o/ \o   /o    /      
                        |     o |/   \ o/  o  /      
                        '-------'     \/____o/          
***************************************************************************
    --------------------------   SCOREBOARD   --------------------------   
                    "Player_01" = {round_game["Player_01"]} x {round_game["Player_02"]} = "Player_02"
                    "Player_03" = {round_game["Player_03"]} x {round_game["Player_04"]} = "Player_04"
    --------------------------                -------------------------- 
***************************************************************************
''')
    #DICIONARIO PARA ARMAZENAR AS JOGADAS
    game = {
        "Player_01": randint(1,6),
        "Player_02": randint(1,6),
        "Player_03": randint(1,6),
        "Player_04": randint(1,6)
        }
    for p, j in game.items():
        print(f"The {p} it played [{j}] ")
        sleep(1)
    # VERIFICAR SE O PLAYER_01 GANHOU A RODADA
    if  game["Player_01"] > game["Player_02"]:
        if  game["Player_01"] > game["Player_03"]:
            if  game["Player_01"] > game["Player_04"]:
                round_game["Player_01"] +=1
                print("Player_01 Win a round")
                sleep(1)
    # VERIFICAR SE O PLAYER_02 GANHOU A RODADA
    if  game["Player_02"] > game["Player_01"]:
        if  game["Player_02"] > game["Player_03"]:
            if  game["Player_02"] > game["Player_04"]:
                round_game["Player_02"] +=1
                print("Player_02 Win a round")
                sleep(1)
    # VERIFICAR SE O PLAYER_03 GANHOU A RODADA
    if  game["Player_03"] > game["Player_01"]:
        if  game["Player_03"] > game["Player_02"]:
            if  game["Player_03"] > game["Player_04"]:
                round_game["Player_03"] +=1
                print("Player_03 Win a round") 
                sleep(1)       
    # VERIFICAR SE O PLAYER_04 GANHOU A RODADA
    if  game["Player_04"] > game["Player_01"]:
        if  game["Player_04"] > game["Player_02"]:
            if  game["Player_04"] > game["Player_03"]:
                round_game["Player_04"] +=1
                print("Player_04 Win a round")
                sleep(1)

    # VERIFICA SE HOUVE EMPATES NA RODADA
    if game["Player_01"] == game["Player_02"]:  
        print(f"there was a tie between players: Player_01[{game['Player_01']}] and Player_02 [{game['Player_02']}]")
        sleep(1)
    if game["Player_01"] == game["Player_03"]:
        print(f"there was a tie between players: Player_01[{game['Player_01']}] and Player_03 [{game['Player_03']}]")
        sleep(1)
    if game["Player_01"] == game["Player_04"]:
        print(f"there was a tie between players:Player_01[{game['Player_01']}] and Player_04 [{game['Player_04']}]")
        sleep(1)
    if game["Player_02"] == game["Player_03"]:
        print(f"there was a tie between players:Player_02[{game['Player_02']}] and Player_03 [{game['Player_03']}]")
        sleep(1)
    if game["Player_02"] == game["Player_04"]:
        print(f"there was a tie between players:Player_02[{game['Player_02']}] and Player_04 [{game['Player_04']}]")
        sleep(1)
    if game["Player_03"] == game["Player_04"]:
        print(f"there was a tie between players: Player_03[{game['Player_03']}] and Player_04 [{game['Player_04']}]")
        sleep(2)

        # LIMPAR A TELA APOS TODAS AS RODADAS
        clear = input("limpar a tela?: [S/N]").strip().upper()[0]
        if clear == "S":
            os.system("cls")

# LIMPAR A TELA APOS TODAS AS RODADAS
clear = input("limpar a tela?: [S/N]").strip().upper()[0]
if clear == "S":
    os.system("cls") 

print(f'''
****************************************************************************
****************************************************************************
-----------------         DICE GAMES / BLUE EDTECH         -----------------
****************************************************************************
****************************************************************************                         
                          .-------.    ______               
                         /   o   /|   /\     \    
                        /_______/o|  /o \  o  \        
                        | o     | | /   o\_____\         
                        |   o   |o/ \o   /o    /      
                        |     o |/   \ o/  o  /      
                        '-------'     \/____o/          
***************************************************************************
    --------------------------   SCOREBOARD   --------------------------   
                    "Player_01" = {round_game["Player_01"]} x {round_game["Player_02"]} = "Player_02"
                    "Player_03" = {round_game["Player_03"]} x {round_game["Player_04"]} = "Player_04"
    --------------------------                -------------------------- 
***************************************************************************
''')

# VERIFICAR SE O PLAYER_01 GANHOU O JOGO        
if  round_game["Player_01"] > round_game["Player_02"]:
        if  round_game["Player_01"] > round_game["Player_03"]:
            if  round_game["Player_01"] > round_game["Player_04"]:
                print("Player_01 Winner")
                sleep(1)
# VERIFICAR SE O PLAYER_02 GANHOU O JOGO
if  round_game["Player_02"] > round_game["Player_01"]:
    if  round_game["Player_02"] > round_game["Player_03"]:
        if  round_game["Player_02"] > round_game["Player_04"]:
            print("Player_02 Winner")
            sleep(1)
# VERIFICAR SE O PLAYER_03 GANHOU O JOGO
if  round_game["Player_03"] > round_game["Player_01"]:
    if  round_game["Player_03"] > round_game["Player_02"]:
        if  round_game["Player_03"] > round_game["Player_04"]:
            print("Player_03 Winner") 
            sleep(1)       
# VERIFICAR SE O PLAYER_04 GANHOU
if  round_game["Player_04"] > round_game["Player_01"]:
    if  round_game["Player_04"] > round_game["Player_02"]:
        if  round_game["Player_04"] > round_game["Player_03"]:
            print("Player_04 Winner")
            sleep(1)            
