import os
os.system("cls || clear")

usuario_cadastrado = 'Adocica'
senha_cadastrada = 'adocicameuamor25'

while True:
    usuario = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    if usuario_cadastrado != usuario and senha_cadastrada != senha:
        print("login ou senha incorretos. Digite certo, ou será eliminado.")
    else:
        print("Seja bem vindo, Adocica!")
        break








