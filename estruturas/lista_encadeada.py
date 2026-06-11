class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar(self, dado):
        novo_no = No(dado)

        if self.inicio is None:
            self.inicio = novo_no
            return

        atual = self.inicio

        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo_no

    def remover_por_id(self, id_cliente):
        atual = self.inicio
        anterior = None

        while atual:

            if atual.dado.id == id_cliente:

                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                return True

            anterior = atual
            atual = atual.proximo

        return False

    def buscar_por_id(self, id_cliente):
        atual = self.inicio

        while atual:

            if atual.dado.id == id_cliente:
                return atual.dado

            atual = atual.proximo

        return None

    def listar(self):
        clientes = []

        atual = self.inicio

        while atual:
            clientes.append(atual.dado)
            atual = atual.proximo

        return clientes

    def tamanho(self):
        contador = 0
        atual = self.inicio

        while atual:
            contador += 1
            atual = atual.proximo

        return contador