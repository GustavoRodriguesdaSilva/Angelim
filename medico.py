from pessoa import *


class Medico(Pessoa):
    def __init__(self, crm, especialidade):
        self.crm = crm
        self.especialidade = especialidade
