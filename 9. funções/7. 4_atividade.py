import os
import time
os.system("cls || clear")

def inteiro(parametro):
    os.system("cls || clear")
    print("É positivo ou negativo...")
    time.sleep(2)
    if parametro > 0: 
        print(f"O número {parametro} é positivo!")
    elif parametro == 0:
        print(f"O número {parametro} é neutro.")    
    else:
        print(f"O número {parametro} é negativo!")

numero = int(input("Digite um número: "))
inteiro(numero)        
           
