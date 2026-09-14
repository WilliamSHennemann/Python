agenda = {
    "Ana": "51999999999",
    "Carlos": "51988888888",
    "Maria": "51977777777",
}

while True:
    print("\n1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Alterar telefone")
    print("4 - Remover contato")
    print("5 - Listar contatos")
    print("0 - Sair")
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome: ")
        agenda[nome] = input("Telefone: ")
        print("Contato adicionado.")
    elif opcao == "2":
        nome = input("Nome do contato: ")
        print(agenda.get(nome, "Contato nao encontrado."))
    elif opcao == "3":
        nome = input("Nome do contato: ")
        if nome in agenda:
            agenda[nome] = input("Novo telefone: ")
            print("Telefone alterado.")
        else:
            print("Contato nao encontrado.")
    elif opcao == "4":
        nome = input("Nome do contato: ")
        if nome in agenda:
            del agenda[nome]
            print("Contato removido.")
        else:
            print("Contato nao encontrado.")
    elif opcao == "5":
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")
    elif opcao == "0":
        print("Saindo da agenda.")
        break
    else:
        print("Opcao invalida.")
