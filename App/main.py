from App import app
@app.route('/')
def index():
    return '<h1>Início</h1>'

@app.route('/home')
def home():
    return '<h1>Angelim</h1>'

@app.route('/login_medico')
def login_medico():
    return '<h1>Autenticação</h1>'

@app.route('/login_paciente')
def login_paciente():
    return '<h1>Autenticação</h1>'

@app.route('/cadastro')
def cadastro():
    return '<h1>Cadastro</h1>'

@app.route('/cadastro_medico')
def cadastro_medico():
    return '<h1>Cadastro</h1>'

@app.route('/cadastro_paciente')
def cadastro_paciente():
    return '<h1>Cadastro</h1>'

@app.route('/pagamento_paciente')
def pagamento_paciente():
    return '<h1>Pagamento</h1>'

@app.route('/pagamento_medico')
def pagamento_medico():
    return '<h1>Pagamento</h1>'

@app.route('/agenda_medico')
def agenda_medico():
    return '<h1>Agenda</h1>'

@app.route('/agenda_paciente')
def agenda_paciente():
    return '<h1>Agenda</h1>'

@app.route('/historico')
def historico():
    return '<h1>Histórico</h1>'

@app.route('/anotacoes')
def anotacoes():
    return '<h1>Anotações</h1>'

@app.route('/prontuario')
def prontuario():
    return '<h1>Prontuário</h1>'

@app.route('/remarcar_medico')
def remarcar_medico():
    return '<h1>Remarcar Consulta</h1>'

@app.route('/login_assistente')
def login_assistente():
    return '<h1>Autenticação</h1>'

@app.route('/assistente')
def assistente():
    return '<h1>Página Inicial</h1>'

@app.route('/agenda_assistente')
def agenda_assistente():
    return '<h1>Agenda</h1>'

@app.route('/marcar_exame_assistente')
def marcar_exame_assistente():
    return '<h1>Remarcar Exame</h1>'

@app.route('/paciente')
def paciente():
    return '<h1>Página Inicial</h1>'

@app.route('/medico')
def medico():
    return '<h1>Página Inicial</h1>'
