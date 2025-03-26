# Construa um algoritmo que calcule a média aritmética de vários valores inteiros positivos, inseridos pelo usuário.
# O final da leitura acontecerá quando for lido um valor negativo
# Mostre a média aritmética dos números inforamdos pelo usuário. 

import os
os.system("cls || clear")

soma = 0
contador = 0

while True:
    valor_inteiro = int(input("Digite um valor: "))   

    if valor_inteiro < 0:
        break    
    else:    
        contador += 1
        soma += valor_inteiro   
        media = soma / contador


# Evita divisão por zero
if contador == 0:
    soma = valor_inteiro
    contador = 1

print(f"Média: {media}")

