from modelos.cliente import Cliente
from estruturas.lista_encadeada import ListaEncadeada


def test_adicionar_cliente():
    lista = ListaEncadeada()

    cliente = Cliente(1, "João", "111")

    lista.adicionar(cliente)

    assert lista.tamanho() == 1