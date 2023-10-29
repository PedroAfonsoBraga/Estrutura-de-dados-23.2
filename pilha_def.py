# Pilhas (Last In First Out- LIFO)
# inserir, remover e observar o valor do topo da pilha
class No:
    def __init__(self):
        self.valor: 0
        self.prox: None


class Stack:
    def __init__(self):
        self.topo = None
        self.size = 0

    def push(self, valor):
        """Insere elemento na pilha"""
        novo = No()
        novo.valor = valor
        novo.prox = self.topo
        self.topo = novo
        self.size += 1

    def pop(self):
        """Remove o valor do topo da pilha"""
        if self.size > 0:
            no = self.topo
            self.topo = self.topo.prox
            self.size -= 1
            return no.valor
        raise IndexError("A pilha está vazia")

    def peek(self):
        """Retorna o valor do topo da pilha"""
        if self.size > 0:
            no = self.topo.valor
            return no
        raise IndexError("A pilha está vazia")


pilha = Stack()
pilha.push(20)
pilha.push(30)
pilha.push(40)
print(pilha.size)
print(pilha.peek())
print(pilha.pop())
print(pilha.peek())
