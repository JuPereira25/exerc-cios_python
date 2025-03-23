# Criar uma função que recebe uma lista e remove os elementos duplicados

def RemoverDuplicados(lista):
    lista_sem_duplicatas = list(set(lista))
    return lista_sem_duplicatas

lista = [1, 2, 3, 3, 5, 6, 8, 9, 9]

lista_sem_duplicatas = RemoverDuplicados(lista)

print(lista_sem_duplicatas)