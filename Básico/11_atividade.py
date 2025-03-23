# Gera uma sequência de Fibonacci até um número dado
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequencia = fibonacci_recursive(n - 1)
        proximo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_numero)
        return sequencia

n = 10
resultado = fibonacci_recursive(n)
print(resultado)
