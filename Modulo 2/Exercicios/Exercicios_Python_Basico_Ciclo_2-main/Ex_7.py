# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
lista = [
    {
    'nome' : 'Davi',
    'idade' : 51,
    'cidade' : 'Santana de Parnaíba',
    },
    {
        'nome' : 'Johnny',
        'idade' : 23,
        'cidade' : 'Cajamar'
    },
    {
        'nome' : 'Michael Jackson',
        'idade' :  66,
        'cidade' : 'Periferia de Gay'    
     
     }

]

controle = 0
while controle <= 2:
    print(lista[controle]['nome'])
    controle += 1 

