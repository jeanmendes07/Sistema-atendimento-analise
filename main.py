from servicos.clientes import GerenciadorClientes
from servicos.atendentes import GerenciadorAtendentes


clientes = GerenciadorClientes()
atendentes = GerenciadorAtendentes()


def menu_clientes():
    while True:
        print("\n=== CLIENTES ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar por ID")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "0":
            return

        elif opcao == "1":
            try:
                id_cliente = int(input("ID: "))
                nome = input("Nome: ")
                telefone = input("Telefone: ")

                prioridade = (
                    input("Prioridade? (s/n): ").lower() == "s"
                )

                if clientes.cadastrar_cliente(
                    id_cliente,
                    nome,
                    telefone,
                    prioridade
                ):
                    print("Cliente cadastrado.")
                else:
                    print("ID já existe.")

            except ValueError:
                print("Entrada inválida.")

        elif opcao == "2":
            lista = clientes.listar_clientes()

            if not lista:
                print("Nenhum cliente cadastrado.")
                continue

            for cliente in lista:
                print(cliente)

        elif opcao == "3":
            try:
                id_cliente = int(input("ID: "))

                cliente = clientes.buscar_cliente(id_cliente)

                if cliente:
                    print(cliente)
                else:
                    print("Cliente não encontrado.")

            except ValueError:
                print("ID inválido.")


def menu_atendentes():
    while True:
        print("\n=== ATENDENTES ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "0":
            return

        elif opcao == "1":
            try:
                id_atendente = int(input("ID: "))
                nome = input("Nome: ")

                if atendentes.cadastrar_atendente(
                    id_atendente,
                    nome
                ):
                    print("Atendente cadastrado.")
                else:
                    print("ID já existe.")

            except ValueError:
                print("Entrada inválida.")

        elif opcao == "2":
            lista = atendentes.listar_atendentes()

            if not lista:
                print("Nenhum atendente cadastrado.")
                continue

            for atendente in lista:
                print(atendente)


def exibir_menu():
    print("\n=== SISTEMA DE ATENDIMENTO ===")
    print("1 - Clientes")
    print("2 - Atendentes")
    print("3 - Atendimento")
    print("4 - Relatórios")
    print("0 - Sair")


def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando sistema...")
            break

        elif opcao == "1":
            menu_clientes()

        elif opcao == "2":
            menu_atendentes()

        else:
            print("Funcionalidade ainda não implementada.")


if __name__ == "__main__":
    main()