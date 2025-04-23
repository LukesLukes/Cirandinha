import os
import time

def limpar_terminal():
    # Limpando o terminal
    os.system("clear")

juntar_pratos = []
precos_pratos = []
total_pedidos = 0

limpar_terminal()
while True:
    menu = int(input("""
    \t\t Menu 
    Código \t\t Prato \t\t\t Valor

    1 \t\t Picanha \t\t 25,00
    2 \t\t Lasanha \t\t 20,00
    3 \t\t Strogonoff \t\t 18,00
    4 \t\t Bife Acebolado \t 15,00
    5 \t\t Vara Mista \t\t 5,00
    6 \t\t Hamburguer \t\t 19,99

    
    0 \t\t Escolher novo prato
                     
    Digite o código da opção que você deseja: 
                 """))

    match menu:
        case 1:
            prato = "Picanha"
            valor = 25.00
        case 2:
            prato = "Lasanha"
            valor = 20.00
        case 3:
            prato = "Strogonoff"
            valor = 18.00
        case 4:
            prato = "Bife Acebolado"
            valor = 15.00
        case 5:
            prato = "Vara Mista"
            valor = 5.00
        case 6:
            prato = "Hamburguer"
            valor = 19.99
        case _:
            print("Erro. Digite mais uma vez o número do pedido.")
    
    total_pedidos += valor

    juntar_pratos.append(prato)
    precos_pratos.append(valor)

    limpar_terminal()
    pedido_extra = input("\nDigite '0' para fazer outro pedido. Para parar, digite '7': ")
    if pedido_extra == '7':
        print("Exibindo o resultado dos seus pedidos...")
        time.sleep(2)
        
        limpar_terminal()
        for prato in juntar_pratos:            
            time.sleep(2)
            print(f"Prato escolhido: {prato}")               
        for valor in precos_pratos:
            print(f"Valores (do primeiro ao ultimo pedido): {valor}")
            time.sleep(2)
        print(f"Valor total: {total_pedidos}")
        break