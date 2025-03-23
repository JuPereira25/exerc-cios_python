# Ler um arquivo de texto e conte quantas palavras ele tem

def contarPalavras(texto):
    palavras = texto.split()
    return len(palavras)

texto = "Olá, isso é um exemplo de contagem de palavras!"
numero_de_palavras = contarPalavras(texto)
print(f'O número de palavras é: {numero_de_palavras}')