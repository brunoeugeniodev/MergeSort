import random

def merge_sort(v):
    if len(v) <= 1:
        return v
    
    meio = len(v) // 2
    esquerda = merge_sort(v[:meio])
    direita = merge_sort(v[meio:])
    
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
    return [random.randint(1, 1000) for _ in range(tamanho)]

def testar_merge_sort():
    tamanhos = [10, 100, 1000]
    
    for tamanho in tamanhos:
        vetor = gerar_vetor(tamanho)
        vetor_ordenado = merge_sort(vetor)
        
        # Verificar se o vetor está ordenado corretamente
        esta_ordenado = all(vetor_ordenado[i] <= vetor_ordenado[i + 1] for i in range(len(vetor_ordenado) - 1))
        
        print(f"Teste com {tamanho} elementos: {'Sucesso' if esta_ordenado else 'Falha'}")

# Executar os testes
testar_merge_sort()
