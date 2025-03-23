# Gere um número aleatorio e peça ao usuario para adivinhar.
import random

# Lista de números possíveis
numeros = [1, 6, 8, 1, 4, 9]

numero_sorteado = random.choice(numeros)

advinhe = int(input('Tente adivinhar o número sorteado: \n'))

if advinhe == numero_sorteado:
    print(f'Parabéns! Você acertou! O número sorteado foi {numero_sorteado}.')
else:
    print(f'Você errou! O número sorteado era {numero_sorteado}.')
