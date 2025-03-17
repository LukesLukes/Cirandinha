import os
os.system("cls || clear")

soma = 0
media = 0

for i in range(3):
    nota = int(input("Digite a nota: "))
    soma += nota
    media = soma / 3

if media >= 7:
        print("Parabéns! Você foi aprovado")
elif media < 7 and media >= 4:
        print("Você está na recuperação.")
else:
        print("Você foi reprovado.")    

print()
print(f"Média: {media}")


print("\nFIM DO PROGRAMA")
