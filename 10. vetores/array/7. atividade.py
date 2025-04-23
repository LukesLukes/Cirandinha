import os
import time

def limpar_terminal():
    # Limpando o terminal
    os.system("cls || clear")

limpar_terminal()
lista_numeros = []
QUANTIDADE_NUMEROS = 5

def positivos_negativos(lista):
    soma = 0
    negativos = 0
    for numero in lista:
        if numero > 0:
            soma += numero
        else:
            negativos += 1
    return soma, negativos

def solicitando_numeros():
    # Adicionando os 6 números na lista.
    for i in range(QUANTIDADE_NUMEROS):
        numero = int(input(f"Digite o {i+1}º número: "))
        lista_numeros.append(numero)




# Verificando quantos números são pares e quantos são ímpares.
lista = solicitando_numeros()
soma, negativos = positivos_negativos(lista_numeros)

# Exibindo resultados...
limpar_terminal()
for i, numero in enumerate(lista_numeros, start=1): #ForEach
    print(f"{i}º número: {numero}")
    time.sleep(1)

# Exibindo a quantidade de números pares e ímpares.
print(f"\nSoma dos números positivos: {soma}")
print(f"Números negativos: {negativos}")



