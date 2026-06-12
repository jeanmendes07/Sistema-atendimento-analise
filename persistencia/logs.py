from datetime import datetime


def registrar_log(mensagem):
    with open(
        "dados/logs.txt",
        "a",
        encoding="utf-8"
    ) as arquivo:

        horario = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        arquivo.write(
            f"[{horario}] {mensagem}\n"
        )