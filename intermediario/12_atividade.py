# Construa um sistema de login simples com usuarios e senhas armazenados em um dicionario

usuarios = {
    "usuario1": "senha123",
    "usuario2": "senha456",
    "usuario3": "senha789"
}

# Função para realizar o login
def login():
    print("Bem-vindo ao sistema de login!")
    usuario = input("Digite seu nome de usuários: ")
    senha = input("Digite sua senha: ")

    # Verifica se o usuário existe e a senha está correta
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos. Tente novamente.")

login()

