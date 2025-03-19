import os
os.system("cls || clear")

idade = int(input("Digite sua idade: "))

while idade < 18:
    print("Somente maiores de 18 anos.\n")
    idade = int(input("Digite sua idade: "))

print("FIM")