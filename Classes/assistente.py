from pessoa import Pessoa
from medico import Medico
from paciente import Paciente
from consultas import Consultas


class Assistente(Pessoa):
    def __init__(self, agenda, nome, CPF, data_nascimento, genero, endereco, consulta):
        super().__init__(nome, CPF, data_nascimento, genero, endereco)
        self.agenda = agenda
        self.consulta = consulta

    def marcarConsulta(self, consulta, CRM):
        Medico(CRM)
        self.agenda = Consultas.agendarConsultas(consulta)

    def remarcarConsulta(self, consulta, CRM):
        Medico(CRM)
        self.agenda = Consultas.agendarConsultas(consulta)

    def desmarcarConsulta(self):
        del self.consulta

    def marcarExame(self, exame, nome, CPF, data_nascimento, genero, convenio):
        Paciente(nome, CPF, data_nascimento, genero, convenio)
        Consultas.agendarExames(exame)

    def remarcarExame(self, exame, nome, CPF, data_nascimento, genero, convenio):
        Paciente(nome, CPF, data_nascimento, genero, convenio)
        Consultas.agendarExames(exame)

    def centraldeAjuda(self):
        print('Central de ajuda ao Paciente')

    def abrirAgenda(self, nome, data_hora, consultas, CRM):
        dado1 = Medico(nome, CRM)
        dado2 = Consultas(data_hora, consultas)
        self.agenda = dado1, dado2
