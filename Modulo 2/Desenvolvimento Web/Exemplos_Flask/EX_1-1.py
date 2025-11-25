#EXERCICIO 1-1: Hello FLask!
# Crie um app Flask básico que exibe "Olá, mundo!" na rota principal (/).
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo!'
 

if __name__ == '__main__':
    app.run(debug=True)

