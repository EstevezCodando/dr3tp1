class MinHeap:
    def __init__(self):
        """Inicializa a MinHeap como uma lista vazia."""
        self.heap = []

    def _pai(self, i):
        """Retorna o índice do nó pai."""
        return (i - 1) // 2

    def _esquerda(self, i):
        """Retorna o índice do filho esquerdo."""
        return 2 * i + 1

    def _direita(self, i):
        """Retorna o índice do filho direito."""
        return 2 * i + 2

    def _subir(self, i):
        """Reorganiza o heap subindo um elemento para manter a propriedade da MinHeap."""
        while i > 0 and self.heap[i] < self.heap[self._pai(i)]:
            self.heap[i], self.heap[self._pai(i)] = self.heap[self._pai(i)], self.heap[i]
            i = self._pai(i)

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

    def inserir(self, valor):
        """Insere um novo valor na MinHeap e ajusta a estrutura."""
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def remover_min(self):
        """Remove e retorna o menor elemento da MinHeap."""
        if not self.heap:
            raise IndexError("Heap vazia")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)
        return raiz

    def get_min(self):
        """Retorna o menor elemento sem removê-lo."""
        if not self.heap:
            raise IndexError("Heap vazia")
        return self.heap[0]

    def tamanho(self):
        """Retorna o tamanho da MinHeap."""
        return len(self.heap)

    def __str__(self):
        """Representação textual da MinHeap."""
        return str(self.heap)

# Exemplo de uso:
heap = MinHeap()
heap.inserir(10)
heap.inserir(5)
heap.inserir(20)
heap.inserir(2)

print(heap)  # [2, 5, 20, 10]
print(heap.remover_min())  # 2
print(heap)  # [5, 10, 20]
