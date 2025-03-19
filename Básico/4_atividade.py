4.	# 4. Verifique se um número é par ou ímpar.

Numero = int(input('Digite um valor inteiro: \n'))

if Numero % 2 == 0: # Se o resto da divisão for zero, o número é par. 
    print('É par')
elif Numero % 2 == 1: #Se o resto da divisão for 1, o número é ímpar. 
    print('É impar')
else:
    print('Duvidas?')

    