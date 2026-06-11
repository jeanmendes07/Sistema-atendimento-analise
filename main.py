from modelos.cliente import Cliente
from modelos.atendente import Atendente


def exibir_menu():
    print("\n=== SISTEMA DE ATENDIMENTO ===")
    print("1 - Clientes")
    print("2 - Atendentes")
    print("3 - Atendimento")
    print("4 - Relatórios")
    print("0 - Sair")


def main():
    cliente_teste = Cliente(
        1,
        "João Silva",
        "11999999999",
        True
    )

    atendente_teste = Atendente(
        1,
        "Maria"
    )

    print(cliente_teste)
    print(atendente_teste)

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando sistema...")
            break

        print("Funcionalidade ainda não implementada.")


if __name__ == "__main__":
    main()