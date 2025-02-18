# Aplicação de Heap em um Cenário Real

## Implementação de uma Fila de Prioridade com Heap

### Conceito de Heap e Fila de Prioridade

Uma **Heap** é uma estrutura de dados em forma de árvore binária que satisfaz a propriedade da heap:
- Em uma **MinHeap**, cada nó pai tem um valor menor ou igual ao de seus filhos.
- Em uma **MaxHeap**, cada nó pai tem um valor maior ou igual ao de seus filhos.

Uma **Fila de Prioridade** é uma estrutura de dados que permite que elementos sejam retirados com base em sua prioridade, em vez de seguir a ordem de chegada. Isso é útil em situações como escalonamento de processos, gerenciamento de tarefas e algoritmos de otimização.

Usar uma Heap para implementar uma Fila de Prioridade tem as seguintes vantagens:
- **Inserção eficiente**: O tempo de inserção é **O(log n)**.
- **Remoção eficiente**: A remoção do elemento de maior prioridade também é **O(log n)**.
- **Acesso rápido ao elemento de maior prioridade**: O elemento de maior prioridade (raiz da heap) pode ser acessado em **O(1)**.

## Implementação: Sistema de Agendamento de Tarefas

Abaixo, implementamos um sistema de agendamento de tarefas utilizando uma **MinHeap**, onde as tarefas de menor prioridade numérica (maior urgência) são executadas primeiro.

```python
import heapq

class FilaDePrioridade:
    def __init__(self):
        self.heap = []

    def adicionar_tarefa(self, prioridade, descricao):
        """Adiciona uma tarefa à fila de prioridade."""
        heapq.heappush(self.heap, (prioridade, descricao))

    def executar_tarefa(self):
        """Remove e retorna a tarefa de maior prioridade (menor valor de prioridade)."""
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def visualizar_tarefas(self):
        """Retorna a lista de tarefas ordenadas por prioridade."""
        return sorted(self.heap)

# Exemplo de uso
if __name__ == "__main__":
    fila = FilaDePrioridade()
    fila.adicionar_tarefa(3, "Revisar relatório")
    fila.adicionar_tarefa(1, "Corrigir bug crítico")
    fila.adicionar_tarefa(2, "Responder e-mails")

    print("Tarefas na fila:", fila.visualizar_tarefas())
    print("Executando tarefa:", fila.executar_tarefa())
    print("Tarefas restantes:", fila.visualizar_tarefas())
```

### Explicação do Código
1. **`heapq`**: Biblioteca embutida no Python que implementa uma MinHeap.
2. **Métodos**:
   - `adicionar_tarefa(prioridade, descricao)`: Adiciona uma nova tarefa na heap.
   - `executar_tarefa()`: Remove e retorna a tarefa com a maior prioridade.
   - `visualizar_tarefas()`: Retorna uma lista ordenada das tarefas.
3. **Ordem de Execução**:
   - Primeiro, adicionamos tarefas com diferentes prioridades.
   - Depois, a execução ocorre removendo a tarefa com menor valor de prioridade.

## Conclusão
A utilização de uma **MinHeap** para implementar uma **Fila de Prioridade** é eficiente e adequada para sistemas de agendamento de tarefas. Com tempo de inserção e remoção **O(log n)**, a abordagem é escalável e aplicável em diversos contextos, como escalonadores de processos, planejamento de execução de eventos e algoritmos de busca. Esta implementação mostra como podemos gerenciar tarefas de forma eficaz utilizando essa estrutura.

