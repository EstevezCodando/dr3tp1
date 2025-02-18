# MinHeap: Remoção do Elemento Raiz

## Processo de Remoção em MinHeap
A remoção do elemento raiz em uma **MinHeap** segue os seguintes passos:

1. **Substituir a raiz pelo último elemento**
   - O primeiro elemento do heap (o menor) é removido e substituído pelo último elemento do array.
   
2. **Aplicar o heapify-down (ajuste descendente)**
   - O novo elemento na raiz é comparado com seus filhos.
   - Se for maior que algum dos filhos, troca-se com o menor deles para restaurar a propriedade da MinHeap.
   - O processo continua até que o elemento esteja corretamente posicionado.

## Implementação em Python

```python
class MinHeap:
    def __init__(self):
        """Inicializa a MinHeap como uma lista vazia."""
        self.heap = []

    def _pai(self, i):
        return (i - 1) // 2

    def _esquerda(self, i):
        return 2 * i + 1

    def _direita(self, i):
        return 2 * i + 2

    def _descer(self, i):
        """Reorganiza o heap descendo um elemento para manter a propriedade da MinHeap."""
        menor = i
        esquerda = self._esquerda(i)
        direita = self._direita(i)

        if esquerda < len(self.heap) and self.heap[esquerda] < self.heap[menor]:
            menor = esquerda

        if direita < len(self.heap) and self.heap[direita] < self.heap[menor]:
            menor = direita

        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self._descer(menor)

    def pop(self):
        """Remove e retorna o menor elemento da MinHeap."""
        if not self.heap:
            raise IndexError("Heap vazia")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)
        return raiz

    def inserir(self, valor):
        """Insere um novo valor na MinHeap e ajusta a estrutura."""
        self.heap.append(valor)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] < self.heap[self._pai(i)]:
            self.heap[i], self.heap[self._pai(i)] = self.heap[self._pai(i)], self.heap[i]
            i = self._pai(i)

    def __str__(self):
        return str(self.heap)

# Exemplo de uso:
heap = MinHeap()
heap.inserir(10)
heap.inserir(20)
heap.inserir(5)
heap.inserir(30)
heap.inserir(15)
print("MinHeap antes da remoção:", heap)
print("Elemento removido:", heap.pop())
print("MinHeap após a remoção:", heap)
```

## Cálculo dos Índices na Heap

Em uma **implementação de Heap usando um array**, os índices dos nós podem ser calculados da seguinte forma:

1. **Índice do pai de um nó no índice `i`**:
   ```python
   pai = (i - 1) // 2
   ```
   - O nó pai está localizado no índice `(i - 1) // 2`.

2. **Índice do filho esquerdo de um nó no índice `i`**:
   ```python
   filho_esquerdo = 2 * i + 1
   ```
   - O filho esquerdo está no índice `2 * i + 1`.

3. **Índice do filho direito de um nó no índice `i`**:
   ```python
   filho_direito = 2 * i + 2
   ```
   - O filho direito está no índice `2 * i + 2`.

Essas fórmulas são essenciais para manipular eficientemente heaps armazenadas em arrays.

## Justificativa
A remoção da raiz na MinHeap é eficiente e mantém a propriedade da heap:
1. **A troca da raiz pelo último elemento** mantém a estrutura de árvore binária completa.
2. **O ajuste descendente (`heapify-down`) reordena os elementos** em **O(log n)**, garantindo que a menor chave continue na raiz.
3. **O tempo de remoção é O(log n)**, tornando essa abordagem eficiente para filas de prioridade e ordenações rápidas.

