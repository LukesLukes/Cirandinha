import os
import time

def limpar_terminal():
    # Limpando o terminal
    os.system("cls || clear")

# Criando uma lista.
lista_numeros = []
QUANTIDADE_NUMERO = 5

# Adicionando os 5 números na lista.
limpar_terminal()
for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

# Verificando qual o maior e menor número.
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

# Exibindo resultados...
limpar_terminal()
for i, numero in enumerate(lista_numeros, start=1): #ForEach
    print(f"\n{i}º número: {numero}")
    time.sleep(1)
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
