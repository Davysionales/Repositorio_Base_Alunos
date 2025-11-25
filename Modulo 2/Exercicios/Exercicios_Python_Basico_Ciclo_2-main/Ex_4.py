# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

#7.9375

# LOOP WHILE
# soma = 0
# controle = 0
# while controle <= 3:
#     n = float(notas[controle])
#     controle += 1
   
#     soma = soma + n
    
#     media = round(soma/4, 2)
# print(media)







# LOOP FOR

soma = 0

for nota in notas:
    n = float(nota)
    soma = soma + n
    media = soma / 4

print(f'A media das notas é {media:.2f}')




