from myapp import app
from bottle import template, static_file, request, redirect
from myapp.models.tables import User

#static routes
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='myapp/static/css')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='myapp/static/js')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='myapp/static/fonts')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='myapp/static/img')

@app.route('/')
def login():
    return template('login', sucesso=True)

@app.route('/cadastro')
def cadastro():
    return template('cadastro', existe_usuario=False)

@app.route('/cadastro', method='POST')
def acao_cadastro(db):
    usuario = request.forms.get('usuario')
    senha = request.forms.get('senha')
    try:
        db.query(User).filter(User.usuario == usuario).one()
        existe_usuario = True
    except:
        existe_usuario = False
    if not existe_usuario:
        new_user = User(usuario, senha)
        db.add(new_user)
        return redirect('/usuarios')
    return template('cadastro', existe_usuario=True)

@app.route('/', method='POST')
def acao_login(db):
    usuario = request.forms.get('usuario')
    senha = request.forms.get('senha')
    result = db.query(User).filter((User.usuario == usuario) & (User.senha == senha)).all()
    if result:
        return redirect('/usuarios')
    return template('login', sucesso=False)

@app.route('/usuarios')
def usuarios(db):
    usuarios = db.query(User).all()
    return template('lista_usuarios', usuarios=usuarios)

@app.error(404)
def error404(error):
    return template('pagina404')
