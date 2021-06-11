from consultas import consultas


class Receita:
    def __init__(self, consultas):
        self.consultas = consultas
        self.receita = []

    def adicionarReceita(self, consultas, medico, data_hora):
        medicacao = str(input('Digite a receita: '))
        receita = Consultas(consultas, medico, data_hora)
        self.receita.append(receita)
        self.receita.append(medicacao)

    def acessarReceita(self, consultas, medico, data_hora):
        receita = Consultas(consultas, medico, data_hora)
        self.receita.append(receita)

    def modificarReceita(self, consultas, medico, data_hora):
        medicacao = str(input('Digite a receita: '))
        receita = Consultas(consultas, medico, data_hora)
        self.receita.append(receita)
        self.receita.append(medicacao)

    def removerReceita(self):
        del self.receita
