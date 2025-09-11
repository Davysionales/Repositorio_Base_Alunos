altura = float(input('Digite aqui a sua altura: '))
peso = float(input('Digite aqui o seu peso: '))
imc = peso / (altura ** 2)
print(f'A sua altura é {altura} e o seu peso é {peso}, logo o seu imc é {imc:.2f}')