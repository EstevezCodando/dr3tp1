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
heap.inserir((1, "Tarefa A"))
heap.inserir((3, "Tarefa C"))
heap.inserir((2, "Tarefa B"))
heap.inserir((4, "Tarefa D"))
print("Fila de Prioridade (MinHeap) antes da remoção:", heap)
print("Tarefa com maior prioridade removida:", heap.pop())
print("Fila de Prioridade após a remoção:", heap)
```

## Aplicação de Heap em Fila de Prioridade

Uma **Heap** pode ser utilizada para implementar uma **Fila de Prioridade** onde elementos com menor valor de prioridade são atendidos primeiro. Isso é útil em sistemas de agendamento de tarefas, gerenciamento de processos e algoritmos como o **Dijkstra** para encontrar caminhos mínimos.

## Justificativa
O uso da MinHeap em uma fila de prioridade permite:
1. **Inserção eficiente** em **O(log n)**.
2. **Remoção rápida do elemento de maior prioridade** em **O(log n)**.
3. **Estrutura dinâmica** que mantém a ordem dos elementos automaticamente.

Essa abordagem é amplamente utilizada em sistemas de computação e inteligência artificial para processamento de tarefas com prioridade.

---

# Implementação de Trie

## Explicação
Uma **Trie** é uma estrutura de dados eficiente para armazenar e buscar palavras, permitindo pesquisas rápidas e armazenamento compacto. Ela é amplamente usada em **autocompletar, dicionários e compressão de texto**.

Cada nó da Trie contém:
1. **Filhos**: Referências para os caracteres seguintes.
2. **Flag de palavra**: Indica se um nó marca o fim de uma palavra.

## Implementação em Python

```python
class TrieNode:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def inserir(self, palavra):
        """Insere uma palavra na Trie."""
        nodo = self.raiz
        for char in palavra:
            if char not in nodo.filhos:
                nodo.filhos[char] = TrieNode()
            nodo = nodo.filhos[char]
        nodo.fim_palavra = True

    def buscar(self, palavra):
        """Busca uma palavra na Trie e retorna True se encontrada."""
        nodo = self.raiz
        for char in palavra:
            if char not in nodo.filhos:
                return False
            nodo = nodo.filhos[char]
        return nodo.fim_palavra

# Exemplo de uso:
trie = Trie()
trie.inserir("casa")
trie.inserir("carro")
print("Palavra 'casa' está na Trie?", trie.buscar("casa"))  # True
print("Palavra 'caminho' está na Trie?", trie.buscar("caminho"))  # False
```

## Justificativa
A Trie permite:
- **Inserção e busca rápidas** em **O(m)**, onde `m` é o tamanho da palavra.
- **Eficiência no armazenamento** de prefixos compartilhados.
- **Aplicação em sistemas de busca e autocompletar**.

