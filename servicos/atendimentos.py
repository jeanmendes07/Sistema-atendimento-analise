from modelos.atendimento import Atendimento
from estruturas.fila import Fila
from estruturas.pilha import Pilha


class GerenciadorAtendimentos:
    def __init__(self):
        self.fila_prioridade = Fila()
        self.fila_normal = Fila()

        self.atendimentos = []
        self.atendimentos_abertos = {}

        self.pilha_desfazer = Pilha()

        self.proximo_id = 1

    def abrir_atendimento(self, cliente):
        if cliente.prioridade:
            self.fila_prioridade.enfileirar(cliente)
        else:
            self.fila_normal.enfileirar(cliente)

    def chamar_proximo(self, atendente):
        if atendente.ocupado:
            return None

        cliente = None

        if not self.fila_prioridade.esta_vazia():
            cliente = self.fila_prioridade.desenfileirar()

        elif not self.fila_normal.esta_vazia():
            cliente = self.fila_normal.desenfileirar()

        if cliente is None:
            return None

        atendimento = Atendimento(
            self.proximo_id,
            cliente.id,
            atendente.id
        )

        self.proximo_id += 1

        atendente.ocupado = True

        self.atendimentos_abertos[atendente.id] = atendimento

        return atendimento

    def finalizar_atendimento(self, atendente, duracao):

        atendimento = self.atendimentos_abertos.get(
            atendente.id
        )

        if atendimento is None:
            return False

        atendimento.finalizar(duracao)

        self.atendimentos.append(atendimento)

        self.pilha_desfazer.empilhar(atendimento)

        del self.atendimentos_abertos[atendente.id]

        atendente.ocupado = False

        return True
    
    def cliente_em_atendimento(self, id_cliente):
        for atendimento in self.atendimentos_abertos.values():

            if atendimento.cliente_id == id_cliente:
                return True

        return False

    def desfazer_ultima_finalizacao(self):
        ultimo = self.pilha_desfazer.desempilhar()

        if ultimo is None:
            return False

        self.atendimentos.remove(ultimo)

        return True

    def historico_cliente(self, id_cliente):
        return [
            atendimento
            for atendimento in self.atendimentos
            if atendimento.cliente_id == id_cliente
        ]