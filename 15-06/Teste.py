from random import randint # biblioteca para gerar números inteiros aleatorios
    
# Variável para contar as vitórias01
vitoria = 0
# Laço infinito até o break 

while True:
   jogador = int(input('Diga um valor: ')) 
   computador = randint(0, 10) 
   # Soma o valor do user com do pc
   total = jogador + computador 
   # Inicializa a variável tipo
   tipo = ' ' 
   # Laço para repetir a pergunta de par ou impar até que seja digitado P ou I
   while tipo not in 'PI': 
      # Recebe P ou I do user, tirando os espaço, colcoando a letra em maiuscula e pagando apenas a primeira letra
      tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
   # Mostrando o resultado do jogador mais o computador
   print(f'Você jogou {jogador} e computador {computador}. Total de {total}')

   # Verificando se eu digitei P no tipo
   if tipo == 'P':
      # Verificando se o total é par
      if total % 2 == 0:
         # Mostrando que venci
         print('Você venceu!')
         # Somando mais UMA vitória para mim
         vitoria += 1
      else:
         # Senão eu perdi
         print('Você perdeu!')
         # Dai o laço infinito para
         break
   # Veirificando de digitei I
   elif tipo == 'I':
      # Verificando se o total foi impar
      if total % 2 != 0:
         # Mostra que venci
         print('Você venceu!')
         # Adiciona mais UMA vitória pra mim
         vitoria += 1
      else:
         # Mostra se perdi
         print('Você perdeu!')
         # Para o laço infinito
         break
   # Se venci, fala para eu continuar o jogo e volta pro começo do laço infinito
   print('\nVamos jogar novamente...')
# Se entrar no break finaliza o jogo e mostra minhas vitórias.
print(f'GAME OVER! Você venceu {vitoria} vezes')

#------------------------------------------------

# Exercicio