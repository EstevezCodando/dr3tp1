class NoTrie:
    """Representa um nó na estrutura de dados Trie."""
    
    def __init__(self):
        self.filhos = {}
        self.eh_palavra_final = False


class Trie:
    """Implementa uma Trie para armazenar um conjunto de palavras."""
    
    def __init__(self):
        self.raiz = NoTrie()
    
    def inserir(self, palavra: str) -> None:
        """
        Insere uma palavra na Trie.
        
        :param palavra: Palavra a ser adicionada à estrutura.
        """
        no_atual = self.raiz
        
        for caractere in palavra:
            if caractere not in no_atual.filhos:
                no_atual.filhos[caractere] = NoTrie()
            no_atual = no_atual.filhos[caractere]
        
        no_atual.eh_palavra_final = True

    def buscar(self, palavra: str) -> bool:
        """
        Busca uma palavra na Trie e retorna se ela existe ou não.
        
        :param palavra: Palavra a ser buscada.
        :return: True se a palavra existe na Trie, False caso contrário.
        """
        no_atual = self.raiz
        
        for caractere in palavra:
            if caractere not in no_atual.filhos:
                return False
            no_atual = no_atual.filhos[caractere]
        
        return no_atual.eh_palavra_final

    def iniciar_com(self, prefixo: str) -> bool:
        """
        Verifica se existe alguma palavra na Trie que começa com um determinado prefixo.
        
        :param prefixo: Prefixo a ser buscado.
        :return: True se existir alguma palavra com esse prefixo, False caso contrário.
        """
        no_atual = self.raiz
        
        for caractere in prefixo:
            if caractere not in no_atual.filhos:
                return False
            no_atual = no_atual.filhos[caractere]
        
        return True

# Exemplo de uso
if __name__ == "__main__":
    trie = Trie()
    trie.inserir("casa")
    trie.inserir("carro")
    trie.inserir("caminho")

    print(trie.buscar("casa"))       # True
    print(trie.buscar("casaco"))     # False
    print(trie.iniciar_com("ca"))    # True
    print(trie.iniciar_com("car"))   # True
    print(trie.iniciar_com("bat"))   # False
