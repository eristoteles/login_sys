from app import app
from bottle import template, static_file, request

#static routes
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@app.route('/')
def login():
    return template('login')

@app.route('/cadastro')
def cadastro():
    return template('cadastro')

@app.route('/cadastro', method='POST')
def acao_cadastro():
    usuario = request.forms.get('usuario')
    senha = request.forms.get('senha')
    insert_user(usuario, senha)
    return template('verificacao_cadastro', nome=usuario)

@app.route('/', method='POST')
def acao_login():
    usuario = request.forms.get('usuario')
    senha = request.forms.get('senha')
    return template('verificacao_login', sucesso=True)

@app.error(404)
def error404(error):
    return template('pagina404')
