print('********************************')
print('Bem vindo ao jogo de adivinhação')
print('********************************\n')

numero_secreto = 42

# O "int()" serve para forçar que o input seja um inteiro.
chute = int(input('Digite um número: '))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print('\nVocê acertou!')
elif (maior):
    print('\nO seu chute foi maior que o número secreto!')
elif (menor):
    print('\nO seu chute foi menor que o número secreto!')
else:
    print('\nNúmero inválido')

print('\n************')
print('Fim do jogo!')
print('************')
