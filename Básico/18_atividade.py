# Simular o funcionamento de um semáforo (imprimindo "Verde", "Amarelo" e "Vermelho" com um intervalo de tempo)

import time

Semafaro = ['verde', 'amarelo', 'vermelho']  # Lista de cores

for cor in Semafaro:  # Itera sobre as cores da lista
    print(f"Semáforo: {cor.upper()}")  # Exibe a cor atual

    if cor == 'vermelho':
        print('Pare!')

    elif cor == 'verde':
        print('Prossiga!')

    elif cor == 'amarelo':
        print('Reduza a velocidade!')

    time.sleep(3)  # Pausa de 3 segundos para simular a troca do semáforo

print("Ciclo do semáforo concluído!")











