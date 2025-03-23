# Encontrar o segundo maior número em uma lista

Numeros = [1, 6, 8, 9, 70, 60]

maior_numero = (max(Numeros))  # Encontra o maior número
Numeros.remove(maior_numero) # Remove o primeiro número

segundo_maior = max(Numeros)

print(f'O segundo maior numero é: {segundo_maior}')