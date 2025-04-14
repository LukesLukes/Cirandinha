import os
import time

def limpar_terminal():
    # Limpando o terminal
    os.system("cls || clear")

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

limpar_terminal()
lista_numeros = []
QUANTIDADE_NUMEROS = 6

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

pares, impares = pares_impares(lista_numeros)

limpar_terminal()
for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}º núemro: {numero}")
    time.sleep(1)
       
print(f"\nOs números pares são: {pares}")
print(f"Os números ímpares são: {impares}")