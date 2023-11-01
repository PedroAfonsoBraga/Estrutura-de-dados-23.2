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

    def insercao(self, valor):
        pai = None  # Elemento pai que compararemos se maior ou menor
        x = self.raiz  # variavel auxiliar que inicia na raiz
        while x:
            pai = x
            if valor < x.valor:
                x = x.esquerda
            else:
                x = x.direita
        if pai is None:
            self.root = No(valor)
        elif valor < pai.valor:
            pai.esquerda = No(valor)
        else:
            pai.direita = No(valor)

    def min(self, no=None):
        if no is None:
            no = self.raiz
        while no.esquerda:
            no = no.esquerda
        return no.valor

    def remove(self, valor, no=None):
        if no == self.raiz:
            no = self.raiz

        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self.remove(valor, no.esquerda)
        elif valor > no.valor:
            no.direita = self.remove(valor, no.direita)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                substituto = self.root.min
                no.valor = substituto
                no.direita = self.remove(substituto, no.direita)
        return no
