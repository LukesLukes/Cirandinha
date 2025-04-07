import os
os.system("cls || clear")


def pares_e_impares(parametro):        
    if numero % 2 == 0:
        print(f"O número {parametro} é par.")
    else:
        print(f"O número {parametro} é ímpar.")

numero = int(input("Digite um número: "))
pares_e_impares(numero)