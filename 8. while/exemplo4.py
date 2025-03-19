import os
os.system("cls || clear")


while True:
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Somente maiores de 18 anos.\n")
    else:
        break

print("FIM")