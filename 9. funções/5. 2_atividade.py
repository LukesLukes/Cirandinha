import os
import time
os.system("cls || clear")


print("INÍCIO DO PROGRAMA")

def taboada(parametro):
    for i in range(1,2):        
        os.system("cls || clear")
        print("SEGUE A TABUADA DO NÚMERO SOLICITADO...")
        time.sleep(2)
        print(f"{parametro} x 1: {(parametro*1)}")
        time.sleep(2)
        print(f"{parametro} x 2: {(parametro*2)}")
        time.sleep(2)
        print(f"{parametro} x 3: {(parametro*3)}")
        time.sleep(2)
        print(f"{parametro} x 4: {(parametro*4)}")
        time.sleep(2)
        print(f"{parametro} x 5: {(parametro*5)}")
        time.sleep(2)
        print(f"{parametro} x 6: {(parametro*6)}")
        time.sleep(2)
        print(f"{parametro} x 7: {(parametro*7)}")
        time.sleep(2)
        print(f"{parametro} x 8: {(parametro*8)}")
        time.sleep(2)
        print(f"{parametro} x 9: {(parametro*9)}")
        time.sleep(2)
        print(f"{parametro} x 10: {(parametro*10)}")
        time.sleep(2)
        print("FIM DO PROGRAMA")
    return i

numero = int(input("Digite um número, e assim aparecerá a taboada dele: "))

taboada(numero)