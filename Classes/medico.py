from pessoa import Pessoa
from consultas import Consultas
from receita import Receita
from paciente import Paciente


class Medico(Pessoa):
    def __init__(self, CRM, especialidade, nome, CPF, data_nascimento, genero, endereco):
        super().__init__(nome, CPF, data_nascimento, genero, endereco)
        self.CRM = CRM
        self.especialidade = especialidade
        self.receita = []
        self.atualizaPront = []
        self.anotacao = []
        self.solicitExam = []

    def prescreverReceitas(self, prescricao, consulta):
        prescricao = Receita.adicionarReceita()
        consulta = Consultas(consulta)
        self.receita.append(prescricao)
        self.receita.append(consulta)

    def atualizarProntuario(self, nome, genero, data_nascimento, consultas, data_hora, prontuario):
        paciente = Paciente(nome, genero, data_nascimento)
        consult = Consultas(consultas, data_hora, prontuario)
        self.atualizaPront.append(paciente)
        self.atualizaPront.append(consult)

    def fazerAnotacao(self, nome, genero, consultas, data_hora, data_nascimento):
        paciente = Paciente(nome, genero, data_nascimento)
        consult = Consultas(consultas, data_hora)
        self.anotacao.append(paciente)
        self.anotacao.append(consult)

    def solicitarExame(self, nome, data_nascimento, consultas, data_hora):
        paciente = Paciente(nome, data_nascimento)
        consult = Consultas(consultas, data_hora)
        self.solicitExam = []
        self.solicitExam.append(paciente)
        self.solicitExam.append(consult)

    def alterarEspecialidade(self, especialidade):
        self.especialidade = especialidade
