# EXERCICIO 1-2: Rota personalizada
# Adicione uma nova rota /sobre que retorna uma mensagem com seu nome e uma frase sobre você.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo!'

@app.route('/sobre')
def sobre():
    return 'Eae, eu sou o Davi. Quero cursar a área de TI, e me tornar um seniôr profissa' 

if __name__ == '__main__':
    app.run(debug=True)