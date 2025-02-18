# Estruturas de Dados: Heap Binária e Trie

Este repositório contém implementações e explicações detalhadas sobre as estruturas de dados **Heap Binária** e **Trie**, cobrindo conceitos fundamentais, implementações práticas e aplicações reais.

## 📌 Conteúdo

1. [Motivação para usar Heap](#1-motivação-para-usar-heap)
2. [Implementação da MinHeap](#2-implementação-da-minheap)
3. [Implementação da MaxHeap](#3-implementação-da-maxheap)
4. [Remoção na MinHeap](#4-remocao-na-minheap)
5. [Heaps e Arrays](#5-heaps-e-arrays)
6. [Aplicação de Heap em Fila de Prioridade](#6-aplicação-de-heap-em-fila-de-prioridade)
7. [Implementação de Trie](#7-implementação-de-trie)
8. [Operações e Visualização da Trie](#8-operações-e-visualização-da-trie)

---

## 1️⃣ Motivação para usar Heap

A **Heap Binária** é uma estrutura de dados eficiente para manipulação de **mínimos** ou **máximos** em tempo **O(1)**, sendo amplamente utilizada para:

- **Filas de prioridade** (ex: sistemas de agendamento de processos).
- **Algoritmos de grafos** (ex: Dijkstra e Prim).
- **Ordenação eficiente** (ex: Heapsort).
- **Gerenciamento de memória** (ex: coleta de lixo em linguagens como Java e Python).

🔗 Explicação completa no arquivo [Ex1_Heap.md](Ex1_Heap.md).

---

## 2️⃣ Implementação da MinHeap

A **MinHeap** é uma estrutura onde o menor elemento sempre fica na raiz. Implementamos uma **MinHeap do zero**, sem bibliotecas auxiliares, garantindo que os elementos sejam organizados corretamente após inserções e remoções.

📂 Código: [Ex2_MinHeap.py](Ex2_MinHeap.py)

---

## 3️⃣ Implementação da MaxHeap

Dado um array inicial `[50, 30, 40, 10, 20, 35]`, ao inserir **45**, a estrutura **MaxHeap** é reorganizada.

🔹 **Explicação:** O novo elemento **45** é inserido no final e sobe até encontrar sua posição correta, mantendo a propriedade de MaxHeap.

📂 Código: [Ex3_MaxHeap.py](Ex3_MaxHeap.py)
🔗 Explicação completa no arquivo [Ex3_MaxHeap.md](Ex3_MaxHeap.md).

---

## 4️⃣ Remoção na MinHeap

A remoção da raiz de uma **MinHeap** envolve substituir o elemento da raiz pelo último nó, reestruturar a árvore e garantir que a propriedade de heap seja mantida.

🔹 **Explicação detalhada + código**: [Ex4_MinHeap_remove.py](Ex4_MinHeap_remove.py)

---

## 5️⃣ Heaps e Arrays

Em uma **Heap implementada como array**, os índices seguem a seguinte relação:

- **Pai do nó `i`**: `(i - 1) // 2`
- **Filho esquerdo do nó `i`**: `2 * i + 1`
- **Filho direito do nó `i`**: `2 * i + 2`

📂 Explicação completa: [Ex5_HeapArray.md](Ex5_HeapArray.md)

---

## 6️⃣ Aplicação de Heap em Fila de Prioridade

Implementamos um **sistema de agendamento de tarefas** utilizando uma **MinHeap**, onde as tarefas são organizadas conforme suas prioridades.

📂 Explicação completa: [Ex6_HeapReal.md](Ex6_HeapReal.md)

---

## 7️⃣ Implementação de Trie

A **Trie** é uma árvore eficiente para armazenar e buscar palavras. Nossa implementação inclui:

- **inserir(palavra)** → Adiciona uma palavra na Trie.
- **buscar(palavra)** → Retorna `True` se a palavra existir na Trie.
- **iniciar_com(prefixo)** → Verifica se existe alguma palavra com o prefixo informado.

📂 Código: [Ex7_Trie.py](Ex7_Trie.py)
📂 Explicação completa: [Ex7_Trie.md](Ex7_Trie.md)

---

## 8️⃣ Operações e Visualização da Trie

Inserimos as palavras **"casa", "carro", "caminhão", "cachorro" e "cadeira"** na **Trie**, e geramos uma representação gráfica da estrutura.

📂 Código + Visualização: [Ex8_TrieGraph.py](Ex8_TrieGraph.py)

📷 **Exemplo da estrutura gerada**:
``` bash
Estrutura da Trie:
└── c
    ├── a
    │   ├── s
    │   │   └── a (*)
    │   └── r
    │       └── r
    │           └── o (*)
    ├── a
    │   ├── m
    │   │   └── i
    │   │       └── n
    │   │           └── h
    │   │               └── ã
    │   │                   └── o (*)
    │   └── c
    │       └── h
    │           └── o
    │               └── r
    │                   └── r
    │                       └── o (*)
    └── d
        └── e
            └── i
                └── r
                    └── a (*)
 ```