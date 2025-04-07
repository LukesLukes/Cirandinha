import os
import time

def limpar_terminal():
    # Limpar a tela do terminal
    os.system("cls || clear")

# Função
def valor_em_centimetros(valor):
    centimetros = valor / 100
    return centimetros

# Entrada de Dados
limpar_terminal()
valor = int(input("Digite um valor em metros: "))

# Processamento de Dados
centimetros = valor_em_centimetros(valor)

# Saída de Dados
limpar_terminal()
print("Exibindo o resultado da conversão de 'metros' para 'centímetros'...")
time.sleep(2)
print(f"O valor {valor} em centimetros é: {centimetros} cm.")