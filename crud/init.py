from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__,template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agenda.sqlite3'
db = SQLAlchemy(app)

class Agenda(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self,nome,email):
        self.nome = nome
        self.email = email



@app.route('/')
def index():
    Cadastro = Agenda.query.all()
    return render_template("contatos.html", Cadastro=Cadastro)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        Cadastro = Agenda(request.form['nome'],request.form['email'])
        db.session.add(Cadastro)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit<int:id>',  methods=['GET', 'POST'])
def edit(id):
    Cadastro = Agenda.query.get(id)
    if request.method == "POST":
       Cadastro.nome = request.form['nome']
       Cadastro.email = request.form['email']
       db.session.commit()
       return redirect(url_for('index'))

    return render_template('edit.html', Cadastro=Cadastro)

@app.route('/deletar<int:id>')
def delete(id):

    Cadastro = Agenda.query.get(id)
    db.session.delete(Cadastro)
    db.session.commit()

    return  redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)