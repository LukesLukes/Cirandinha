# Funções sem retorno






import os

# Função sem retorno
def logo_senai ():
    os.system("cls || clear")
    print("=== SENAI 2025 ===")

logo_senai() # Chamando a função
nome = input("Digite o seu nome: ")

logo_senai() # Chamando a função
idade = int(input("Digite a sua idade: "))

logo_senai() # Chamando a função
print(f"Nome: {nome}")
print(f"Idade: {idade}")