import json

with open('senha.json', 'r') as f:
    dados = json.load(f)

    email = input('Confirme seu email: ')
    senha = input('Confirme sua senha: ')

if email == dados['email'] and senha == dados['senha']:
    print('Pode entrar vacilão')

else:
    print('Saí pra lá, vacilão')