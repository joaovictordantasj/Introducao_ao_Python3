from os import system
import random

system('clear')

print('*****************************')
print('     Jogo de adivinhação')
print('*****************************\n')

numero_secreto = random.randint(0, 50)
total_de_tentativas = 1
pontuacao = 1000

while (1):
    system('clear')

    print('*****************************')
    print('     Jogo de adivinhação')
    print(f'     {numero_secreto}')
    print('*****************************\n')

    # O "int()" serve para forçar que o input seja um inteiro.
    print(f'-=- Tentativa {total_de_tentativas} -=-\n')
    chute = int(input('Digite um número: '))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        break
    elif (maior or menor):
        pontuacao = pontuacao - (chute / 2)
    else:
        print('\nValor inválido')

    total_de_tentativas += 1

    system('clear')

system('clear')
print('\n*****************************************************************')
print('Fim do jogo!')
print(f'Total de tentativas: {total_de_tentativas}')
print(f'Pontuação final: {pontuacao}')
print('*****************************************************************')
