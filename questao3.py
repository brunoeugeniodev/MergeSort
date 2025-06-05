# a) Houve diferença nos resultados? Na maioria dos casos, ambas as 
# variações devem produzir um vetor ordenado corretamente. 
# No entanto, dependendo do tamanho do vetor e da divisão dos índices, 
# uma pequena alteração na definição do "meio" pode impactar a divisão 
# exata dos subvetores.

# b) O algoritmo ainda funciona corretamente? Sim, ambas as variações 
# devem manter o funcionamento geral do Merge Sort, já que ele ainda divide
# o vetor corretamente e intercala os valores ordenados.

# c) Alguma das variações provoca falhas? Justifique. A variação 
# (inicio + fim + 1) // 2 pode, em alguns casos, levar a divisões
# desbalanceadas e resultar em chamadas recursivas desnecessárias. 
# Isso ocorre porque ela pode aumentar o índice meio de forma que um dos
# subvetores seja ligeiramente maior que o outro, podendo afetar a 
# eficiência do algoritmo. Enquanto isso, (inicio + fim - 1) // 2 tende
# a dividir melhor os casos pares, mas pode alterar a forma como os
# elementos são agrupados. No entanto, em geral, ambas ainda devem 
# funcionar corretamente.

def merge_sort_var1(v, inicio, fim):
    if inicio >= fim:
        return
    
    meio = (inicio + fim - 1) // 2  # Primeira variação
    merge_sort_var1(v, inicio, meio)
    merge_sort_var1(v, meio + 1, fim)
    intercalar(v, inicio, meio, fim)

def merge_sort_var2(v, inicio, fim):
    if inicio >= fim:
        return
    
    meio = (inicio + fim + 1) // 2  # Segunda variação
    merge_sort_var2(v, inicio, meio)
    merge_sort_var2(v, meio + 1, fim)
    intercalar(v, inicio, meio, fim)

def intercalar(v, inicio, meio, fim):
    esquerda = v[inicio:meio + 1]
    direita = v[meio + 1:fim + 1]

    i = j = 0
    k = inicio

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
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

# Teste experimental
vetor_teste = [38, 27, 43, 3, 9, 82, 10]

# Testando as variações
v1 = vetor_teste[:]
merge_sort_var1(v1, 0, len(v1) - 1)
print("Variação (inicio + fim - 1) / 2:", v1)

v2 = vetor_teste[:]
merge_sort_var2(v2, 0, len(v2) - 1)
print("Variação (inicio + fim + 1) / 2:", v2)
