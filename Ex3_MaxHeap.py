class MaxHeap:
    def __init__(self):
        """Inicializa a MaxHeap como uma lista vazia."""
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
        """Reorganiza o heap subindo um elemento para manter a propriedade da MaxHeap."""
        while i > 0 and self.heap[i] > self.heap[self._pai(i)]:
            self.heap[i], self.heap[self._pai(i)] = self.heap[self._pai(i)], self.heap[i]
            i = self._pai(i)

    def _descer(self, i):
        """Reorganiza o heap descendo um elemento para manter a propriedade da MaxHeap."""
        maior = i
        esquerda = self._esquerda(i)
        direita = self._direita(i)

        if esquerda < len(self.heap) and self.heap[esquerda] > self.heap[maior]:
            maior = esquerda

        if direita < len(self.heap) and self.heap[direita] > self.heap[maior]:
            maior = direita

        if maior != i:
            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            self._descer(maior)

    def inserir(self, valor):
        """Insere um novo valor na MaxHeap e ajusta a estrutura."""
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def remover_max(self):
        """Remove e retorna o maior elemento da MaxHeap."""
        if not self.heap:
            raise IndexError("Heap vazia")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)
        return raiz

    def get_max(self):
        """Retorna o maior elemento sem removê-lo."""
        if not self.heap:
            raise IndexError("Heap vazia")
        return self.heap[0]

    def tamanho(self):
        """Retorna o tamanho da MaxHeap."""
        return len(self.heap)

    def __str__(self):
        """Representação textual da MaxHeap."""
        return str(self.heap)

# Exemplo de uso:
heap = MaxHeap()

# Criando a heap inicial com os valores fornecidos
valores_iniciais = [50, 30, 40, 10, 20, 35]
for v in valores_iniciais:
    heap.inserir(v)

print("Heap inicial:", heap)  # [50, 30, 40, 10, 20, 35]

# Inserindo o elemento 45
heap.inserir(45)

print("Heap após inserção de 45:", heap)  # [50, 30, 45, 10, 20, 35, 40]
