# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE

# qtd_filmes = int(input('Digite quantos filmes deseja adicionar na lista de filmes: '))
# controle = 0

# while controle != qtd_filmes:
#     nome = input('Adicione o filme que deseja: ')
#     filmes.append(nome)
#     controle += 1


# print(filmes)

# LOOP FOR


quantidade = int(input("Quantos filmes você deseja adicionar? "))


for i in range(quantidade):
    nome = input(f"Digite o nome do {i + 1}º filme: ")
    filmes.append(nome)



print(filmes)

