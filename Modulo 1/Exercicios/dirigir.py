idade = int(input('Digite a sua idade: '))
habilitacao = str(input('Você tem habilitação? (s/n?): '))
print(f'Você é maior de idade? {idade >= 18 and habilitacao == 's'}')