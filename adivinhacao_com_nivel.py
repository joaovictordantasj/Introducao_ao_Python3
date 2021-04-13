import random
from os import system
from time import sleep

'''
    REGRAS DO JOGO:
        - A cada chute errado é diminuído uma porcentagem do valor do chute à 
          pontuação de acordo com a dificuldade escolhida;
        - Fácil:   30%
        - Médio:   50%
        - Difícil: 70%
'''

system('clear')

print('*****************************')
print('     Jogo de adivinhação')
print('*****************************\n')

print('Qual o nível de dificuldade?')
dificuldade = int(input('(1) - Fácil;\n(2) - Médio;\n(3) - Difícil;\nR: '))

numero_secreto = random.randint(0, 50)
total_de_tentativas = 0
percentual_de_erro = 0
pontuacao = 1000

if (dificuldade == 1):
    total_de_tentativas = 7
    percentual_de_erro = 0.3
elif (dificuldade == 2):
    total_de_tentativas = 5
    percentual_de_erro = 0.5
elif (dificuldade == 3):
    total_de_tentativas = 3
    percentual_de_erro = 0.7

for rodada in range(1, total_de_tentativas + 1):
    system('clear')
    print('*****************************')
    print('     Jogo de adivinhação')
    #print(f'     {numero_secreto}')
    print('*****************************\n')

    print(f'-=- Tentativa {rodada} / {total_de_tentativas} -=-\n')
    # O "int()" serve para forçar que o input seja um inteiro.
    chute = int(input('Digite um número entre 0 e 50: '))

    if (chute < 0 or chute > 50):
        print('O número não pode ser menor do que 0 ou maior que 50!!!')
        sleep(1.5)
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Parabéns, você acertou!')
        sleep(2)
        break
    elif (menor):
        print(f'\n{chute} é MENOR que o número secreto!')
        pontuacao = pontuacao - \
            abs((chute - numero_secreto) * percentual_de_erro)
        sleep(2)
    elif(maior):
        print(f'\n{chute} é MAIOR que o número secreto!')
        pontuacao = pontuacao - \
            abs((chute - numero_secreto) * percentual_de_erro)
        sleep(2)
    else:
        print('\nValor inválido')

    system('clear')

system('clear')
print('\n*****************************************************************')
print('Fim do jogo!')
print(f'Total de tentativas: {rodada} / {total_de_tentativas}')
print(f'Pontuação final: {pontuacao}')
print('*****************************************************************')
