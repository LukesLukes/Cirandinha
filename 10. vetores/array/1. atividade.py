import os
import time

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

# Criando uma lista
lista_notas = []
QUANTIDADE_NOTAS = 3

# Adicionado 3 notas numa lista
limpar_terminal()
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Soma e Média
soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS

# ---- Ou: media = sum(lista_notas) / QUANTIDADE_NOTAS ----

# Exibição de resultados
limpar_terminal()
print("Exibindo as notas inseridas...\n")
time.sleep(2)
for nota in lista_notas: #ForEach
    print(nota)
    time.sleep(2)
print(f"Resultado das notas somadas: {soma}\n")
time.sleep(2)
print(f"Média: {media}")