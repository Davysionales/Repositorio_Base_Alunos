import time
print('\n\n\n\n\n\n')
print('| Verifique se sua saúda está em dia! |\n|-------------------------------------| ')

altura = float(input(('Informe a sua altura: ')))
peso = float(input(('Informe o seu peso: ')))
print('|-------------------|')
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.2f}\nlogo. . .')

time.sleep(4.4)
if imc < 18.5:
    print('Cuidado com ventos fortes!')

elif imc >= 18.5 and imc < 24.9:
    print('Continue assim.')

elif imc >= 25 and imc < 29.9:
    print('Se acalma Neymarmita')

elif imc >= 30 and imc < 34.9:
    print('')

elif imc >= 35 and imc < 39.9:
    print('Não pula, se não a terra saí da orbita do sol')

elif imc >= 40:
    print('A cada passo, é um meteoro diferente')

print('|-----------------------------------------|')
