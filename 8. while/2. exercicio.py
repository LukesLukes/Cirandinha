import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input("Digite uma nota do aluno: "))
        
        if nota < 0 or nota > 10:
            print("A nota deve ser entre 0 e 10.\n")
        else:
            soma += nota
            break
        
media = soma / QUANTIDADE_NOTAS


print("FIM")