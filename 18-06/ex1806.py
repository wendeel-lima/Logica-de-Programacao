# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.
lista1 = list()
maior = menor = 0
for c in range(2):
    lista_temp = list()
    lista_temp.append(str(input("Digite o nome: ")))
    lista_temp.append(int(input("Digite a idade: ")))
    lista1.append(lista_temp[:])
    c += 1
for p in lista1:
    if p[1] >= 18:
        print(f" {p[0]} é maior de idade ")
        maior += 1
    else:
        print(f" {p[0]} é menor de idade ")
        menor += 1
print(f"O total de maiores de 18 anos é '{maior}' e menores de 18 anos é '{menor}'")

