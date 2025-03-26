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
os.system("cls || clear")

contador = 0
soma = 0
maior_idade = 0
menor_idade = 0

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
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            sexo = input("Digite 'M' caso seja homem ou 'F' se caso seja mulher: ").upper()
            salario = input("Digite o sálario: R$ ")
            os.system("cls || clear")
            print(f"As informações de {nome}, foram adicionadas.")
        case 2:
            exibicao_de_resultados = int(input(("""
            1 \t\t| Média de sálario do grupo
            2 \t\t| Maior e Menor idade do grupo
            3 \t\t| Quantidade de mulheres com sálario a partir de R$ 5.000,00                                                

            Digite um número de acordo com a opção que deseja: 
                                """)))
            match exibicao_de_resultados:
                case 1:
                    os.system("cls || clear")
                    contador += 1
                    soma += salario
                    media = soma / contador
                    print(f"Média do sálario do grupo: {media}")
                case 2:
                    
                    
                    print(f"")           
                    print(f"")           
