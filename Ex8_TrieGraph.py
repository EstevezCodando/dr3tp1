class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.eh_palavra_final = False


class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra: str) -> None:
        """        
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
        :param prefixo: Prefixo a ser buscado.
        :return: True se existir alguma palavra com esse prefixo, False caso contrário.
        """
        no_atual = self.raiz

        for caractere in prefixo:
            if caractere not in no_atual.filhos:
                return False
            no_atual = no_atual.filhos[caractere]

        return True

    def imprimir_trie(self, no=None, prefixo="", ultimo=True):
        """        
        :param no: Nó atual (usado na recursão).
        :param prefixo: Prefixo para indentação (usado na recursão).
        :param ultimo: Indica se o nó é o último filho (usado na formatação).
        """
        if no is None:
            no = self.raiz

        # Imprime o nó atual
        print(prefixo, end="")
        if ultimo:
            print("└── ", end="")
            novo_prefixo = prefixo + "    "
        else:
            print("├── ", end="")
            novo_prefixo = prefixo + "│   "

        # Imprime os filhos do nó atual
        filhos = list(no.filhos.items())
        for i, (caractere, filho) in enumerate(filhos):
            print(caractere, end="")
            if filho.eh_palavra_final:
                print(" (*)", end="")  # Marca palavras completas
            print()
            self.imprimir_trie(filho, novo_prefixo, i == len(filhos) - 1)


# Exemplo de uso
trie = Trie()
palavras = ["casa", "carro", "caminhão", "cachorro", "cadeira"]
for palavra in palavras:
    trie.inserir(palavra)

print("Estrutura da Trie:")
trie.imprimir_trie()