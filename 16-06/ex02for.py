#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

# pesomaior = 0
# pesomenor = 0

# for n in range(0,5):
#     peso = float(input("Digite o seu peso: "))
#     if n == 1:
#         pesomaior = peso
#         pesomenor = peso
#     else:
#         if peso > pesomaior:
#             pesomaior = peso
#         if peso < pesomenor:
#             pesomenor = peso
# print(f"O maior peso foi {pesomaior}kg e o menor peso foi {pesomenor}kg")

#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
# tabuada desse número.

# numero = int(input("Escolha o numero da tabuada: "))

# for n in range(1,11):
#     print(f"{n} x {numero} = {n * numero}")

#03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores.

# menor = 0
# maior = 0

# for n in range(1,7+1,1):
#     anonascimento = int(input("Qual o seu ano de nascimento: "))
#     anoatual = 2021
#     if anoatual - anonascimento < 18:
#         menor += 1
#     else:
#         maior += 1
# print(f"{menor} pessoas ainda não atingiram a maioridade e {maior} pessoas ja são maiores")

#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados.

# soma = 0
# n1 = 0
# for n in range(1,7):
#     par = int(input("digite um numero: "))
#     if par % 2 == 0:
#         n1 += 1
#         soma += par
# print(f"foram digitados {n1} numeros pares e a soma deles é igual a {soma}")



#01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break)

# total = 0
# resp = ""

# while resp != 5:
#     valor1 = int(input("Digite um valor: "))
#     valor2 = int(input("Digite um valor: "))
#     print('''
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa   
#     ''')
#     resp = int(input("Escolha uma a operação: "))
#     if resp == 1:
#        print(f"A soma de {valor1} + {valor2} = {valor1 + valor2}")
#     if resp == 2:
#         print(f"A Multiplicação de {valor1} * {valor2} = {valor1 * valor2}")
#     if resp == 3:
#         if valor1 > valor2:
#             print(f"o Maior valor é {valor1}")
#         else:
#             print(f"o Maior valor é {valor2}")
#     if resp == 5:
#         print("Você saiu do Programa!!!")

#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

resp = maior18 = homens = mulher20 = 0

while resp != "N":
    idade = int(input("Qual é a sua Idade: "))
    sexo = str(input("Qual é a sua Sexo: [M/F] ")) .strip().upper()
    resp = input("Deseja continuar? [S/N]")
    if resp not in 'SN':
        resp = input("Deseja continuar? [S/N]")
    else:
        break