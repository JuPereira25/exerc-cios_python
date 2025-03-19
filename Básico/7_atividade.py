# 7 verifique se um número é positivo, negativo ou zero

contador = 0

while contador < 3:
    Num = int(input('Enter an integer value: \n'))
    
    if (Num > 0):
        print(f'the number {Num} é positive')
    elif (Num < 0):
        print(f'the number {Num} é negative')
    elif (Num == 0):
        print(f'the numeber {Num} é zero')

    contador += 1 #Incrementa e volta o ciclo
    
print('You have made 3 checks. The program will now exit.')





