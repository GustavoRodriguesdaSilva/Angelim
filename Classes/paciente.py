from pessoa import Pessoa
from consultas import Consultas


class Paciente(Pessoa):
    def __init__(self, convenio, observacoes, nome, CPF, data_nascimente, genero, endereco):
        super().__init__(nome, CPF, data_nascimente, genero, endereco)
        self.convenio = convenio
        self.observacoes = observacoes

    def marcarConsultas(self):
        Consultas.agendarConsultas()

    def marcarExames(self):
        Consultas.agendarExames()

    def receberLaudo(self):
        Consultas.emitirLaudo()

    def modificarConvenio(self):
        novo_convenio = str(input('Digite o nome do convênio e o número da carteirinha: '))
        self.convenio = novo_convenio
