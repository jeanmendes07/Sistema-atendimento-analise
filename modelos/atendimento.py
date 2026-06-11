from datetime import datetime


class Atendimento:
    def __init__(
        self,
        id_atendimento,
        cliente_id,
        atendente_id,
        data_inicio=None
    ):
        self.id = id_atendimento
        self.cliente_id = cliente_id
        self.atendente_id = atendente_id

        self.data_inicio = (
            data_inicio
            if data_inicio
            else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        self.data_fim = None
        self.duracao = 0
        self.status = "EM_ANDAMENTO"

    def finalizar(self, duracao):
        self.data_fim = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.duracao = duracao
        self.status = "FINALIZADO"

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "atendente_id": self.atendente_id,
            "data_inicio": self.data_inicio,
            "data_fim": self.data_fim,
            "duracao": self.duracao,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, dados):
        atendimento = cls(
            dados["id"],
            dados["cliente_id"],
            dados["atendente_id"],
            dados["data_inicio"]
        )

        atendimento.data_fim = dados["data_fim"]
        atendimento.duracao = dados["duracao"]
        atendimento.status = dados["status"]

        return atendimento

    def __str__(self):
        return (
            f"Atendimento {self.id} | "
            f"Cliente {self.cliente_id} | "
            f"Status: {self.status}"
        )