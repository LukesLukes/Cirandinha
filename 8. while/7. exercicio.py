import os
os.system("cls || clear")

refeicao = 0
total_de_pedidos = 0


while True:    
        opcao = int(input(("""
            Código \t Prato \t\t Valor                  
            1 \t Lasanha \t\t R$ 25,00
            2 \t Picanha \t\t R$ 20,00
            3 \t Strogonoff \t\t R$ 18,00
            4 \t Bife Acebolado \t R$ 15,00              
            5 \t Pão com ovo \t\t R$ 5,00

            Digite a opção desejada: 
            """)))   
        match opcao:
            case 1:
                refeicao = 25.00
            case 2:
                refeicao = 20.00        
            case 3:
                refeicao = 18.00        
            case 4:        
                refeicao = 15.00
            case 5:    
                refeicao = 5.00
            case _:
                print("Erro. Digite mais uma vez o número do pedido.")
        total_de_pedidos += refeicao        

        repetir = input("\nDigite '1' se quiser adicionar mais outro prato, ou digite '2' caso não queira: ")
        if repetir == '2':
            print(f"O total foi: {total_de_pedidos}") 
            break
        os.system("cls || clear")