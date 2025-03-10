import os
os.system("clear")

# Faça um programa que calcule o "peso ideal" de um usuário de acordo com um caractere identificador de sexo ("M" para Masculino ou
# "F" para Feminino) inserido pelo mesmo. A fórmula para cada um dos dois casos está definida abaixo.

# Caso "M", utilize a fórmula:
# (72.7 x altura) - 58
# Caso "F", utilize a fórmula: 
# (62.1 x altura) - 44.7

altura = float(input("Digite a sua altura: "))
sexo = input("Digite seu sexo: ").upper()

match sexo:
    case 'M':
        peso_ideal = (72.7 * altura) - 58
        print(f"\nPeso ideal: {peso_ideal}")
    case 'F':
        peso_ideal = (72.7 * altura) - 44.7
        print(f"\nPeso ideal: {peso_ideal}")
    case _:
        print("Opção inválida.")    














































