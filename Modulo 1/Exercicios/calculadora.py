

print('||-------------||\n Calculadora \n||-------------||\n')

print('Opções\n 1 Soma \n 2 Subtração \n 3 Multiplicação \n 4 Divisão\n')

opcao = int(input('Escolha uma das opções: '))
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if opcao == 1:
    
    print(f'O resultado é: {num1 + num2}')

elif opcao == 2:
    print(f'O resultado é: {num1 - num2}')

elif opcao == 3:
    print(f'O resultado é: {num1 * num2}')

elif opcao == 4:
    print(f'O resultado é: {num1 / num2}')

else:
    print('Isso não é uma opção.')