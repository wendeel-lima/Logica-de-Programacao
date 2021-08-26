# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.

povo = list()

while True:
    pessoa = dict()
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['sexoBiologico'] = input('Digite o sexo biológico: [M/F] ').strip().upper()[0]
    while pessoa['sexoBiologico'] not in 'MF':
        pessoa['sexoBiologico'] = input('Opção inválida. Digite o sexo biológico: [M/F] ').strip().upper()[0]
    if pessoa['sexoBiologico'] == 'M':
        pessoa['sexoBiologico'] = 'masculino'
    else:
        pessoa['sexoBiologico'] = 'feminino'
    pessoa['idade'] = int(input('Digite a idade: '))
    povo.append(pessoa)
    continuar = input('Quer continuar cadastrando? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Opção inválida. Quer continuar cadastrando? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

media = 0
mulheres = list()
for pessoa in povo:
    media += pessoa['idade']/len(povo)
    if pessoa['sexoBiologico'] == 'feminino':
        mulheres.append(pessoa['nome'])

acimaMedia = list()
for pessoa in povo:
    if pessoa['idade'] > media:
        acimaMedia.append(pessoa['idade'])

print(f'''
Estão cadastradas {len(povo)} pessoas.
A média de idade cadastrada é {media:.2f} anos.
Lista de mulheres: {mulheres}
Lista de idades acima da média: {acimaMedia}
''')