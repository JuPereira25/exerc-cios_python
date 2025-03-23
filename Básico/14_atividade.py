# Verificar se há vogais em uma string

Frase = input('Digite uma frase: ')
print('Você digitou:', Frase)

vogais = ['a', 'e', 'i', 'o', 'u']

# Verificar se alguma vogal está na frase
tem_vogal = any(vogal in Frase.lower() for vogal in vogais)

if tem_vogal:
    print(f'A frase "{Frase}" tem vogais.')
else:
    print(f'A frase "{Frase}" não tem vogais.')
