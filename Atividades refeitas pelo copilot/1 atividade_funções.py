import os
import time

def limpar_tela():
    """Limpa a tela de forma multiplataforma."""
    os.system("cls" if os.name == "nt" else "clear")

def inteiro(parametro):
    limpar_tela()
    print("É positivo ou negativo...")
    time.sleep(2)
    if parametro > 0: 
        print(f"O número {parametro} é positivo!")
    elif parametro == 0:
        print(f"O número {parametro} é neutro.")    
    else:
        print(f"O número {parametro} é negativo!")

def obter_numero():
    """Obtém um número inteiro do usuário com validação."""
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Programa principal
limpar_tela()
numero = obter_numero()
inteiro(numero)