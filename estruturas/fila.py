class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if self.esta_vazia():
            return None

        return self.itens.pop(0)

    def primeiro(self):
        if self.esta_vazia():
            return None

        return self.itens[0]

    def tamanho(self):
        return len(self.itens)

    def listar(self):
        return self.itens.copy()