# Aula 09 - CodeLab - Estruturas de Repetição e Listas

#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

# lista = []
# par = []
# impar = []
# test = ""
# while True:
#     test = (int(input("digite um numero:")))
#     if test not in lista:
#         lista.append(test)
#         resp = input("deseja continuar? [S/N]") .strip().upper()[0]
#         if resp == "N":
#             break
#     else:
#         resp = input("deseja continuar? [S/N]") .strip().upper()[0]   
#         if resp == "N":
#             break
# lista.sort()
# print(lista)


# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# # disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# # ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# # geradas.

# lista = []
# par = []
# impar = []
# test = ""
# while True:
#     test = (int(input("digite um numero:")))
#     if test not in lista:
#         lista.append(test)
#         if test % 2 == 0:
#             par.append(test)
#         else:
#             impar.append(test)
#         resp = input("deseja continuar? [S/N]") .strip().upper()[0]
#         if resp == "N":
#             break
#     else:
#         resp = input("deseja continuar? [S/N]") .strip().upper()[0]   
#         if resp == "N":
#             break
# lista.sort()
# print(lista)
# print(par)
# print(impar)

# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
n1 = list()
jogos = list()
apostador = int(input("Quantos jogos deseja fazer? "))
for n in range(apostador):  
    cont = 0  
    while True:
        num = randint(1,60)
        if num not in n1:
            n1.append(num)            
            cont += 1
        if cont >= 6: 
            break 
    n1.sort()
    jogos.append(n1[:])
    n1.clear()       
# print(f"Os numeros sorteados são: {jogos[:]}")

print(f"======={apostador} jogos sorteados =======")
for i, c in enumerate(jogos):
    print(f"O {i+1}° jogo foi: {c}")
    sleep(1)



