from estruturas.fila import Fila


def test_enfileirar():
    fila = Fila()

    fila.enfileirar(1)

    assert fila.tamanho() == 1


def test_desenfileirar():
    fila = Fila()

    fila.enfileirar(10)

    assert fila.desenfileirar() == 10