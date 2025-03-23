# Criar uma calculadora que aceita quatro operações(+,-,*,/)


Num1 = int(input('Digite o primeiro valor para calcular: \n'))
Num2= int(input('Digite o segundo valor para calcular: \n'))

while True:
    opcao = int(input(('Escolha a operação: '
         '[1] SOMAR'
         '[2] MULTIPLICAR'
         '[3] SUBTRAIR'
         '[4] DIVIDIR'
         '[5] OPERAÇÃO ENCERRADA \n')))

    if opcao == 1:
        print(f'A soma do {Num1} + {Num2} é: {Num1 + Num2}\n')

    elif opcao == 2:
        print(f'A multiplicação do {Num1} * {Num2} é: {Num1 * Num2}\n')

    elif opcao == 3:
        print(f'A subtração do {Num1} - {Num2} é: {Num1 - Num2}\n')

    elif opcao == 4:
        print(f'A divisão do {Num1} / {Num2} é: {Num1 / Num2}\n')

    elif opcao == 5:
        print('Operação encerrada.')
        break  # Sai do loop

    else:
        print('Opção inválida! Escolha um número entre 1 e 5.\n')