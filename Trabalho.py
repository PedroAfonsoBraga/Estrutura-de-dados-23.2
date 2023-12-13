class NoListaEncadeada:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None


class FilaListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, dado):
        novo_no = NoListaEncadeada(dado)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.prox = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        dado = self.inicio.dado
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None
        return dado


class PilhaListaEncadeada:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def push(self, dado):
        novo_no = NoListaEncadeada(dado)
        novo_no.prox = self.topo
        self.topo = novo_no

    def pop(self):
        if self.esta_vazia():
            return None
        dado = self.topo.dado
        self.topo = self.topo.prox
        return dado


class No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, raiz, chave):
        if raiz is None:
            return No(chave)
        if chave < raiz.chave:
            raiz.esq = self._inserir(raiz.esq, chave)
        elif chave > raiz.chave:
            raiz.dir = self._inserir(raiz.dir, chave)
        return raiz

    def excluir(self, chave):
        self.raiz = self._excluir(self.raiz, chave)

    def _excluir(self, raiz, chave):
        if raiz is None:
            return raiz

        if chave < raiz.chave:
            raiz.esq = self._excluir(raiz.esq, chave)
        elif chave > raiz.chave:
            raiz.dir = self._excluir(raiz.dir, chave)
        else:
            if raiz.esq is None:
                return raiz.dir
            elif raiz.dir is None:
                return raiz.esq

            raiz.chave = self._menor_valor(raiz.dir)
            raiz.dir = self._excluir(raiz.dir, raiz.chave)

        return raiz

    def _menor_valor(self, raiz):
        atual = raiz
        while atual.esq is not None:
            atual = atual.esq
        return atual.chave

    def busca(self, chave):
        return self._busca(self.raiz, chave)

    def _busca(self, raiz, chave):
        if raiz is None or raiz.chave == chave:
            return raiz
        if chave < raiz.chave:
            return self._busca(raiz.esq, chave)
        return self._busca(raiz.dir, chave)

    def preordem_iterativo(self):
        resultado = []
        stack = PilhaListaEncadeada()
        if self.raiz:
            stack.push(self.raiz)

        while not stack.esta_vazia():
            atual = stack.pop()
            resultado.append(atual.chave)

            if atual.dir:
                stack.push(atual.dir)
            if atual.esq:
                stack.push(atual.esq)

        return resultado

    def percurso_nivel(self):
        nivel_resultado = []
        queue = FilaListaEncadeada()
        if self.raiz:
            queue.enfileirar(self.raiz)

        while not queue.esta_vazia():
            atual = queue.desenfileirar()
            nivel_resultado.append(atual.chave)

            if atual.esq:
                queue.enfileirar(atual.esq)
            if atual.dir:
                queue.enfileirar(atual.dir)

        return nivel_resultado


arvore = ArvoreBinaria()
opcao = 0
while opcao != 6:
    print("1 - Inserir")
    print("2 - Excluir")
    print("3 - Buscar")
    print("4 - Mostrar arvore (Pre-ordem)")
    print("5 - Mostrar arvore (Percurso em nivel)")
    print("6 - Sair")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        valor = int(input("Digite o valor a ser inserido: "))
        arvore.inserir(valor)
    elif opcao == 2:
        valor = int(input("Digite o valor a ser excluído: "))
        arvore.excluir(valor)
    elif opcao == 3:
        valor = int(input("Digite o valor a ser buscado: "))
        if arvore.busca(valor) is not None:
            print("Valor encontrado")
        else:
            print("Valor não encontrado")
    elif opcao == 4:
        print(arvore.preordem_iterativo())
    elif opcao == 5:
        print(arvore.percurso_nivel())
    elif opcao == 6:
        print("Saindo...")
    else:
        print("Opção inválida")
