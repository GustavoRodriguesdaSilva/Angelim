from pessoa import *


class Paciente(Pessoa):
    def __init__(self, convenio, observacao):
        self.convenio = convenio
        self.observacao = observacao
        pass
