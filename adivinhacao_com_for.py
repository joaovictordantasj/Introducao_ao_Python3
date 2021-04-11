import random
from os import system
from time import sleep

system('clear')

print('*****************************')
print('     Jogo de adivinhação')
print('*****************************\n')

numero_secreto = random.randint(0, 50)
total_de_tentativas = 3
pontuacao = 1000

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
        pontuacao = pontuacao - (chute * 2)
        sleep(2)
    elif(maior):
        print(f'\n{chute} é MAIOR que o número secreto!')
        pontuacao = pontuacao - (chute * 2)
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
