# Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e sálario.
# Faça um algoritmo que informe:
# a) a média de salário do grupo;
# b) maior e menor idade do grupo;
# c) quantidade de mulheres com salário a partir de R$ 5.000,00.
# Crie um menu com três opções.

# Código | Descrição
# 1 | Adicionar pessoa
# 2 | Exibir resultados
# 3 | Sair

# O final da leitura de dados se dará com quando o usuário digitar o número código 3
# Ao adicionar uma família, deve-se limpar o terminal e apresentar o menu novamente.

import os
import time
os.system("cls || clear")

contador = 0
soma_salarial = 0
mulheres5k = 0
maior_idade = 0
menor_idade = 999

while True:
    menu = int(input(("""
    Código \t| Descrição
    1 \t\t| Adicionar Pessoa
    2 \t\t| Exibir resultados
    3 \t\t| Sair

    Digite um número de acordo com a opção que deseja:                                    
                    """)))
    match menu:
        case 1:
            contador += 1
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            sexo = (input("""Digite 'M' caso seja homem ou 'F' se caso seja mulher: """)).upper()
            salario = float(input("Digite o sálario: R$ "))
            soma_salarial += salario
            maior_idade = max(maior_idade, idade)
            menor_idade = min(menor_idade, idade)
            os.system("cls || clear")
            print(f"As informações de {nome}, foram adicionadas.")
            time.sleep(3)
        case 2:
            exibicao_de_resultados = int(input(("""
            1 \t\t| Média de sálario do grupo
            2 \t\t| Maior e Menor idade do grupo
            3 \t\t| Quantidade de mulheres com sálario a partir de R$ 5.000,00                                                

            Digite um número de acordo com a opção que deseja: 
                                """)))
            time.sleep(3)
            match exibicao_de_resultados:
                case 1:
                    os.system("cls || clear")
                    if contador > 0:
                        media_salarial = soma_salarial / contador
                        print(f"Média do sálario do grupo: {media_salarial}")
                        time.sleep(3)
                case 2:
                    if contador > 0:
                        print("Exibindo as idades...")
                        print(f"O mais velho deste do grupo tem: {maior_idade}")           
                        print(f"O mais novo deste grupo tem: {menor_idade}")           
                        time.sleep(3)

                case 3:
                    if contador > 0:
                        print("Exibindo quantidade de mulheres com salário a apartir de R$ 5.000,00...")
                    if sexo == "F" and salario >= 5000:
                        mulheres5k += 1
                        print(mulheres5k)        
        case 3:
            print("Obrigado por ter acessado.")
            time.sleep(3)
            os.system("cls || clear")
            break
        case _:
            print("Erro")
            time.sleep(3)
            os.system("cls || clear")