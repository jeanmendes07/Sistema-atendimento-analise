from modelos.cliente import Cliente
from estruturas.fila import Fila
from estruturas.pilha import Pilha
from estruturas.lista_encadeada import ListaEncadeada


def exibir_menu():
    print("\n=== SISTEMA DE ATENDIMENTO ===")
    print("1 - Clientes")
    print("2 - Atendentes")
    print("3 - Atendimento")
    print("4 - Relatórios")
    print("0 - Sair")


def testar_estruturas():
    print("\n=== TESTE FILA ===")

    fila = Fila()

    fila.enfileirar("Cliente A")
    fila.enfileirar("Cliente B")

    print("Primeiro:", fila.primeiro())
    print("Saiu:", fila.desenfileirar())

    print("\n=== TESTE PILHA ===")

    pilha = Pilha()

    pilha.empilhar("Atendimento 1")
    pilha.empilhar("Atendimento 2")

    print("Topo:", pilha.topo())
    print("Desempilhado:", pilha.desempilhar())

    print("\n=== TESTE LISTA ENCADEADA ===")

    lista = ListaEncadeada()

    cliente1 = Cliente(1, "João", "1111")
    cliente2 = Cliente(2, "Maria", "2222")

    lista.adicionar(cliente1)
    lista.adicionar(cliente2)

    for cliente in lista.listar():
        print(cliente)


def main():
    testar_estruturas()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando sistema...")
            break

        print("Funcionalidade ainda não implementada.")


if __name__ == "__main__":
    main()