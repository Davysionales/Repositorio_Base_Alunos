# EXERCICIO 1-3: Parâmetros na URL (rotas dinâmicas)
# Crie uma rota /saudacao/<nome> que retorna "Olá, <nome>! Seja bem-vindo!".

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

if __name__ == '__main__':
    app.run(debug=True)