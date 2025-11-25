# Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Crie um dicionário com duas chaves: "pares" e "ímpares", onde cada chave terá uma lista com os números correspondentes.


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valores = {
    'par' : [],
    'impar' : [], 
}



for n in numeros:
    valor = n % 2
    if valor == 0:
        valores['par'].append(n)

    else:
        valores['impar'].append(n)

print(valores)







