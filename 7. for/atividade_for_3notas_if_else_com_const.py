import os
os.system("cls || clear")

soma = 0
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    soma += nota
    
media = soma / QUANTIDADE_NOTAS

if media >= 7:
         print("Parabéns! Você foi aprovado")
elif media < 7 and media >= 4:
        print("Você está na recuperação.")
else:
        print("Você foi reprovado.")    

print()
print(f"Média: {media}")


print("\nFIM DO PROGRAMA")

    

