dias = int(input('DIgite aqui quantos dias você alugou o carro: '))
km = float(input('Digite aqui quantos kilometros você andou com o carro: '))
total_dias = dias * 60
total_km = km * 0.15
pagar_total = total_dias + total_km
print(f'você andou por {dias} dias e {km} km, então o preço à se pagar é de {pagar_total}')