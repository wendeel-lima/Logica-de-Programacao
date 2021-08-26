# #01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:

# # matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # [  1  ][  2  ][  3  ]
# # [  4  ][  5  ][  6  ]
# # [  7  ][  8  ][  9  ] 

# matriz = [[],[],[]]
# for linha in range(0,3):
#         for coluna in range(0,3):
#                 matriz[linha].append(int(input(f"Digite um valor para [{linha},{coluna}]: ")))
# for linha in range(0,3):
#         for coluna in range(0,3):
#                 print(f'[{matriz[linha][coluna]:^5}]', end='')
#         print()


#02 - Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha.

# par = 0
# matriz = [[],[],[]]
# for linha in range(0,3):
#         for coluna in range(0,3):
#                 num = int(input(f"Digite um valor para [{linha},{coluna}]: "))
#                 if num % 2 == 0:
#                         par += num
#                 matriz[linha].append(num)
# print(matriz)
# for linha in range(0,3):
#         for coluna in range(0,3):
#                 print(f'[{matriz[linha][coluna]:^5}]', end='')
#         print()
# print(f"A soma dos numeros pares é {par}.")
# print(f"A soma dos valores da terceira coluna é {(matriz[0][2] + matriz[1][2] + matriz[2][2])}")
# print(f"O Maior valor da segunda linha é {max(matriz[1])} ")


#03 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:
   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso


lista1 = list()
menor = maior = pessoas = 0
while True:
     lista_temp = list()
     nome = str(input("Digite o nome: "))
     peso = int(input("Digite o peso: "))
     pessoas += 1      
     lista_temp.append(nome)
     lista_temp.append(peso)
     lista1.append(lista_temp)
     r = input("Deseja continuar? [S/N] ").strip().upper()[0]
     if r == "N":
        break
print(lista1)
# print(f"A quantidades de pessoas cadastradas foi {pessoas}")
# for l in range(lista1):
#         for c in range(lista1):
#                 print(l[1])


