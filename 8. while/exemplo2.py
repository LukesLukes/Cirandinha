import os
import time
os.system("cls || clear")

contador = 0

while True:
    # comandos a serem repetidos
    print("Repetindo...")

    continua = input("Tecle 's' se deseja continuar: ").strip().lower()
    contador += 1

    if continua != 's':
        break


if contador == 0:
    print("O bloco NÂO foi repetido.")
else:
    print(f"O bloco foi repetido {contador} vezes")