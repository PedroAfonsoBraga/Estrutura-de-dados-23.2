# Uma deque é uma lista na qual inclusões e exclusões podem ser efetuadas em qualquer das duas extremidades. 
# Elabore um algoritmo de inclusão para uma deque que deve obter o valor a ser inserido e a indicação da extremidade 
# (esquerda ou direita) na qual a inclusão irá ocorrer, considerando a deque alocada sequencialmente 
# (em vetor) e implementada como uma lista circular.

tamanho_deque = 10
deque = [None] * tamanho_deque
frente = -1
fim = -1

def incluir(valor, extremidade):
    global frente, fim

    if frente == -1: # deque vazia
        frente = 0
        fim = 0
    elif frente == (fim+1) % tamanho_deque: # deque cheia
        print("Deque cheia!")
        return
    
    if extremidade == "esquerda":
        frente = (frente-1) % tamanho_deque
        deque[frente] = valor
    elif extremidade == "direita":
        fim = (fim+1) % tamanho_deque
        deque[fim] = valor
    else:
        print("Extremidade inválida!")
        return

incluir(1, "esquerda")
incluir(20, 'direita')
incluir(30, 'esquerda')

print(deque)