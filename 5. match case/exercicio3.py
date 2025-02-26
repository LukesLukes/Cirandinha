import os
os.system("cls||clear")

# Desenvolva um programa que receba como entrada um número inteiro que represente um dos 7 dias -
# da semana e imprima 
# 


dia = int(input("Digite um número de 1 a 7, que represente os dias da semana: "))

match dia:

    case 1:
        print("Hoje é domingo. Final de Semana!")
    case 2:
        print("Hoje é segunda feira. Dia útil.")
    case 3:
        print("Hoje é terça feira. Dia útil.")
    case 4:
        print("Hoje é quarta feira. Dia útil.")    
    case 5:
        print("Hoje é quinta feira. Dia útil.")    
    case 6:
        print("Hoje é sexta feira. Dia útil.")
    case 7:
        print("Hoje é sábado. Final de semana!")    
    case _:
        print("Dia inválido.")

print(dia)

print("===FIM==")





































