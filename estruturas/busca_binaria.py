def busca_binaria(clientes, id_cliente):
    esquerda = 0
    direita = len(clientes) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if clientes[meio].id == id_cliente:
            return clientes[meio]

        if clientes[meio].id < id_cliente:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return None


def busca_binaria_recursiva(clientes, id_cliente, esquerda, direita):
    if esquerda > direita:
        return None

    meio = (esquerda + direita) // 2

    if clientes[meio].id == id_cliente:
        return clientes[meio]

    if clientes[meio].id < id_cliente:
        return busca_binaria_recursiva(
            clientes,
            id_cliente,
            meio + 1,
            direita
        )

    return busca_binaria_recursiva(
        clientes,
        id_cliente,
        esquerda,
        meio - 1
    )