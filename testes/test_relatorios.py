from modelos.atendimento import Atendimento
from servicos.relatorios import Relatorios


def test_tempo_medio():

    a1 = Atendimento(
        1,
        1,
        1
    )

    a1.duracao = 10

    a2 = Atendimento(
        2,
        2,
        1
    )

    a2.duracao = 20

    media = (
        Relatorios.tempo_medio_atendimento(
            [a1, a2]
        )
    )

    assert media == 15


def test_merge_sort():

    a1 = Atendimento(
        1,
        1,
        1
    )

    a2 = Atendimento(
        2,
        2,
        1
    )

    a1.duracao = 30
    a2.duracao = 10

    resultado = Relatorios.merge_sort(
        [a1, a2]
    )

    assert resultado[0].duracao == 10

    def test_top_5():

        a1 = Atendimento(1, 1, 1)
        a2 = Atendimento(2, 1, 1)
        a3 = Atendimento(3, 2, 1)

        ranking = Relatorios.top_5_clientes(
            [a1, a2, a3]
        )

        assert ranking[0][0] == 1