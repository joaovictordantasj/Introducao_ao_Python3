from os import system

system('clear')

print('*****************************')
print('     Jogo de adivinhação')
print('*****************************\n')

numero_secreto = 42
total_de_tentativas = int(
    input('Quantas tentativas você precisa para advinhar o número secreto: '))
contador = total_de_tentativas
pontuacao = 0

while (contador > 0):
    system('clear')

    print('*****************************')
    print('     Jogo de adivinhação')
    print('*****************************\n')

    # O "int()" serve para forçar que o input seja um inteiro.
    print(f'Tentativa {total_de_tentativas} de {contador}!\n')
    chute = int(input('Digite um número: '))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        pontuacao += 1
    elif (maior or menor):
        pontuacao = pontuacao
    #     print('\nVocê acertou!')
    # elif (maior):
    #     print('\nO seu chute foi maior que o número secreto!')
    # elif (menor):
    #     print('\nO seu chute foi menor que o número secreto!')
    else:
        print('\nNúmero inválido')

    contador -= 1

    system('clear')

print('\n*****************************************************************')
print('Fim do jogo!')
print(f'Você acertou {pontuacao} vez em {total_de_tentativas} tentaivas!')
print('*****************************************************************')
