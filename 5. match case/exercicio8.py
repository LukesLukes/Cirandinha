import os
os.system("clear || cls")

# Elabore um algoritmo usando operações lógicas para uma empresa que quer verificar se um empregado está qualificado para
# a aposentadoria ou não.
# 


# Entrada

codigo_do_empregado = input("Digite a matrícula do empregado: ")
ano_de_nascimento = int(input("Digite o ano de seu nascimento: "))
tempo_de_trabalho = int(input("Digite o tempo de trabalho, em anos, do empregado: "))

# Processamento

idade = 2025 - ano_de_nascimento

if idade > 65 or tempo_de_trabalho >= 30:
   resultado = "Requerer aposentadoria."
else:
   resultado = "Não requerer aposentadoria."

# Saída
print(f"\nMatrícula: {codigo_do_empregado}")
print(f"Idade: {idade}")
print(f"Tempo de trabalho: {tempo_de_trabalho}")
print(f"Resultado: {resultado}")





































































































































