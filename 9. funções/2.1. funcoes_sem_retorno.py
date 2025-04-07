# Funções sem retorno

import os
os.system("clear")

def saudacao(parametro):
    os.system("clear")
    print(f"Olá, {parametro}!")


nome_do_visistante = input("Qual o seu nome?: ")
saudacao(nome_do_visistante)