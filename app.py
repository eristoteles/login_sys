from bottle import route, run
from bottle import request, template
from bottle import static_file, get
from bottle import error
import os

'''@route('/')
@route('/user/<nome>')
def index(nome='Desconhecido'):
    return '<center><h1>Olá ' + nome + '</h1></center>'
'''

#static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@route('/')
def login():
    return template('login')

def check_login(usuario, senha):
    d = {'tote': '1234', 'tote1': '1q2w3e', 'tote2': '9999'}
    if usuario in d.keys() and d[usuario] == senha:
        return True
    return False

@route('/', method='POST')
def acao_login():
    usuario = request.forms.get('usuario')
    senha = request.forms.get('senha')
    return template('verificacao_login', sucesso=check_login(usuario, senha), nome=usuario)

@error(404)
def error404(error):
    return template('pagina404')

if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        run(host='localhost', port=8080, debug=True, reloader=True)