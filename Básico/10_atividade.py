# Calcule o fatorial de um número

Numero = int(input('Digite um número: '))
resultado = 1

for n in range (1, Numero+1):
    resultado *= n

print('\nO resultado de {0}! é: {1}'.format(Numero, resultado))