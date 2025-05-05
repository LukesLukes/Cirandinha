import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str
    cargo: str
    salario: float

    def exibir_dados(self):
        # Saída de dados
        print("Exibindo resultados...\n")
        time.sleep(1)
        print("Dados do Funcionário:")
        print(f"Nome: {self.nome} | Data de Nascimento: {self.data_nascimento} | RG: {self.rg} | CPF: {self.cpf} | Cargo: {self.cargo} | Salário: R$ {self.salario:.2f}")
        print("--------------------------------------------------")



def main():
    # Atribuindo dados ao funcionário
    lista_funcionarios = []
    QUANTIDADE_FUNCIONARIOS = 5
    
    limpar_terminal()
    for i in range(QUANTIDADE_FUNCIONARIOS):
        funcionario = Funcionario(
            nome = input("Digite o nome do funcionário: "),
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): "),
            rg = input("Digite o RG do funcionário: "),
            cpf = input("Digite o CPF do funcionário: "),
            cargo = input("Digite o cargo do funcionário: "),
            salario = float(input("Digite o salário do funcionário: R$ "))
        )
        lista_funcionarios.append(funcionario)
        print("--------------------------------------------------")

    # Salvando em um arquivo .txt
    nome_arquivo = "funcionarios.txt"
    with open(nome_arquivo, "a") as arquivo_funcionario:
        for funcionario in lista_funcionarios:
            arquivo_funcionario.write(f"""
        Nome: {funcionario.nome}
        Data de Nascimento: {funcionario.data_nascimento}
        RG: {funcionario.rg}
        CPF: {funcionario.cpf}
        Cargo: {funcionario.cargo}
        Salário: R$ {funcionario.salario:.2f}\n""")
            arquivo_funcionario.write("--------------------------------------------------\n")  

    limpar_terminal()
    for funcionario in lista_funcionarios:
        funcionario.exibir_dados()
    print("--------------------------------------------------")

    try:
        with open(nome_arquivo, "r", encoding = "utf-8") as arquivo_funcionario:
            linha = arquivo_funcionario.readline()
            limpar_terminal()
            for linha in arquivo_funcionario:
                print(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado.")

if __name__ == "__main__":
    main()
