import os
os.system("cls || clear")

soma = 0
media = 0

for i in range(4):
    nota = int(input("Digite a nota: "))
    soma += nota

media = soma / 4

print()
print(f"Média:  {media}")


print("\nFIM DO PROGRAMA")