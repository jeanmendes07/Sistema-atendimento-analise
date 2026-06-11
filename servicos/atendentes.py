from modelos.atendente import Atendente


class GerenciadorAtendentes:
    def __init__(self):
        self.atendentes = []

    def cadastrar_atendente(self, id_atendente, nome):
        for atendente in self.atendentes:
            if atendente.id == id_atendente:
                return False

        novo_atendente = Atendente(
            id_atendente,
            nome
        )

        self.atendentes.append(novo_atendente)

        return True

    def listar_atendentes(self):
        return self.atendentes

    def buscar_atendente(self, id_atendente):
        for atendente in self.atendentes:
            if atendente.id == id_atendente:
                return atendente

        return None
    
    def carregar_atendentes(self, atendentes):
        self.atendentes = atendentes