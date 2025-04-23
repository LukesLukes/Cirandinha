import os
import time

def limpar_terminal():
    # Limpando o terminal
    os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5

def armazenar_numeros():

    # Adicionando os 6 números na lista.
    for i in range(QUANTIDADE_NUMEROS):
        numero = int(input(f"Digite o {i+1}º número: "))
        if numero < 0:
            numero = 0
        lista_numeros.append(numero)

limpar_terminal()
armazenar_numeros()

# Listando os números
limpar_terminal()
for i, numero in enumerate(lista_numeros, start=1): #ForEach
    print(f"{i}º número: {numero}")
    time.sleep(1)
    