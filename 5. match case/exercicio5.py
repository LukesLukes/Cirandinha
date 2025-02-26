import os
os.system("clear")

valor_do_produto = int(input("Digite o valor de um produto: "))
forma_de_pagamento = float(input("""" 
1 - A vista
2 - A prazo

Digite a forma de pagamento: """))
total_a_pagar = int
parcelas = float

# Processamento

match forma_de_pagamento:
    case 1:
        desconto = valor_do_produto * 0.10
    case 2:
        print(input("Deseja parcelar quantas vezes?: "))    
    case _:
        print("Inválido.")

match parcelas: 
      case 1:  




























