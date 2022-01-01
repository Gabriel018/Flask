from flask import  Flask,render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/<name_user>")
def user(name_user):
    return render_template('Perfil.html',name_user=name_user)

if __name__ == '__main__':
    app.run(debug=True)