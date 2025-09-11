
carro = input('Qual é o modelo do carro?\n Escreva aqui: ')

valor = 0

if carro == 'Onix':
    valor = 500

elif carro == 'Kombi':
    valor = 50

elif carro == 'Spark':
    valor = 300

else:
    valor = 100

dias = int(input('Quantos dias você ficou com o carro alugado?\n Escreva aqui: '))

km = float(input('Quantos km você dirigiu com o carro?\n Escreva aqui: '))

total_dias = valor * dias
total_km = km * 0.15
total_pagar = total_dias + total_km
print(f'Você alugou o carro {carro} por {dias} e andou por {km} km, logo o preço à se pagar é de: R$ {total_pagar}')