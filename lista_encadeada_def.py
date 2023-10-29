class No:
    """Criando um novo nó na lista"""

    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None


class Lista:
    def __init__(self):
        self.header = None
        self._size = 0

    def inserir(self, valor):
        if (self.header):
            # outras inserções
            pointer = self.header
            while (pointer.proximo):
                pointer = pointer.proximo
            pointer.proximo = No(valor)
        else:
            # primeira inserção
            self.header = No(valor)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista encadeada"""
        return self._size

    def busca(self, valor):
        pointer = self.header
        i = 0
        while (pointer):
            if pointer.data == valor:
                return i
            pointer = pointer.proximo
            i = i + 1
        raise ValueError("Não está na lista")

    def remove(self, elem):
        if (self.header == None):
            raise ValueError("Lista vazia")
        elif (self.header == elem):
            self.header = pointer.proximo
            return True
        else:
            antecessor = self.header
            pointer = self.header.proximo
            while (pointer):
                if (pointer.valor == elem):
                    antecessor.proximo = pointer.proximo
                    pointer.proximo = None
                antecessor = pointer
                pointer = pointer.proximo
            return True
        raise ValueError("{} is not in the list".format(elem))


lista = Lista()
lista.inserir(2)
lista.inserir(3)
lista.inserir(4)
lista.inserir(5)
lista.remove(4)
