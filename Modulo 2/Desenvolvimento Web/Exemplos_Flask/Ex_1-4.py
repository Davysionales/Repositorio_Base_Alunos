# EXERCICIO 1-4: Rota com número (tipagem na rota)
# Crie uma rota /dobro/<int:numero> que recebe um número e retorna o dobro dele.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo!'

@app.route('/sobre')
def sobre():
    return 'Eae, eu sou o Davi. Quero cursar a área de TI, e me tornar um seniôr profissa' 

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
