class Cidade:
    def __init__(self,nome,linha,coluna):
        self.nome = nome
        self.linha = linha
        self.coluna = coluna

    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return self.nome