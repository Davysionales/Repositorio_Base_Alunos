from flask import Flask, render_template, request
import json
import resend

resend.api_key = "re_XHjpR5zx_MDG29KDEQzGYFPs9y2W2Zpsz"

with open('contatos.json', 'r', encoding='utf-8') as f:
    contatos = json.load(f)


app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def index():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        mensagem = request.form['message']

        contato = {}
        contato['nome'] = nome
        contato['email'] = email
        contato['mensagem'] = mensagem

        contatos.append(contato)

        with open('contatos.json', 'w', encoding='utf8') as f:
            json.dump(contatos, f, indent=4, ensure_ascii=False)

        email_html = f"""
        <h1> Novo contato de {nome}!</h1><br>
        <p>Email: {email}</p><br>
        <p>{mensagem}</p>

        """

        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "cavalocavalo823@gmail.com",
        "subject": "Contato de adoção de pets",
        "html": email_html
        })



    return  render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)