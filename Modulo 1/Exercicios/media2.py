print('| __________________ |\n Sistema de Provas\n| __________________ |')

Nome = input("Digite o nome do aluno: ")
Nota1 = float(input("Digite a nota do aluno da primeira prova: "))
Nota2 = float(input('Digite a nota do aluno da segunda prova: '))
Nota3 = float(input('Digite a nota do aluno da terceira prova: '))
Nota4 = float(input('Digite a nota do aluno da quarta prova: '))

Média = round((Nota1 + Nota2 + Nota3 + Nota4) / 4, 1)
print('| __________________ |')

if Média >= 5:
    print(f'O aluno(a) {Nome} foi com uma média de {Média}.')
else:
    print(f'O aluno(a) {Nome} reprovou com uma média de {Média}, Parabéns.')
