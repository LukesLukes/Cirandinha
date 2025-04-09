import os
import time

def limpar_terminal():
    # Limpar a tela do terminal
    os.system("cls || clear")

# Função - Produto Inflacionado
def inflacionar_preco(preco):
    if preco < 100:
        preco_inflacionado = preco * 1.10 # Inflação de 10%
    else:
        preco_inflacionado = preco * 1.20 # Inflação de 20%
    return preco_inflacionado

# Entrada de Dados
limpar_terminal()
preco_do_produto = float(input("Digite o preço do produto: R$ "))

# Processamento de Dados
preco_inflacionado = inflacionar_preco(preco_do_produto)

# Saída de Dados
limpar_terminal()
print("O preço do produto com inflação é...")
time.sleep(2)

print(f"R$ {preco_inflacionado:.2f}.")
