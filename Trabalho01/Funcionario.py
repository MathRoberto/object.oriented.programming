#Matheus Roberto Barcellos Ferraz

class Funcionario:
    def __init__(self, nome, numero, trabalho, alocacao, coordenacao):
        self.nome = nome
        self.numero = numero
        self.trabalho = trabalho
        self.alocacao = alocacao
        self.coordenacao = coordenacao

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def getTrabalho(self):
        return self.trabalho

    def setTrabalho(self, trabalho):
        self.trabalho = trabalho

    def setAlocacao(self, alocacao):
        self.alocacao = alocacao

    def getAlocacao(self):
        return self.alocacao

    def getCoordenacao(self):
        return self.coordenacao

    def setCoordenacao(self, coordenacao):
        self.coordenacao = coordenacao