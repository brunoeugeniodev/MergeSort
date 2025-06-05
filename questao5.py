import random
import time

def merge_sort_iterativo(v):
    tamanho = len(v)
    bloco = 1
    
    while bloco < tamanho:
        for inicio in range(0, tamanho, 2 * bloco):
            meio = min(inicio + bloco, tamanho)
            fim = min(inicio + 2 * bloco, tamanho)
            v[inicio:fim] = intercalar(v[inicio:meio], v[meio:fim])
        bloco *= 2
    
    return v

def merge_sort_recursivo(v):
    if len(v) <= 1:
        return v
    
    meio = len(v) // 2
    esquerda = merge_sort_recursivo(v[:meio])
    direita = merge_sort_recursivo(v[meio:])
    
    return intercalar(esquerda, direita)

def intercalar(esquerda, direita):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

def gerar_vetor(tamanho):
    return [random.randint(1, 10000) for _ in range(tamanho)]

def testar_algoritmos():
    tamanhos = [10, 100, 1000, 10000]
    resultados = []

    for tamanho in tamanhos:
        vetor = gerar_vetor(tamanho)

        # Teste Recursivo
        v_recursivo = vetor[:]
        inicio_recursivo = time.time()
        merge_sort_recursivo(v_recursivo)
        tempo_recursivo = time.time() - inicio_recursivo

        # Teste Iterativo
        v_iterativo = vetor[:]
        inicio_iterativo = time.time()
        merge_sort_iterativo(v_iterativo)
        tempo_iterativo = time.time() - inicio_iterativo

        resultados.append((tamanho, tempo_recursivo, tempo_iterativo))

    return resultados

# Executar testes e exibir tabela
dados = testar_algoritmos()
print("\nComparação de Tempo de Execução:")
print(f"{'Tamanho do Vetor':<20} {'Recursivo (s)':<15} {'Iterativo (s)':<15}")
for tamanho, tempo_r, tempo_i in dados:
    print(f"{tamanho:<20} {tempo_r:<15.6f} {tempo_i:<15.6f}")
