from servicos.clientes import GerenciadorClientes


def test_cadastro_cliente():
    gerenciador = GerenciadorClientes()

    resultado = gerenciador.cadastrar_cliente(
        1,
        "João",
        "111"
    )

    assert resultado is True


def test_busca_cliente():
    gerenciador = GerenciadorClientes()

    gerenciador.cadastrar_cliente(
        1,
        "João",
        "111"
    )

    cliente = gerenciador.buscar_cliente(1)

    assert cliente.nome == "João"