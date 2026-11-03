livros = []

def cadastrar_livro():
    titulo = input("Digite o título do livro: ")

    if titulo == "":
        print("Título inválido!")
    else:
        livro = {
            "codigo": len(livros) + 1,
            "titulo": titulo
        }

        livros.append(livro)
        print("Livro cadastrado!")

opcao = -1

while opcao != 0:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Consultar livro")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_livro()

    elif opcao == 2:
        listar_livros()

    elif opcao == 3:
        consultar_livro()

    elif opcao == 0:
        print("Encerrando programa...")

    else:
        print("Opção inválida!")