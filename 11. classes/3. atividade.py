import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

@dataclass
class Funcionarios:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str

    def exibir_dados(self):
        # Saída de dados
        print("Exibindo resultados...\n")
        time.sleep(1)
        print("Dados do Funcionário:")
        print(f"Nome: {self.nome} | Data de Nascimento: {self.data_nascimento} | RG: {self.rg} | CPF: {self.cpf}")
        print("--------------------------------------------------")

# Criando uma lista de funcionários
lista_funcionarios = []
QUANTIDADE_FUNCIONARIOS = 5

def main():
    # Atribuindo dados ao funcionário
    limpar_terminal()
    for i in range(QUANTIDADE_FUNCIONARIOS):
        funcionario = Funcionarios(
            nome = input("Digite o seu nome: "),
            data_nascimento = input("Digite a sua data de nascimento (DD/MM/AAAA): "),
            rg = input("Digite o seu RG: "),
            cpf = input("Digite o seu CPF: ")
        )
        lista_funcionarios.append(funcionario)
        print("--------------------------------------------------")
    
    # Salvando em um arquivo .txt
    nome_arquivo = "Funcionarios.txt"
    with open(nome_arquivo, "a") as arquivo_funcionario:
        for funcionario in lista_funcionarios:
            arquivo_funcionario.write(f"Funcionário: {funcionario.nome} | Data de Nascimento: {funcionario.data_nascimento} | RG: {funcionario.rg} | CPF: {funcionario.cpf}\n")
            arquivo_funcionario.write("--------------------------------------------------\n")
    # Exibindo os dados dos funcionários
    limpar_terminal()
    for funcionario in lista_funcionarios:
        funcionario.exibir_dados()

if __name__ == "__main__":
    main()        
    