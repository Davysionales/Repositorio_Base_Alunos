print('| __________________ |\n Sistema de Provas\n| __________________ |')

Nome = input("Digite o nome do aluno: ")
Nota1 = float(input("Digite a nota do aluno da primeira prova: "))
Nota2 = float(input('Digite a nota do aluno da segunda prova: '))
Nota3 = float(input('Digite a nota do aluno da terceira prova: '))
Nota4 = float(input('Digite a nota do aluno da quarta prova: '))

Média = round((Nota1 + Nota2 + Nota3 + Nota4) / 3, 1)
print('| __________________ |')
print(f'A média do aluno é: {Média}. Aprovado: {Média >=5}')