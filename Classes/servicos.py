class Servicos_Prestados:
    def __init__(self, metodos_pagamento, status_pagamento):
        self.metodos_pagamento = metodos_pagamento
        self.status_pagamento = status_pagamento

    def verificarStatus(self):
        if self.status_pagamento:
            print('Pagamento efetuado')
        else:
            print('Pagamento não realizado')

    def efetuarPagamento(self):
        if not self.status_pagamento:
            modo = int(input("""Digite: [1] para Cartão de Crédito
            [2] para Cartão de Débito
            [3] para Dinheiro
            [4] para Convênio"""))
            while modo not in 1 <= modo <= 4:
                novo = int(input("Opção inválida!\nDigite novamente: "))
                modo = novo
                break
            if modo == 1:
                escolher = input('Escolher cartão de crédito')
                self.metodos_pagamento = escolher
                self.status_pagamento = True
            elif modo == 2:
                escolher = input('Escolher cartão de débito')
                self.metodos_pagamento = escolher
                self.status_pagamento = True
            elif modo == 3:
                escolher = input('Pague diretamente no consultório médico!')
                self.metodos_pagamento = escolher
                self.status_pagamento = True
            elif modo == 4:
                escolher = input('Escolher convênio')
                self.metodos_pagamento = escolher
                self.status_pagamento = True

    def receberPagamento(self):
        adicionar = str(input('Dados da conta de recebimento'))
        self.metodos_pagamento = adicionar
