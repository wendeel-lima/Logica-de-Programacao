# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
#l = [5, 7, 2, 9, 4, 1, 3]

# # a) tamanho da lista.
# print(f"O tamano da lista é de {len(l)} posições")
# # b) maior valor da lista.
# print(f"O Maior valor da lista é: {max(l)} ")
# # c) menor valor da lista.
# print(f"O Menor valor da lista é: {min(l)} ")
# # d) soma de todos os elementos da lista.
# print(f" A soma dos valores da lista é {sum(l)}")
# # e) lista em ordem crescente.
# l.sort()
# print(l)
# # f) lista em ordem decrescente.
# l.reverse()
# print(l)


# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

# Detetive

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
resp = soma = 0
for p,r in enumerate(perguntas):
    resp = input(f"{r}: ").strip().upper()[0] 
    if resp == "Y":
        alg1 = int((resp.replace("Y","1")))
        soma += alg1    
    else:
        alg1 = int((resp.replace("N","0")))  
        soma -= alg1   
if soma < 2:
  print("Inocente")
elif soma == 2 or soma < 3: 
  print("Suspeito")
elif soma == 3 or soma < 5:
  print("Cumplice")
else:
  print("Assassino")