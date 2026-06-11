from modelos.cliente import Cliente
from estruturas.lista_encadeada import ListaEncadeada
from estruturas.busca_binaria import busca_binaria


class GerenciadorClientes:
    def __init__(self):
        self.clientes = []
        self.clientes_ativos = ListaEncadeada()

    def cadastrar_cliente(self, id_cliente, nome, telefone, prioridade=False):
        if busca_binaria(self.clientes, id_cliente):
            return False

        cliente = Cliente(
            id_cliente,
            nome,
            telefone,
            prioridade
        )

        self.clientes.append(cliente)

        self.clientes.sort(key=lambda c: c.id)

        self.clientes_ativos.adicionar(cliente)

        return True

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente(self, id_cliente):
        return busca_binaria(self.clientes, id_cliente)

    def remover_cliente(
    self,
    id_cliente,
    gerenciador_atendimentos=None
    ):
        cliente = self.buscar_cliente(id_cliente)

        if not cliente:
            return False

        if (
            gerenciador_atendimentos
            and
            gerenciador_atendimentos.cliente_em_atendimento(
                id_cliente
            )
        ):
            return False

        cliente.ativo = False

        self.clientes_ativos.remover_por_id(
            id_cliente
        )

        return True
    
    def carregar_clientes(self, clientes):
        self.clientes = sorted(
            clientes,
            key=lambda c: c.id
        )

        for cliente in clientes:
            if cliente.ativo:
                self.clientes_ativos.adicionar(cliente)