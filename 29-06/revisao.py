# estado = dict()
# brasil = list()

# for c in range(0,3):
#     estado['uf'] = str(input("Digite a UF: "))
#     estado['Sigla'] = str(input("Digite a sigla: "))
#     brasil.append(estado.copy())

# print(brasil)
# for abacate in brasil:
#     print(abacate)

# for i in brasil:
#     for abacate, banana in i.items():
#         print(f"a {banana}  é {abacate}")


# Faça um programa que tenha uma função chamada área(),
# que recebe as dimensões de um terreno retangular (L + C)
# e mostre a área do terreno.


""" def area(l, c):
    area = l * c
    print(f"A largura é {l}, o comprimento é {c}.")
    print(area)

area(5, 4) """
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada.
# A) de 1 até 10, de 1 em 1
# B) de 10 até 0, de 2 em 2
# C) Uma contagem personalizada.


''' def contador(inicio, fim, passo):
    print(f"A contagem de {inicio} até {fim} com o passo de {passo}:")

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}", end=" ")
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}", end=" ")
            cont -= passo

    print("\nFIM")



contador(1, 10, 1)
contador(10, 0, 2)
contador(2, 10, -2) '''


# Faça um programa que tenha uma função chamada notas()  ok
# que pode receber várias notas de alunos ok
# e vai retornar um dicionário 
# 
# com as seguintes informações:
# - Quantidade de notas ok
# - A maior nota ok
# - A menor nota ok
# - A média da turma ok
# - A situação (opcional)



def notas(*notas, situação=False):
    dicionario = dict()
    dicionario["totalNotas"] = len(notas)
    dicionario["maiorNota"] = max(notas)
    dicionario["menorNota"] = min(notas)
    dicionario["mediaTurma"] = sum(notas)/len(notas)

    if situação == True:
        if dicionario["mediaTurma"] >= 7:
            dicionario["situação"] = "APROVADO"
            
        else:
            dicionario["situação"] = "REPROVADO"

    
    return(dicionario)


resp = notas(10, 5, 8, 9 , 9, 8, 9, situação=True)
print(resp)
