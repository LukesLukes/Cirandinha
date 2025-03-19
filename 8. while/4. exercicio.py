import os
os.system("cls || clear")

usuario_cadastrado = 'Adocica'
senha_cadastrada = 'adocicameuamor25'

for i in range(3):
        usuario = input("Digite o seu login: ")
        senha = input("Digite a sua senha: ")

        if usuario_cadastrado != usuario and senha_cadastrada != senha:
            print("login ou senha incorretos. Digite certo, ou será eliminado.\n")
            if i == 2:
                print("Você foi eliminado.")     
        else:
            print("Seja bem vindo, Adocica!")
            break
    








