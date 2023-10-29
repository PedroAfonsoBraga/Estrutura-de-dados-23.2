# Elabore algoritmos para inclusão (empilhar) e exclusão (desempilhar) que permita implementar 
# 2 pilhas em um único vetor. Os algoritmos devem solicitar a identificação de qual pilha (1 ou 2), e fazer a
# operação solicitada. Qual a complexidade destes algoritmos?

tamanho_vetor = 10
topo_pilha1 = -1
topo_pilha2 = tamanho_vetor

def empilhar(pilha, elemento):
    global topo_pilha1, topo_pilha2
    if pilha == 1: 
        if topo_pilha1 < topo_pilha2 - 1:
            topo_pilha1 += 1
            vetor[topo_pilha1] = elemento
        else:
            print("Pilha 1 cheia!")
    else:
        if topo_pilha2 - 1 > topo_pilha1:
            topo_pilha2 -= 1
            vetor[topo_pilha2] = elemento
        else:
            print("Pilha 2 cheia!")

def desempilhar(pilha):
    global topo_pilha1, topo_pilha2
    if pilha == 1:
        if topo_pilha1 >= 0:
            topo_pilha1 -= 1
            return vetor[topo_pilha1 + 1]
        else:
            print("Pilha 1 vazia!")
            return None
    else:
        if topo_pilha2 < tamanho_vetor:
            topo_pilha2 += 1
            return vetor[topo_pilha2 - 1]
        else:
            print("Pilha 2 vazia!")
            return None

vetor = [None] * tamanho_vetor

empilhar(1, 10)
empilhar(1, 20)
empilhar(2, 30)
empilhar(2, 40)

print(desempilhar(1))
print(desempilhar(2))
