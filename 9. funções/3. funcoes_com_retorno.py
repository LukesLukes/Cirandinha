# Funções com retorno

import os
os.system("cls || clear")

def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    media = soma / 2
    return media # Devolvendo a execução dos códigos acima para a função.

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

media = calcular_media(primeiro_numero, segundo_numero) # Chamando a função e executando o que há nela.

print(f"Média: {media}")