# Criar uma função que receba uma string e retorne sua versão invertida

def Palavrainvertida(palavra):
    string = palavra[::-1]
    return string

palavra = str(input('Digite uma palavra: '))
invertida = Palavrainvertida(palavra)

# Mostrar os resultados
print('Você digitou: {}'.format(palavra))
print('A palavra que você digitou invertida fica: {}'.format(invertida))
