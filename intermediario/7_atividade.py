# Substituir todas as ocorrências de uma palavra em um arquivo por outra

def substituirPalavras(texto, palavra_antiga, palavra_nova):
    return texto.replace(palavra_antiga, palavra_nova)

texto = "Eu gosto de programar em Python"
novo_texto = substituirPalavras(texto, "Python", "Java")
print(novo_texto)