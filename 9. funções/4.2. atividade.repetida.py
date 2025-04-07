import os
import time

def limpar_terminal():
    # Limpar a tela do terminal
    os.system("cls || clear")


limpar_terminal()
# Funções
def somar_numeros(n1, n2):
    adicao = n1 + n2
    return adicao    
def subtrair_numeros(n1, n2):
    subtracao = n1 - n2
    return subtracao    
def multiplicar_numeros(n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao    
def dividir_numeros(n1, n2):
    divisao = n1 / n2
    return divisao    

# - Dado Opcional
def media_dos_numeros(n1, n2):
    adicao = n1 + n2
    media = adicao / 2
    return media    
# Dado Opcional -

# Entrada de Dados
limpar_terminal()
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Processamento de Dados
adicao = somar_numeros(n1, n2)
subtracao = subtrair_numeros(n1, n2)
multiplicacao = multiplicar_numeros(n1, n2)
divisao = dividir_numeros(n1, n2)
media = media_dos_numeros(n1, n2)

# Saída de Dados
limpar_terminal()
print("Exibindo Resultados...\n")
time.sleep(2)
print(f"Adição: {n1} + {n2}")
print(f"Resultado da adição: {adicao}\n")
time.sleep(2)

print(f"Subtração: {n1} - {n2}")
print(f"Resultado da subtração: {subtracao}\n")
time.sleep(2)

print(f"Multiplicação: {n1} * {n2}")
print(f"Resultado da multiplicação: {multiplicacao}\n")
time.sleep(2)

print(f"Divisão: {n1} / {n2}")
print(f"Resultado da divisão: {divisao}\n")
time.sleep(2)

print(f"Saber a média: ({n1} + {n2}) / 2")
print(f"Média: {media}")
time.sleep(2)