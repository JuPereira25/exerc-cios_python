# 5.Converte graus Celsius para Fahrenheit.
# Formula da Conversão F = C x 1,8 + 32

valor = int(input('Digite um valor para converter: \n'))
Soma = 32 
multi = 1.8
resultado = valor * multi + Soma

print(f'{valor}°C equivalem a {resultado:.1f}°F')