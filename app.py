from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar agendamentos (simulação)
agendamentos = []

@app.route('/')
def home():
    return render_template('home.html', agendamentos=agendamentos)

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        data = request.form['data']
        agendamentos.append({'nome': nome, 'email': email, 'data': data})
        return redirect('/sucesso')
    return render_template('agendar.html')

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)
