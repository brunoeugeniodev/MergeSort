class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def merge_sort_lista(head):
    if head is None or head.proximo is None:
        return head

    meio = encontrar_meio(head)
    direita = meio.proximo
    meio.proximo = None

    esquerda_ordenada = merge_sort_lista(head)
    direita_ordenada = merge_sort_lista(direita)

    return intercalar_listas(esquerda_ordenada, direita_ordenada)

def encontrar_meio(head):
    if head is None:
        return head
    
    lento = head
    rapido = head

    while rapido.proximo and rapido.proximo.proximo:
        lento = lento.proximo
        rapido = rapido.proximo.proximo
    
    return lento

def intercalar_listas(esquerda, direita):
    if not esquerda:
        return direita
    if not direita:
        return esquerda

    if esquerda.valor <= direita.valor:
        resultado = esquerda
        resultado.proximo = intercalar_listas(esquerda.proximo, direita)
    else:
        resultado = direita
        resultado.proximo = intercalar_listas(esquerda, direita.proximo)
    
    return resultado

# Função para imprimir a lista
def imprimir_lista(head):
    atual = head
    while atual:
        print(atual.valor, end=" -> ")
        atual = atual.proximo
    print("None")

# Criando uma lista encadeada de exemplo
valores = [38, 27, 43, 3, 9, 82, 10]
head = No(valores[0])
atual = head
for valor in valores[1:]:
    atual.proximo = No(valor)
    atual = atual.proximo

print("Lista original:")
imprimir_lista(head)

# Ordenando a lista encadeada
head_ordenado = merge_sort_lista(head)

print("Lista ordenada:")
imprimir_lista(head_ordenado)
