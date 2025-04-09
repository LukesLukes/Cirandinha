import os
from datetime import date
import time

def limpar_terminal():
    # Limpar a tela do terminal
    os.system("cls || clear")

# Função - Calcular Idade
def calcular_idade(idade):
    idade = date.today().year - ano_nascimento
    return idade

# Entrada de Dados
limpar_terminal()
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

# Processamento de Dados
idade = calcular_idade(ano_nascimento)

# Saída de Dados
limpar_terminal()
print("Atualmente, você tem...")
time.sleep(2)
print(f"{idade} anos.")

