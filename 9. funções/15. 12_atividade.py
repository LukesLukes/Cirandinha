import os
import time

peso = 0
altura = 0

def limpar_terminal():
    # Limpar a tela do terminal
    os.system("cls || clear")

# Função - Calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return imc

# Função - Resultado do IMC
def resultado_imc(imc):
    if imc < 18.5:
        resultado = "Abaixo do peso"
    elif imc >= 18.5 and imc <= 24.9:
        resultado = "Peso normal"        
    elif imc >= 25 and imc >= 29.9:
        resultado = "Sobrepeso"
    elif imc >= 30 and imc >= 34.9:
        resultado = "Obesidade Grau 1"
    elif imc >= 35 and imc >= 39.9:
        resultado = "Obesidade Grau 2"
    else:
        resultado = "Obesidade Grau 3"
    return resultado

# Entrada de Dados
limpar_terminal()
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# Processamento de Dados
imc = calcular_imc(peso, altura)
resultado = resultado_imc(imc)

# Saída de Dados
limpar_terminal()
print(f"O seu IMC é: {calcular_imc(peso, altura):.2f}\n")
print("A sua classificação é...")
time.sleep(3)
print(f"{resultado}")
