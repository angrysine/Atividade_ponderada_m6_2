class pilha():
    def __init__(self):
        self.pilha = []
        self.tamanho = 0

    def empilhar(self, valor):
        self.pilha.append(valor)
        self.tamanho += 1

    def desempilhar(self):
        if not self.vazia():
            self.tamanho -= 1
            return self.pilha.pop(-1)
        else:
            return None

    def vazia(self):
        return self.tamanho == 0

    def topo(self):
        if not self.vazia():
            return self.pilha[-1]
        else:
            return None
        
    def __repr__(self):
        return str(self.pilha)
    
