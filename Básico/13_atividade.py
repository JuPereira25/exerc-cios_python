# Verifique se uma palavra é um palíndromo

palavra = str(input('Digite uma palavra: '))
print(' Você digitou: {}'.format(palavra))

if palavra == palavra[::-1]:
    print(f'A {palavra} é um palíndromo')
else:
    print(f'{palavra} não é um palíndromo')

