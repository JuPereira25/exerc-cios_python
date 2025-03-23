# Gerar uma tabela de multiplicação de um número informado pelo usuário.

def multiplicação(x):
    for i in range(1, 11):  # Gera a tabela de 1 a 10
        resultado = x * i
        print(f'{x} * {i} = {resultado}')

Numero = int(input('Digite um número para tabular: \n'))

# Chama a função passando o número digitado pelo usuário
multiplicação(Numero)






