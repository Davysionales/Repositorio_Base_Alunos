# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('| ______________________________ | \n| SISTEMA DE PROVAS | \n| ______________________________ |')

Nome = input('Digite o nome do aluno: ')
nota1 = int(input('Nota da primeira prova do aluno: '))
nota2 = int(input('Nota da segunda prova do aluno: '))
nota3 = int(input('Nota da terceira prova do aluno: '))
print('| ______________________________ |')
media = (nota1 + nota2 + nota3) / 3

if media >= 5:
    print(f'Aluno: {Nome} \nMédia: {media:.1f}\nAluno aprovado')
else:
    print(f'Aluno: {Nome} \nMédia: {media:.1f}\nAluno reprovado')