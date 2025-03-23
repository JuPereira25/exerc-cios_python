# Ordenar uma lista de números usando o algoritmo Bubble Sort

def bubble_sort(elemento):
    n = len(elemento)
    for i in range(n):  # Correção no for
        print(f'Iteração {i + 1}: {elemento}')
        for j in range(0, n - i - 1):  # Correção no range do segundo for
            if elemento[j] > elemento[j + 1]:
                elemento[j], elemento[j + 1] = elemento[j + 1], elemento[j]  # Troca os elementos
    print(f'Resultado final: {elemento}')
    return elemento

lista = [2, -5, 7, 90, 1]
bubble_sort(lista)
