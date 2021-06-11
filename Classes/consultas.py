from paciente import Paciente


class Consultas:
    def __init__(self, data_hora, local, medico, consultas, exames, prontuario, retorno):
        self.data_hora = data_hora
        self.local = local
        self.medico = medico
        self.consultas = consultas
        self.exames = exames
        self.prontuario = prontuario
        self.retorno = retorno

    def agendarConsultas(self, nome, CPF, data_nascimento, genero, convenio):
        Paciente(nome, CPF, data_nascimento, genero, convenio)
        medico = str(input('Escolha o médico'))
        self.medico = medico
        local = str(input('Escolha o local: '))
        self.local = local
        data = str(input('Escolha a data e horário: '))
        self.data_hora = data

    def agendarExames(self, nome, CPF, data_nascimento, genero, convenio):
        Paciente(nome, CPF, data_nascimento, genero, convenio)
        medico = str(input('Escolha o exame'))
        self.exames = medico
        local = str(input('Escolha o local: '))
        self.local = local
        data = str(input('Escolha a data e horário: '))
        self.data_hora = data

    def emitirLaudo(self):
        laudo = [self.consultas, self.exames, self.medico, self.data_hora, self.local]
        self.prontuario = laudo
