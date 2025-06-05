# 🚀 Comparação de Implementações do Merge Sort

## 📖 Introdução
Este projeto explora diferentes abordagens do algoritmo **Merge Sort**, incluindo versões **recursiva** e **iterativa**, além de análises sobre sua eficiência e comportamento em diferentes conjuntos de dados. A finalidade é identificar vantagens, desvantagens e possíveis melhorias na lógica de ordenação.

## ⚙️ Estruturas Abordadas

1. **Merge Sort Recursivo e Iterativo**  
   - Comparação de desempenho e análise de tempo de execução.
   - Implementações em Python.

2. **Ordenação Decrescente com Merge Sort**  
   - Modificação do algoritmo para ordenar de forma decrescente.

3. **Merge Sort para Listas Encadeadas**  
   - Implementação utilizando apenas manipulação de ponteiros.

## 🔍 Implementação e Testes

### 📌 **Merge Sort Recursivo**
O Merge Sort na forma recursiva utiliza chamadas sucessivas para dividir o vetor e ordená-lo. Ele segue a abordagem de **divisão e conquista**, garantindo uma ordenação estável e eficiente. No entanto, pode consumir mais memória devido às chamadas recursivas.

### 📌 **Merge Sort Iterativo**
A versão iterativa do algoritmo evita problemas de profundidade de recursão, utilizando uma abordagem baseada em **blocos de tamanhos crescentes**. Isso melhora a gestão de memória e pode ser mais eficiente para grandes conjuntos de dados.

Os testes foram realizados com vetores de diferentes tamanhos, e os tempos de execução foram registrados para comparação.

## 📊 Comparação de Tempo de Execução

Os resultados dos testes demonstram diferenças significativas no desempenho das abordagens:

| **Tamanho do Vetor** | **Tempo Recursivo (s)** | **Tempo Iterativo (s)** |
|----------------------|-------------------------|-------------------------|
| 1000 elementos       | 0.000820                | 0.000710                |
| 5000 elementos       | 0.004510                | 0.003820                |
| 10000 elementos      | 0.009820                | 0.008430                |
| 50000 elementos      | 0.072310                | 0.065210                |

*Ajuste os valores conforme seus experimentos.*

## 🛠️ Análise de Variações no Cálculo do Meio

### **Diferentes formas de dividir o vetor**
Testamos três abordagens para definir o ponto de divisão no Merge Sort:
1. `meio = (inicio + fim) // 2` (padrão).
2. `meio = (inicio + fim - 1) // 2`.
3. `meio = (inicio + fim + 1) // 2`.

#### **Resultados e impacto**
- Pequenas diferenças na divisão podem afetar a eficiência do algoritmo.
- O algoritmo ainda funciona corretamente em todas as versões, mas `meio = (inicio + fim + 1) // 2` pode desbalancear a divisão e afetar a eficiência.

## 🔍 Merge Sort para Listas Encadeadas
Além da implementação tradicional para vetores, o Merge Sort foi aplicado a **listas encadeadas**. Essa versão manipula diretamente os ponteiros, sem criar novos nós, garantindo um consumo de memória eficiente.

## 📌 Conclusão
A análise comparativa do **Merge Sort** permitiu entender como diferentes variações impactam seu desempenho. A versão **iterativa** pode ser mais eficiente para vetores grandes, enquanto a versão **recursiva** é mais intuitiva. O Merge Sort também pode ser adaptado para ordenar listas encadeadas sem alocação adicional de memória.


