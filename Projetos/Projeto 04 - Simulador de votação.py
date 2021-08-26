import os

#VARIAVEIS PARA ARMAZENAMENTO DOS VOTOS

candidato_Jose = candidato_Maria = candidato_Joao = votos_nulos = votos_em_branco = 0

#FUNÇÃO PARA VERIFICAR A IDADE DO ELEITOR E AUTORIZAR OU NÃO O VOTO
def autoriza_voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
       return f'VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 70:
       return f'VOTO OPCIONAL'
    else:
       return f'VOTO OBRIGATORIO' 

# Sua função votacao() tem que calcular e mostrar:
def votacao(candidato):  # fução para votação com a variavel candidato como argumento
    global candidato_Maria, candidato_Jose, candidato_Joao, votos_nulos, votos_em_branco

    if candidato == 1 or candidato == 2 or candidato == 3 or candidato == 4 or candidato == 5:
        # ● 1, 2 ou 3 - Votos para os respectivos candidatos
        if candidato == 1:
            candidato_Jose += 1
        elif candidato == 2:
            candidato_Maria += 1
        elif candidato == 3:
            candidato_Joao += 1
            # ● 4- Voto Nulo
        elif candidato == 4:
            votos_nulos += 1
            # ● 5 - Voto em Branco
        elif candidato == 5:
            votos_em_branco += 1
    else:  # se o valor digitado nao e valido, há entrada de novo candidato e a funcao repete
        candidato= str(input('Digite um numero valido para o candidato: '))
        votacao(candidato)


def print_resultados():  # printa resultados e encerra programa
    global candidato_Maria, candidato_Jose, candidato_Joao, votos_nulos, votos_em_branco
    print(f'''
CANDIDATO JOSÉ   - TOTAL DE  {str(candidato_Jose)} votos
CANDIDATO MARIA  - TOTAL DE  {str(candidato_Maria)} votos
CANDIDATO JOÃO   - TOTAL DE  {str(candidato_Joao)} votos
VOTOS NULOS      - TOTAL DE  {str(votos_nulos)} votos
VOTOS EM BRANCO  - TOTAL DE  {str(votos_em_branco)} votos
    ''')
    exit()  # encerra prog


while True:  # laço ocorre indefinidamente ate que ocorra o 'Fim'
    print('''
*********************************************************
                    ELEIÇÕES - 2021
*********************************************************
    CANDIDATOS            NUMERO

CANDIDATO JOSÉ              01
CANDIDATO MARIA             02
CANDIDATO JOÃO              03
VOTOS EM BRANCO             04
VOTOS NULOS                 05

    ''')
    
    #VARIAVEL PARA COLETA DATA DE NASCIMENTO QUE SERA USADA NA FUNÇÃO autoriza_voto()
    voto = int(input("Digite seu ano de Nascimento: "))
    print(autoriza_voto(voto))
    if (autoriza_voto(voto)) == 'VOTO NEGADO':
        voto = int(input("Digite seu ano de Nascimento: "))
        votacao(int(input("Digite o seu candidato: ")))
    else:
        votacao(int(input("Digite o seu candidato: ")))
    #LAÇO ONDE SERA VERIFICADO SE O ELEITOR DESEJA CONTINUAR A VOTAÇÃO
    while True:
        continuar = input('Deseja Votar novamente: [YES/NO] ').strip().upper()[0]
        if continuar in 'YN':
            os.system("cls") 
            break
    # VERIFICAÇÃO QUE ENCERRA A VOTAÇÃO
    if continuar == "N":
        os.system("cls") 
        break

#CABEÇALHO PARA EXIBIR RESULTADOS
print(f'''
    
*********************************************************
                    ELEIÇÕES - 2021
*********************************************************
                    RESULTADO

                    ''')

# VERIFICAÇÃO DE QUAL CANDIDATO GANHOU A ELEIÇÃO
if candidato_Joao > candidato_Jose:
    if candidato_Joao > candidato_Maria:
        print(f"O candidato_Joao Venceu a eleição com {candidato_Joao} votos")

if candidato_Jose > candidato_Joao:
    if candidato_Jose > candidato_Maria:
        print(f"O candidato_Jose Venceu a eleição com {candidato_Jose} votos")

if candidato_Maria > candidato_Jose:
    if candidato_Maria > candidato_Joao:
        print(f"O candidato_Maria Venceu a eleição com {candidato_Maria} votos")

print_resultados() # FUNÇÃO PARA EXIBIR OS RESULTADOS INDIVIDUAIS DE CADA CANDIDATO