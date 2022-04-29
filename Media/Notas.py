from flask import Flask,render_template,request

Media = Flask(__name__,template_folder='template')

@Media.route('/')
def home():

    return render_template('notas.html')


@Media.route('/notas', methods=['POST'])
def situacao():

    total = sum([int(v) for v in request.form.to_dict().values()])
    return  render_template('situacao.html',total=total)
Media.run(debug=True)