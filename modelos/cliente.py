class Cliente:
    def __init__(self, id_cliente, nome, telefone, prioridade=False):
        self.id = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.prioridade = prioridade
        self.ativo = True

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "prioridade": self.prioridade,
            "ativo": self.ativo
        }

    @classmethod
    def from_dict(cls, dados):
        cliente = cls(
            dados["id"],
            dados["nome"],
            dados["telefone"],
            dados["prioridade"]
        )
        cliente.ativo = dados.get("ativo", True)
        return cliente

    def __str__(self):
        tipo = "PRIORIDADE" if self.prioridade else "NORMAL"
        return f"[{self.id}] {self.nome} - {tipo}"