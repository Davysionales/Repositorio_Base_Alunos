# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------





print('|------------------------------|\n| Calculadora|\n|------------------------------|\n1 - Soma|\n2 - Subtração|\n3 - Multiplicação|\n4 - Divisão|\n|------------------------------|')

opcao = int(input('Digite uma das opção: '))
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if opcao == 1:
    print(f'O resultado é:  {num1 + num2}')

elif opcao == 2:
    print(f'O resultado é: {num1 - num2}')
    
elif opcao == 3:
    print(f'O resultado é: {num1 * num2}')
    
elif opcao == 4:
    print(f'O resultado é: {num1 / num2}')
else:
    print('Isso não é uma opção.')