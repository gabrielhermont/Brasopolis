class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 2000 #DETERMINEI ESSE SALDO INICIAL ALEATORIAMENTE
        self.posicao = 0
        self.propriedades = []
        self.preso = False
    
    def pagar (self, valor):
        self.saldo -= valor
        print(f'O jogador {self.nome} pagou {valor}. Saldo atual {self.saldo}')

    def receber (self, valor):
        self.saldo += valor
        print(f"O jogador {self.nome} recebeu {valor}. Saldo atual: {self.saldo}")

    #PRECISA FAZER A FUNÇÃO DE SE MOVER NO TABULEIRO PORÉM TENTEI FAZER E NÃO CONSEGUI!