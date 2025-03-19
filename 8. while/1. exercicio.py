import os
os.system("cls || clear")


while True:
    nota = int(input("Digite a nota do aluno: "))

    if nota < 0 or nota > 10:
        print(f"Nota: {nota}")
    else:
        print(f"Nota: {nota}")
        break
        

print("FIM")