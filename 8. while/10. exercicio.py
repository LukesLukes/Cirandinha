# Faça um algoritmo que leia uma quantidade não determinada de números inteiros positivos. Calcule:
# a. quantidade de números pares e ímpares;
# b. média de valores pares;
# c. média geral dos números lidos.
# O número que encerrará a leitura será o número zero.

import os
os.system("cls || clear")

contador_pares = 0
contador = 0
soma_pares = 0
soma_impares = 0
soma_total = 0
pares = 0
impares = 0

while True:
    numero = int(input(f"Digite o {contador + 1}º número: "))

    if numero == 0 or numero == ' ':
        break
    if numero % 2 == 0:
        contador += 1
        contador_pares += 1
        pares += 1
        soma_pares += pares
        soma_total += numero
    else:
        contador += 1
        impares += 1
        soma_impares += impares
        soma_total += numero
        
media_pares = soma_pares / contador_pares    
media = soma_total / contador

os.system("cls || clear")

print(f"\nPares: {pares}")
print(f"Soma de Números Pares: {soma_pares}")
print(f"\nÌmpares: {impares}")
print(f"Soma de Números Ìmpares: {soma_impares}")
print(f"\nQuantidade Total de Números: {contador}")
print(f"\nMédia dos Valores Pares: {media_pares:.1f}")
print(f"Média Geral: {media:.1f}")