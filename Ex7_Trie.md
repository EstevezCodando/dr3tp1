# Implementação de Trie em Python

## Introdução

A **Trie**, é uma estrutura de dados eficiente para armazenamento e busca de strings. É amplamente utilizada em aplicações como **dicionários, corretores ortográficos, compressão de texto** e **sugestões de pesquisa**.

## Estrutura da Trie

A Trie é composta por nós, onde:
- Cada nó representa um caractere.
- Cada nó possui um conjunto de filhos (outros nós).
- Um nó pode indicar se representa o final de uma palavra.

### Operações implementadas

1. **Inserção (`inserir`)**  
   - Percorre os caracteres da palavra e adiciona nós conforme necessário.  
   - Marca o último nó como final de palavra.

2. **Busca (`buscar`)**  
   - Percorre os caracteres da palavra.  
   - Retorna `True` se a palavra existir na Trie, `False` caso contrário.

3. **Verificação de prefixo (`iniciar_com`)**  
   - Confere se existe alguma palavra que começa com um determinado prefixo.  
   - Útil para sistemas de sugestão de palavras.
   
## Complexidade das Operações

- **Inserção**: O(n)  
- **Busca**: O(n)  
- **Verificação de prefixo**: O(n)  

Onde **n** é o tamanho da string processada.

## Aplicações

- **Sugestões de pesquisa** (ex: autocomplete do Google).  
- **Dicionários de palavras** (ex: verificação ortográfica).  
- **Compressão de dados** (ex: algoritmos de Huffman).  
- **Índices de busca rápida** em sistemas de informação.  

## Conclusão

A Trie é uma estrutura eficiente para operações com strings, oferecendo tempo linear para inserção e busca. Sua aplicação é fundamental em cenários onde prefixos e busca rápida são essenciais.
