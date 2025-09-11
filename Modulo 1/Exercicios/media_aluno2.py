print('SISTEMA DE PROVAS')
cont = 1
qtd_provas = int(input('Quantas provas o aluno fez? '))

while cont <= qtd_provas:
    nota = float(input(f'Digite a nota do aluno da prova {qtd_provas}: '))
    nota_total = nota + nota 
    cont += 1
    
    


media = (nota_total)  /  qtd_provas
print(f'O aluno obteve a média de: {media}')
