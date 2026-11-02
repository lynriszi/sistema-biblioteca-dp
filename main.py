while True:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Consultar livro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Cadastro de livros")

    elif opcao == "2":
        print("Listagem de livros")

    elif opcao == "3":
        print("Consulta de livros")

    elif opcao == "0":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida!")
