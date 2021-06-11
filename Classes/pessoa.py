class Pessoa:
    def __init__(self, nome, CPF, data_nascimento, genero, endereco):
        self.nome = nome
        self.CPF = CPF
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.endereco = endereco

    def alterarDados(self):
        alterar = int(input("""Para alterar: Nome digite [1]
                      CPF digite [2]
                      Data de Nascimento digite [3]
                      Gênero digite [4]
                      Endereço digite [5]"""))

        while alterar not in 1 <= alterar <= 5:
            novamente = int(input('Opção não válida!\nDigite novamente: '))
            alterar = novamente
            break

        if alterar == 1:
            nome = str(input('Digite o nome: '))
            self.nome = nome
        elif alterar == 2:
            cpf = str(input('Digite o CPF: '))
            self.CPF = cpf
        elif alterar == 3:
            nascimento = str(input('Digite a data de nascimento: '))
            self.data_nascimento = nascimento
        elif alterar == 4:
            genero = str(input('Digite o gênero'))
            self.genero = genero
        elif alterar == 5:
            endereco = str(input('Digite o endereço: '))
            self.endereco = endereco
