class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.valor)


class ArvoreBinaria:
    def __init__(self, valor=None):
        no = No(valor)
        self.raiz = no

    def simetrico(self, no=None):  # em ordem
        if no is None:
            no = self.raiz
        if no.esquerda:
            self.simetrico(no.esquerda)
        print(no)
        if no.direita:
            self.simetrico(no.direita)

    def pre_ordem(self, no=None):
        if no is None:
            no = self.raiz
        print(no)
        if no.esquerda:
            self.pre_ordem(no.esquerda)
        if no.direita:
            self.pre_ordem(no.direita)

    def pos_ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no.esquerda:
            self.pos_ordem(no.esquerda)
        if no.direita:
            self.pos_ordem(no.direita)
        print(no)

    def altura(self, no=None):
        if no is None:
            no = self.root

        altura_esquerda = 0
        altura_direita = 0

        if no.esquerda:
            altura_esquerda = self.altura(self, no.esquerda)
        if no.direita:
            altura_direita = self.altura(self, no.direita)

        if altura_direita > altura_esquerda:
            return altura_direita + 1
        return altura_esquerda + 1


arvore = ArvoreBinaria(1)
arvore.raiz.esquerda = No(2)
arvore.raiz.direita = No(3)
arvore.pre_ordem()
