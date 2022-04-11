#Matheus Roberto Barcellos Ferraz

class Empresa:
    def __init__(self, nomeempresa, diretor):
        self.nomeempresa = nomeempresa
        self.diretor = diretor

    def getNomeempresa(self):
        return self.nomeempresa

    def setNomeempresa(self, nomeempresa):
        self.nomeempresa = nomeempresa

    def getDiretor(self):
        return self.diretor

    def setDiretor(self, diretor):
        self.diretor = diretor
