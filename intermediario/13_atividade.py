# Crie um sistema de agenda que permita adicionar, remover e listar contatos

# Dicionário para armazenar os contatos
contatos = {}

def adicionar_contato(nome, telefone):
    contatos[nome] = telefone
    print(f"Contato de {nome} adicionado com sucesso.")

def remover_contato(nome):
    if nome in contatos:
        del contatos[nome]
        print(f"Contato de {nome} removido com sucesso.")
    else:
        print(f"Contato {nome} não encontrado.")

def listar_contatos():
    if contatos:
        print("Lista de Contatos:")
        for nome, telefone in contatos.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    else:
        print("Nenhum contato encontrado.")

while True:
    # Exibe o menu e recebe a escolha do usuário
    menu = input("Escolha uma opção abaixo: \n"
                 "[1] Adicionar\n"
                 "[2] Remover\n"
                 "[3] Listar Contatos\n"
                 "[4] Sair\n")
    
    # Adicionar contato
    if menu == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(nome, telefone)
    
    # Remover contato
    elif menu == '2':
        nome = input("Digite o nome do contato a ser removido: ")
        remover_contato(nome)
    
    # Listar todos os contatos
    elif menu == '3':
        listar_contatos()
    
    # Sair do sistema
    elif menu == '4':
        print("Agenda encerrada.")
        break
    
    # Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida! Tente novamente.")
