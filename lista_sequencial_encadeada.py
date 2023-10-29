# Considere uma lista não ordenada com alocação sequencial, em um vetor com 20 posições. 
# Apresente um algoritmo que faça a inversão da ordem dos valores desta lista, utilizando
# para tal uma pilha com alocação encadeada. Definir a complexidade deste algoritmo.

class NoPilha:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, valor):
        novo_no = NoPilha(valor)
        if self.topo is None:
            self.topo = novo_no
        else: 
            novo_no.proximo = self.topo
            self.topo = novo_no
    
    def desempilhar(self):
        if self.topo is None:
            print("Pilha vazia!")
            return None
        valor = self.topo.valor
        self.topo = self.topo.proximo
        return valor

def inverter_lista(lista):
    pilha = Pilha()
    for elemento in lista:
        pilha.empilhar(elemento)
    
    lista_invertida = []

    while True:
        elemento = pilha.desempilhar()
        if elemento is None:
            break
        lista_invertida.append(elemento)

    return lista_invertida

lista_original = [1, 2, 3, 4, 5]
lista_invertida = inverter_lista(lista_original)
print(lista_invertida)  # Saída: [5, 4, 3, 2, 1]