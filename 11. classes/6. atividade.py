import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_admissao: str
    matricula: str
    endereco_funcionario: str
    salario: float

    def exibir_dados_funcionario(self):
        # Saída de dados
        print("Exibindo resultados...\n")
        time.sleep(1)
        print("Dados do Funcionário:")
        print(f"\nNome: {self.nome} | Data de Admissão: {self.data_admissao} | Matrícula: {self.matricula} | Salário: {self.salario} | Endereço: {self.endereco_funcionario}")
        print("--------------------------------------------------")

@dataclass
class Cliente:
    nome: str
    data_nascimento: str
    endereco_cliente: str

    def exibir_dados_clientes(self):
        # Saída de dados
        print("Exibindo resultados...\n")
        time.sleep(1)
        print("Dados do Cliente:")
        print(f"\nNome: {self.nome} | Data de Nascimento: {self.data_nascimento} | Endereço: {self.endereco_cliente}")
        print("--------------------------------------------------")

def main():
    # Atribuindo dados ao funcionário e ao cliente
    lista_funcionarios = []
    lista_clientes = []
    QUANTIDADE = 3

    limpar_terminal()
    for i in range(QUANTIDADE):
        print("=== Cadastro de Funcionário ===")
        funcionario = Funcionario(
            nome = input("Digite o nome do funcionário: "),
            data_admissao = input("Digite a data de admissão (DD/MM/AAAA): "),
            matricula = input("Digite a matrícula do funcionário: "),
            salario = float(input("Digite o salário do funcionário: R$ "),
            endereco_funcionario = input("Digite o endereço do funcionário: "))
        )
        lista_funcionarios.append(funcionario)
        print("--------------------------------------------------")
    
    limpar_terminal()
    for i in range(QUANTIDADE):
        print("=== Cadastro de Cliente ===")
        cliente = Cliente(
            nome = input("Digite o nome do cliente: "),
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): "),
            endereco_cliente = input("Digite o endereço do cliente: ")
        )
        lista_clientes.append(cliente)
        print("--------------------------------------------------")

    # Salvando em um arquivo .txt
    nome_arquivo = "funcionarios_clientes.txt"
    with open(nome_arquivo, "a") as funcionarios_clientes:
        for funcionario in lista_funcionarios:
            funcionarios_clientes.write(f"""
        == Funcionário==        
        Nome: {funcionario.nome}
        Data de Admissão: {funcionario.data_admissao}
        Matrícula: {funcionario.matricula}
        Endereço: {funcionario.endereco_funcionario}
        Salário: R$ {funcionario.salario}\n""")    
            funcionarios_clientes.write("--------------------------------------------------\n")  
        
        for cliente in lista_clientes:
            funcionarios_clientes.write(f"""
        == Cliente ==
        Nome: {cliente.nome}
        Data de Nascimento: {cliente.data_nascimento}
        Endereço: {cliente.endereco_cliente}\n""")
            funcionarios_clientes.write("--------------------------------------------------\n")

    limpar_terminal()
    for funcionario in lista_funcionarios:
        funcionario.exibir_dados_funcionario()
    print("--------------------------------------------------")
    for cliente in lista_clientes:
        cliente.exibir_dados_clientes()

    try:
        with open(nome_arquivo, "r") as funcionarios_clientes:
            print(funcionarios_clientes.read())
    except FileNotFoundError:
        print("Arquivo não encontrado.")

if __name__ == "__main__":
    main() 
