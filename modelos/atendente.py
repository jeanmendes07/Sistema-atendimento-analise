class Atendente:
    def __init__(self, id_atendente, nome):
        self.id = id_atendente
        self.nome = nome
        self.ocupado = False

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "ocupado": self.ocupado
        }

    @classmethod
    def from_dict(cls, dados):
        atendente = cls(
            dados["id"],
            dados["nome"]
        )
        atendente.ocupado = dados.get("ocupado", False)
        return atendente

    def __str__(self):
        status = "Ocupado" if self.ocupado else "Livre"
        return f"[{self.id}] {self.nome} - {status}"