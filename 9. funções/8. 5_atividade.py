import os
import time

def limpar_terminal():
    # Limpar a tela do terminal
    os.system("cls || clear")

limpar_terminal()
def calcular_media(primeira_nota, segunda_nota):
    limpar_terminal()
    soma = primeira_nota + segunda_nota
    media = soma / 2
    if media >= 7:
        print("Você foi...")
        time.sleep(2)
        print("Aprovado! Parabéns!")
    else:
        print("Você foi...")
        time.sleep(2)
        print("Reprovado. Não desista, estude mais e tente novamente!")    
    return media # Devolvendo a execução dos códigos acima para a função.

limpar_terminal
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
media = calcular_media(primeira_nota, segunda_nota)
print(f"A sua média é: {media}")    