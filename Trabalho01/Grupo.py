#Matheus Roberto Barcellos Ferraz

class Grupo:
    def __init__(self, nome, presidente, sede):
        self.nome = nome
        self.presidente = presidente
        self.sede = sede


    def getPresidente(self):
        return self.presidente

    def setPresidente(self, presidente):
        self.presidente = presidente

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getSede(self):
        return self.sede

    def setSede(self, sede):
        self.sede = sede


