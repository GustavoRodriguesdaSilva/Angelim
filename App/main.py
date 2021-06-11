from flask import render_template
from App import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_paciente')
def login_paciente():
    return render_template('login.html')

@app.route('/cadastro_paciente')
def cadastro_paciente():
    return '<h1>Cadastro</h1>'

@app.route('/pagamento_paciente', methods=['POST'])
def pagamento_paciente():
    return '<h1>Pagamento</h1>'

@app.route('/agenda_paciente', methods=['POST'])
def agenda_paciente():
    return '<h1>Agenda</h1>'

@app.route('/paciente', methods=['POST'])
def paciente():
    return '<h1>Página Inicial</h1>'

@app.route('/home')
def home():
    return '<h1>Angelim</h1>'

@app.route('/login_medico')
def login_medico():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return '<h1>Cadastro</h1>'

@app.route('/cadastro_medico')
def cadastro_medico():
    return '<h1>Cadastro</h1>'

@app.route('/pagamento_medico', methods=['POST'])
def pagamento_medico():
    return '<h1>Pagamento</h1>'

@app.route('/agenda_medico', methods=['POST'])
def agenda_medico():
    return '<h1>Agenda</h1>'

@app.route('/historico', methods=['POST'])
def historico():
    return '<h1>Histórico</h1>'

@app.route('/anotacoes', methods=['POST'])
def anotacoes():
    return '<h1>Anotações</h1>'

@app.route('/prontuario', methods=['POST'])
def prontuario():
    return '<h1>Prontuário</h1>'

@app.route('/remarcar_medico', methods=['POST'])
def remarcar_medico():
    return '<h1>Remarcar Consulta</h1>'

@app.route('/login_assistente')
def login_assistente():
    return render_template('login.html')

@app.route('/assistente', methods=['POST'])
def assistente():
    return '<h1>Página Inicial</h1>'

@app.route('/agenda_assistente', methods=['POST'])
def agenda_assistente():
    return '<h1>Agenda</h1>'

@app.route('/marcar_exame_assistente', methods=['POST'])
def marcar_exame_assistente():
    return '<h1>Remarcar Exame</h1>'

@app.route('/medico', methods=['POST'])
def medico():
    return '<h1>Página Inicial</h1>'
