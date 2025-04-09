import os
import time

nota = 0

def limpar_terminal():
    # Limpar a tela do terminal
    os.system("cls || clear") 

def calcular(media):
    media = nota / 2
    return media

limpar_terminal()
for i in range(2):
    nota += float(input("Digite uma nota: ")) 

media = calcular(nota)

limpar_terminal()
print("Exibindo a média...\n")
time.sleep(2)
print(f"Média: {media}")