# Exercícios Tuplas:
# 01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições.
# Dica: utilizar a biblioteca random do Python.

# from random import randint  
# tupla = ((randint(1,50)), (randint(1,50)), (randint(1,50)), (randint(1,50)),(randint(1,50)))
# print(tupla)
# print(f"O valor Maximo foi: {max(tupla)}")
# print(f"O valor Minimo foi: {min(tupla)}")

# 02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.

# n1 = int(input("Escreva um Numero: "))
# n2 = int(input("Escreva um Numero: "))
# n3 = int(input("Escreva um Numero: "))
# n4 = int(input("Escreva um Numero: "))

# tupla = (int(input("Escreva um Numero: ")), int(input("Escreva um Numero: ")), int(input("Escreva um Numero: ")), int(input("Escreva um Numero: ")))
# print(f" O numero 9 aparece {tupla.count(9)} vezes")
# print(f" O numero 3 aparece na posição {tupla.index(3)}")
