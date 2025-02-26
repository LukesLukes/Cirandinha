import os
os.system("cls||clear")


# Entrada

idade = int(input("Digite a sua idade: "))

# Processamento

if idade >= 18 and idade <= 65:
    resultado = "Voto Obrigatório"
else:
    resultado = "Voto Não-Obrigatório"

# Saída

print(f"\nResultado: {resultado}")














