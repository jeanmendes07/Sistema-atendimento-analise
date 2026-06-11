import json

from modelos.cliente import Cliente
from modelos.atendente import Atendente
from modelos.atendimento import Atendimento


def salvar_clientes(clientes, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            [cliente.to_dict() for cliente in clientes],
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def carregar_clientes(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return [
            Cliente.from_dict(item)
            for item in dados
        ]

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_atendentes(atendentes, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            [atendente.to_dict() for atendente in atendentes],
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def carregar_atendentes(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return [
            Atendente.from_dict(item)
            for item in dados
        ]

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_atendimentos(atendimentos, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            [atendimento.to_dict() for atendimento in atendimentos],
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def carregar_atendimentos(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return [
            Atendimento.from_dict(item)
            for item in dados
        ]

    except (FileNotFoundError, json.JSONDecodeError):
        return []