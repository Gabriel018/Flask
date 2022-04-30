import requests
from flask import Flask,render_template,session,request,redirect,url_for


app = Flask(__name__,template_folder='template')

app.secret_key='12345'

@app.route('/')
def index():
    username = ''
    if username in session:
       username = session['username']
    return   render_template('index.html', username=username)

@app.route('/login', methods=['GET','POST'])
def login():
 if request.method == 'POST' and request.form['username'] :
     session['username'] = request.form['username']
     return redirect(url_for('index'))
 return render_template('log.html')

if __name__ == '__main__':

 app.run(debug=True)