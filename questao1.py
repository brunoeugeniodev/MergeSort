def merge_sort_decrescente(v, inicio, fim):
    if inicio >= fim:
        return

    meio = (inicio + fim) // 2
    merge_sort_decrescente(v, inicio, meio)
    merge_sort_decrescente(v, meio + 1, fim)
    intercalar_decrescente(v, inicio, meio, fim)

def intercalar_decrescente(v, inicio, meio, fim):
    esquerda = v[inicio:meio + 1]
    direita = v[meio + 1:fim + 1]

    i = j = 0
    k = inicio

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] >= direita[j]:  # Comparação invertida
            v[k] = esquerda[i]
            i += 1
        else:
            v[k] = direita[j]
            j += 1
        k += 1

    while i < len(esquerda):
        v[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        v[k] = direita[j]
        j += 1
        k += 1

# Exemplo de uso
v = [38, 27, 43, 3, 9, 82, 10]
merge_sort_decrescente(v, 0, len(v) - 1)
print("Vetor ordenado de forma decrescente:", v)
