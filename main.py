def listar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado!")
    else:
        print("\n=== LIVROS CADASTRADOS ===")

        for livro in livros:
            print("Código:", livro["codigo"])
            print("Título:", livro["titulo"])
            print("--------------------")

def consultar_livro():
    codigo = int(input("Digite o código do livro: "))

    encontrado = False

    for livro in livros:
        if livro["codigo"] == codigo:
            print("Livro encontrado!")
            print("Título:", livro["titulo"])
            encontrado = True

    if encontrado == False:
        print("Livro não encontrado!")

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
