import forca
import adivinhacao_com_nivel
from os import system

system('clear')

print('***********************')
print('* Escolha o seu jogo! *')
print('***********************\n')

op = int(input('[1] - Forca\n[2] - Advinhação\nR: '))

if (op == 1):
    forca.jogar()
elif (op == 2):
    adivinhacao_com_nivel.jogar()
else:
    print('Opção inválida!')
