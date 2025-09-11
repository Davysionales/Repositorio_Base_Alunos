

from colorama import init,Fore
init(autoreset=True)


numero = int(input("Digite um número: "))




if numero == 1:
    print(Fore.LIGHTBLUE_EX+'Domingo')

elif numero == 2:
    print(Fore.GREEN+'Segunda')

elif numero == 3:
    print(Fore.LIGHTGREEN_EX+'Terça')

elif numero == 4:
    print(Fore.LIGHTMAGENTA_EX+'Quarta')

elif numero == 5:
    print(Fore.LIGHTYELLOW_EX+'Quinta')

elif numero == 6:
    print(Fore.LIGHTWHITE_EX+'Sexta')

elif numero == 7:
    print(Fore.BLUE+'Sábado')

else:
    print(Fore.LIGHTRED_EX+'Número errado seu bobalhão')


