import os
import time

nota = 0
media = 0

def limpar_terminal():
    # Limpar a tela do terminal
    os.system("cls || clear")

def calcular(media):
    media = nota / 3
    return media

def aprovacao(resultado):
    if media >= 7:
        resultado = "Aprovado."
    else:
        resultado = "Reprovado."
    return resultado

limpar_terminal()
for i in range(3):
    nota += float(input("Digite uma nota: "))

media = calcular(nota)
resultado = aprovacao(media)

limpar_terminal()
print("Exibindo resultados...")
time.sleep(2)
limpar_terminal()
print(f"Média: {media:.2f}")
print(f"O aluno foi {resultado}")