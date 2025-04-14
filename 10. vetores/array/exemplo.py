import os
import time

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

# Criando uma lista.
lista_notas = []

# Adicionado 3 notas em uma lista.
limpar_terminal()
for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Exibindo todods os valores em uma lista.
limpar_terminal()
print("Exibindo as notas inseridas...\n")
time.sleep(2)
for nota in lista_notas: #ForEach
    print(nota)
    time.sleep(2)