import requests
from flask import Flask,render_template,session,request,redirect,url_for,g

import  os


app = Flask(__name__,template_folder='template')

app.secret_key= os.urandom(24)

@app.route('/', methods=["GET","POST"])
def index():
 if request.method == "POST":
     session.pop('user',None)

     if request.form['password'] == 'password':
        session['user'] = request.form['username']
        return redirect(url_for('login'))
 return render_template('index.html')

@app.route('/login')
def login():
 if g.user:
     return render_template('log.html', user=session['user'])
 return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']


if __name__ == '__main__':

 app.run(debug=True)