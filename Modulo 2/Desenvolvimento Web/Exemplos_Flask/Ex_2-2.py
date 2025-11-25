# Exercicio 2-2: Links entre rotas
# Adicione um menu de navegação simples com links para todas as suas rotas (/, /sobre, /saudacao, etc.).
# Passar a variável através do 'url_for' dentro do script html: ("{{ url_for('saudacao', nome='João') }}")
# 'saudacao' é o nome da função Python que define a rota.
# nome='João' está passando o valor para a variável que a rota espera (<nome>).

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Meu nome começa com "DA" e termina com "VI"'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    if nome == 'Davi':
        return 'Olá meu lindo, maravilhoso, perfeito, prefeito, não imperfeito, presidente, Davisionário. Bom dia'
    else:
        return f'Olá {nome}. Seja bem vindo'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O número {numero}, multiplicado por 2, é igual à: {numero * 2}'


if __name__ == '__main__':
    app.run(debug=True)


