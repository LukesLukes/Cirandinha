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

# Adicionando os 6 números na lista.
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

# Verificando quantos números são pares e quantos são ímpares.
pares, impares = pares_impares(lista_numeros)

# Exibindo resultados...
limpar_terminal()
for i, numero in enumerate(lista_numeros, start=1): #ForEach
    print(f"{i}º número: {numero}")
    time.sleep(1)

# Exibindo a quantidade de números pares e ímpares.
print(f"\nNúmeros pares: {pares}")
print(f"Números ímpares: {impares}")


