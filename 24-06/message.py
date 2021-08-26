#1. Crie um programa que leia nome, sexo biologico e idade de várias pessoas, 
#2. guardando os dados de cada pessoa em um dicionário 
#3. todos os dicionários em uma lista. 
#4. OBS: O programa deve garantir que o genero digitado seja válido, e que quando perguntar ao usuário se 
# deseja continuar a resposta seja somente sim ou não.​ 

''' Lembrando sempre que é mais fácil entender e resolver o exercício em partes!'''

galera = list() # precisamos criar essa lista porque o exercício pede que os dicionários sejam guardados em listas!
pessoa = dict() # dicionário que criamos para salvar os dados de cada pessoa!
soma = media = 0 # variáveis criadas para resolução da parte B do exercício

# Utilizamos o WHILE TRUE porque queremos fazer VERIFICAÇÕES (com os ifs) para GARANTIR
# que o usuário só digite F M N no gênero e para que o usuário só digite S N para continuar ou não.

while True:
    pessoa['nome'] = str(input("NOME: ")) # para adicionar algo no dicionário utilizando input usamos essa estrutura
    
    # Mais um WHILE TRUE - neste caso, ele está garantindo que o genero digitado seja apenas F M N.
    while True:
        pessoa['genero'] = str(input("GENERO (F/M/N): ")).upper()[0]
        if pessoa['genero'] in 'FMN':
            break
        print("ERRO! Digite apenas M, N ou F. ")

    pessoa['idade'] = int(input("IDADE: "))
    galera.append(pessoa.copy()) # estrutura que permite que coloquemos um dicionário dentro de uma lista
    soma += pessoa['idade'] # estamos realizando aqui a soma das idades adicionadas na variável soma (parte B do exercício)

    # Este WHILE TRUE faz a mesma função do anterior. Garante que o usuário só digite S ou N.
    while True:
        resp = str(input("Deseja continuar? (S/N): ")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Digite apenas S ou N")
    
    # Condicional que acaba com nosso WHILE TRUE principal (se o usuário digitar N, acabou o cadastro de pessoas)
    if resp == 'N':
        break

print('--'*30) # formatação
print(galera) # mostra nossa lista de dicionários!

# No final, mostre:​ 
# A) Quantas pessoas estão cadastradas.​ 
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas. ") # len(galera) mostra o tamanho de galera (quantos dict tem)
print('--'*30) # formatação

# B) A média da idade.​ 
media = soma / len(galera)
print(f"B) A média de idade é {media:.2f} anos.")
print('--'*30) # formatação

# C) Uma lista com as mulheres.​ 
print(f"C) A lista de mulheres cadastradas foi: ")
for p in galera:
    if p['genero'] in 'Ff':
        print(f" {p['nome']} ", end='')
print('--'*30) # formatação

# D) Uma lista com as idades que estão acima da média.​ 
print('D) Lista de pessoas que estão acima da média: ')

for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f"{k} = {v}")
print('--'*30) # formatação