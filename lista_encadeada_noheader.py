class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None


class ListaOrdenada:
    def __init__(self):
        self.header = No()

    def inserir(self, valor):
        novo_no = No(valor)
        atual = self.header
        while atual.proximo != None and atual.proximo.valor < valor:
            atual = atual.proximo
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
