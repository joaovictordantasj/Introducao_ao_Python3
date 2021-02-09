print('********************************')
print('Bem vindo ao jogo de adivinhação')
print('********************************\n')

numero_secreto = 42

# O "int()" serve para forçar que o input seja um inteiro.
chute = int(input('Digite um número: '))

if (chute == numero_secreto):
    print('\nVocê acertou!')
else:
    print('\nVocê Errou!')

print('\n************')
print('Fim do jogo!')
print('************')
