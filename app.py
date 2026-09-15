from flask import Flask, render_template, request, flash, url_for, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


@app.route('/')
def home():
    return render_template("pagina_inicial.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/base2')
def base2():
    return render_template("base2.html")

@app.route('/cadastro_maquinas')
def cad_maquinas():
    return render_template("cad_maquinas.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)