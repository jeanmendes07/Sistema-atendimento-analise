import csv


class Relatorios:

    @staticmethod
    def tempo_medio_atendimento(atendimentos):
        if not atendimentos:
            return 0

        total = sum(
            atendimento.duracao
            for atendimento in atendimentos
        )

        return total / len(atendimentos)

    @staticmethod
    def merge_sort(lista):
        if len(lista) <= 1:
            return lista

        meio = len(lista) // 2

        esquerda = Relatorios.merge_sort(
            lista[:meio]
        )

        direita = Relatorios.merge_sort(
            lista[meio:]
        )

        return Relatorios._merge(
            esquerda,
            direita
        )

    @staticmethod
    def _merge(esquerda, direita):
        resultado = []

        i = 0
        j = 0

        while (
            i < len(esquerda)
            and
            j < len(direita)
        ):

            if esquerda[i].duracao <= direita[j].duracao:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1

        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])

        return resultado

    @staticmethod
    def top_5_clientes(atendimentos):
        contador = {}

        for atendimento in atendimentos:

            cliente = atendimento.cliente_id

            contador[cliente] = (
                contador.get(cliente, 0)
                + 1
            )

        ranking = sorted(
            contador.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return ranking[:5]

    @staticmethod
    def exportar_csv(atendimentos, caminho):
        with open(
            caminho,
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            escritor = csv.writer(arquivo)

            escritor.writerow([
                "ID",
                "Cliente",
                "Atendente",
                "Duracao",
                "Status"
            ])

            for atendimento in atendimentos:

                escritor.writerow([
                    atendimento.id,
                    atendimento.cliente_id,
                    atendimento.atendente_id,
                    atendimento.duracao,
                    atendimento.status
                ])