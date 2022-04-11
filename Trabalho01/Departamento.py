#Matheus Roberto Barcellos Ferraz

class Departamento:
    def __init__(self, nomedepartamento, chefia):
        self.nomedepartamento = nomedepartamento
        self.chefia = chefia

    def getNomedepartamento(self):
        return self.nomedepartamento

    def setNomedepartamento(self, nomedepartamento):
        self.nomedepartamento = nomedepartamento

    def setChefia(self, chefia):
        self.chefia = chefia

    def getChefia(self):
        return self.chefia
