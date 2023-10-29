class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinariaDeBusca:
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

    def altura(self, no=None):
        if no is None:
            no = self.raiz

        altura_esq = 0
        altura_dir = 0

        if no.esquerda:
            altura_esq = self.altura(self, no.esquerda)
        if no.direita:
            altura_dir = self.altura(self, no.direita)

        if altura_dir > altura_esq:
            return altura_dir + 1
        return altura_esq + 1
