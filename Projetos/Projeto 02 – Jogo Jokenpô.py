from random import randint
import os
from time import sleep

pedra = '''Pedra
    ____
  _/  _ \\
 / _ - _ \\
 \\_______/   
 '''

papel = '''Papel
   _____
  O_____O
  /     /
 /____ /
O_____O
'''
tesoura = '''Tesoura
    _    _
   (_)  / )
     | (_/ 
    _+/  
  // ||
 (/  |/ 
 '''
itens = [pedra, papel, tesoura]
while True:
    vitoriacomp = vitoriajog = empates = 0
    print(f"---"*30)
    rodadas = int(input("""
        ------------------------------------------------
        ------------------ JOKENPÔ----------------------  
        ------------------------------------------------      
        [0] = Pedra    [1] = Papel     [2] = Tesoura
            ____             _____         _    _ 
        _  /  _ \\         O_____O        (_)  / )
        / _ - _ \\       /     /            | (_/ 
        \\_______/      /____ /            _+/    
        '''            O_____O           // ||
                                       (/   |/ 
        DIGITE A QUANTIDADE DE RODADAS:   """))
    os.system("cls")
    for c in range(rodadas):      
        computador = randint(0,2)
        print(f"-"*30)
        print(f''' 
        Rodada {c+1} 
        jogador = {vitoriajog} x {vitoriacomp} = Computador    Empates =  {empates}
        ''')
        print(f"-"*30)
        jogador = int(input("""        
        ------------------------------------------------
        ------------------ JOKENPÔ----------------------  
        ------------------------------------------------      
        [0] = Pedra    [1] = Papel     [2] = Tesoura
            ____             _____         _    _ 
        _  /  _ \\         O_____O        (_)  / )
        / _ - _ \\       /     /            | (_/ 
        \\_______/      /____ /            _+/    
        '''            O_____O           // ||
                                       (/   |/ 
        
        Qual é a sua jogada? =  """))
        print("JO")
        sleep(0.5)
        print("KEN")
        sleep(0.5)
        print("PÔ")
        sleep(0.25)
        print(f"-"*30)       
        print(f"O computador escolheu  {itens[computador]} ", end = "")
        print(f"O Jogador escolheu {itens[jogador]} ")
        print(f"-"*30)
        sleep(0.5)
        print(f"-"*30)
        if computador == 0:
            if jogador == 0:
                print("EMPATE")
                print(f"-"*30)
                empates += 1  
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
            elif jogador == 1:
                print("Vitoria do Jogador")
                print(f"-"*30)
                vitoriajog += 1
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
            elif jogador == 2:
                print("Vitoria do Computador")
                print(f"-"*30)
                vitoriacomp += 1
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
            else:
                print("JOGADA INVALIDA")
                print(f"-"*30)
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
        elif computador == 1:
            if jogador == 0:
                print("Vitoria do Computador")
                print(f"-"*30)
                vitoriacomp += 1
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
            elif jogador == 1:
                print("EMPATE")
                print(f"-"*30)
                empates += 1
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
            elif jogador == 2:
                print("Vitoria do Jogador")
                print(f"-"*30)
                vitoriajog += 1
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
            else:
                print("JOGADA INVALIDA")
                print(f"-"*30)
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
        elif computador == 2:
            if jogador == 0:
                print("Vitoria do Jogador")
                print(f"-"*30)
                vitoriajog += 1
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
            elif jogador == 1:
                print("Vitoria do Computador")
                print(f"-"*30)
                vitoriacomp += 1
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
            elif jogador == 2:
                print("EMPATE")
                print(f"-"*30)
                empates += 1
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")
            else:
                print("JOGADA INVALIDA")
                print(f"-"*30)
                clear = input("limpar a tela?: [S/N]").strip().upper()[0]
                if clear == "S":
                    os.system("cls")                    
        rodadas -=1
        print(f"-"*30)
        print('''
        ------------------------------------------------
        ------------------ JOKENPÔ----------------------  
        ------------------------------------------------   
        ''')
        print(f"-"*30)
        print(f"COMPUTADOR {vitoriacomp} X {vitoriajog} JOGADOR")
    if vitoriacomp > vitoriajog:
        print(f"-"*30)
        print(f"O grande vencedor foi o computador com {vitoriacomp} vitorias")
        print(f"-"*30)
    elif vitoriajog > vitoriacomp:
        print(f"-"*30)
        print(f"O grande vencedor foi o Jogador com {vitoriajog} vitorias")
        print(f"-"*30)
    else:
        print(f"-"*30)
        print(f"Tivemos um Empate")
        print(f"-"*30)        
    r = input("Deseja jogar novamente? [S/N]").strip().upper()[0]
    if r == "N":
        print("""                                                  
  __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
 / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
| (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
 \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  __/ |                                           
 |___/       """)
        break

