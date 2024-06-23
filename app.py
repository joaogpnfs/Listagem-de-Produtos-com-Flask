from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

produtos = []

@app.route('/')
def index():
    return redirect(url_for('listar_produtos'))

@app.route('/listar')
def listar_produtos():
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    return render_template('listar.html', produtos=produtos_ordenados)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        disponivel = request.form['disponivel'] == 'sim'
        produtos.append({
            'nome': nome,
            'descricao': descricao,
            'valor': valor,
            'disponivel': disponivel
        })
        return redirect(url_for('listar_produtos'))
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)