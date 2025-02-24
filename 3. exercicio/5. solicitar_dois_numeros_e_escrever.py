import os
os.system("clear")

# Elabore um algoritmo usando operações lógicas para solicitar ao usuário 2 números e escrever:

# Os números informados;
# O maior número;
# O menor número;

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo_número: "))

if primeiro_numero > segundo_numero:
   menor = segundo_numero
   maior = primeiro_numero
else:
   menor = primeiro_numero
   maior = segundo_numero


print("\nExibindo resultados: ")
print(f"Menor: {menor}")
print(f"Maior: {maior}")














