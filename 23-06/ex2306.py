

# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
       return f'Com {idade} anos o voto é NEGADO'
    elif 16 <= idade < 18 or idade >= 70:
       return f'Com {idade} anos o voto é OPCIONAL'
    else:
       return f'Com {idade} anos o voto é OBRIGATORIO' 

nasc = int(input("digite seu ano de nascimento: "))
print(voto(nasc))

# Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

# def pos_neg(n):
#    numero = n
#    if numero <= 0:
#       return f'N'
#    else:
#       return f'P'
# n = int(input("Digite um numero: "))
# print(pos_neg(n))


# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.


def func1(a, b, c):
   s = a + b + c
   return s

def media(func1):
   m = func1 / 3
   return f" A media é {m:.2f}"

n1 = float(input("DIGITE UM NUMERO: "))
n2 = float(input("DIGITE UM NUMERO: "))
n3 = float(input("DIGITE UM NUMERO: "))

print(func1(n1,n2,n3))
print(media(func1(n1,n2,n3)))
