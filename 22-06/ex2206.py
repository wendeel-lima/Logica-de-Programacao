# Exercícios – Dicionários

# 1. Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9
# (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}

# lista = dict()

# lista[1] = 1**2
# lista[4] = 4**2
# lista[5] = 5**2
# lista[6] = 6**2
# lista[7] = 7**2
# lista[9] = 9**2

# print(lista)

# 2. Exercício Treino - Crie um dicionário em que suas chaves correspondem a números
# inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# lista = dict()

# for c in range(1,11):
#     lista[c] = c**2
# print(lista)

# 3. Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.
    
# if nome_media[] >= 7:
#     print(f"o aluno(a) {nome_media['nome']} esta APROVADO!!")
# elif nome_media["media"] == 5 and nome_media["media"] <= 6.9:
#     print(f"o aluno(a) {nome_media['nome']} esta DE RECUPERAÇÃO!!")
# else:
#     print(f"o aluno(a) {nome_media['nome']} esta REPROVADO!!")

# 4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastreos (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade
# , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve
# contribuir por 35 anos para se aposentar.




# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.



# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.


# 6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve 
# receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que
# calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios
# apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as
# situações dos 15 alunos de uma vez só.

classe = list()

for i in range(2):
    aluno = dict()
    aluno['nome'] = input('Digite o nome: ').capitalize()
    aluno['notas'] = list()
    media = 0
    for j in range(2):
        nota = float(input(f'Digite a {j+1}ª nota '))
        aluno['notas'].append(nota)
        media += nota/5
    aluno['media'] = round(media, 2)
    if aluno['media'] >= 7:
        aluno['situacao'] = 'aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situacao'] = 'recuperação'
    else:
        aluno['situacao'] = 'reprovado'
    classe.append(aluno)
    # print(aluno)
print()
print(f'{"Nome":^25} {"Notas":^25} {"Média":^25} {"Situação":^25}')
print(f"-"*60)
for aluno in classe:
    # notas = " - ".join([str(f'{n:.2f}') for n in aluno['notas']])
     print(f'{aluno["nome"]:^25}')