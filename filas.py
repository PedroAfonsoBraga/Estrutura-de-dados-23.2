# Fila (First In First Out - FIFO)
class No:
    def __init__(self, valor):
        self.valor: valor
        self.prox: None


class Queue:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._size = 0

    def push(self, valor):
        """Insere elemento na fila"""
        novo = No(valor)
        if self.fim is None:
            self.fim = novo
        else:
            self.fim.prox = novo
            self.fim = novo
        if self.inicio is None:
            self.inicio = novo

        self._size = self._size + 1

    def pop(self):
        """Remove o valor do topo da fila"""
        if self._size > 0:
            elem = self.inicio.valor
            self.inicio = self.inicio.prox
            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")

    def peek(self):
        """Retorna o valor do topo da fila"""
        if self._size > 0:
            elem = self.inicio.data
            return elem
        raise IndexError("The queue is empty")

    def __len__(self):
        return self.size
