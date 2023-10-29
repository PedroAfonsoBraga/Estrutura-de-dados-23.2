# considere uma lista de inteiros desordenada, armazenada em um vetor, com M posições. 
# Chamaremos de lista 1. esta lista deve ser lida sequencialmente. Se o numero lido for par, este deve ser inserido numa pilha, inicialmente vazia. 
# Se for impar, deve ser inserido em uma fila, também inicialmente vazia. A pilha e a fila devem ser alocadas sequencialmente em vetores diferentes.

lista1 = [1,2,3,4,5,6,7,8,9,10]
m = 9
pilha = []*m
topo = -1

fila = []*m
inicio = 0
fim = -1

def empilhar(topo, elemento):
    global pilha
    if(topo == m):
        print("Pilha cheia!")
    else:
        topo = topo + 1
        pilha[topo] = elemento
    return pilha

def enfileirar (inicio, elemento):
    global fila, fim
    if(fim == m):
        print("Fila cheia!")
    else:
        fim = fim + 1
        fila[fim] = elemento

    return fila

for i in range(0, m):
    if lista1[i] % 2 == 0:
        empilhar(topo, lista1[i])
    else:
        enfileirar(inicio, lista1[i])




