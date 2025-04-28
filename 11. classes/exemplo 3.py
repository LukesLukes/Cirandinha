import os
import time
from dataclasses import dataclass   

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")   

@dataclass
class Endereco:
    logradouro: str
    numero: str

@dataclass
class Usuario: 
    nome: str
    email: str
    telefone: str
    endereco: Endereco  

    def exibir_dados(self):
        # Saída de dados
        limpar_terminal()
        print("Exibindo resultados...\n")
        time.sleep(2)
        print("Dados do Usuário:")
        print(f"Nome: {self.nome} | Email: {self.email} | Telefone: {self.telefone} | Endereço: {self.endereco.logradouro} {self.endereco.numero}")

def main():
    limpar_terminal()
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ") 
    telefone = input("Digite seu telefone: ")   
    logradouro = input("Digite seu logradouro: ")   
    numero = input("Digite o número da sua residência: ")

    # Uso de classe
    endereco = Endereco(logradouro, numero)
    usuario = Usuario(nome, email, telefone, endereco)
    usuario.exibir_dados()

if __name__ == "__main__":
    main()