import os
os.system("cls||clear")

# Faça um algoritmo que mostre um menu com opções de um cardápio de restaurante para uma pessoa
# A pessoa vai escolher o prato desejado digitando o código do prato.
# Após escolher o prato, o algoritmo deve mostrar o nome e valor do prato escolhido.

# Entrada

opcao = int(input("""
Código \t Prato \t\t Valor                  
1 \t Lasanha \t\t R$ 25,00
2 \t Picanha \t\t R$ 20,00
3 \t Strogonoff \t\t R$ 18,00
4 \t Bife Acebolado \t R$ 15,00              
5 \t Pão com ovo \t\t R$ 5,00
6 \t Pizza \t\t\t R$ 30,00                  
7 \t Empadão Salgado \t R$ 35,00

Digite a opção desejada: 
"""))

# Processamento
match opcao:
    case 1:
        print("Pedido de: , feito com sucesso!")
    case 2:
        print("Pedido de: , feito com sucesso!")
    case 3:
        print("Pedido de: , feito com sucesso!")
    case 4:
        print("Pedido de: , feito com sucesso!")
    case 5:
        print("Pedido de: , feito com sucesso!")
    case 6:
        print("Pedido de: , feito com sucesso!")
    case 7:
        print("Pedido de: Empadão Salgado, feito com sucesso!")

























