import os
import time
from dataclasses import dataclass 

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

@dataclass
class Paciente:
    # Atributos: são variáveis que pertencem à classe
    nome: str
    idade: int

    # Método: é uma função que pertence a classe. Este método é para exibir dados do paciente.
    def exibir_dados(self):
        # Saída de dados
        print("Exibindo resultados...\n")
        time.sleep(1)
        print("Dados do Paciente:")
        print(f"Nome: {self.nome} | Idade: {self.idade}")
        print("--------------------------------------------------")

# Criando uma lista de pacientes
lista_pacientes = []
QUANTIDADE_PACIENTES = 2

def main():
# Atribuindo dados ao paciente1
    limpar_terminal()
    for i in range(QUANTIDADE_PACIENTES):
        paciente = Paciente(
            nome = input("Digite o nome do paciente: "),
            idade = int(input("Digite a idade do paciente: "))
        )
        lista_pacientes.append(paciente)
        print("--------------------------------------------------")
    
    # Salvando em um arquivo .txt
    nome_arquivo = "Dados_paciente.txt"
    with open(nome_arquivo, "a") as arquivo_paciente:
        for paciente in lista_pacientes:
            arquivo_paciente.write(f"Paciente: {paciente.nome} | Idade: {paciente.idade}\n")

    # Exibindo os dados dos pacientes
    limpar_terminal()
    for paciente in lista_pacientes:
        paciente.exibir_dados() 

if __name__ == "__main__":
    main()
    # o código acima (main) serve para executar o código, ou seja, ele é o ponto de partida do programa.
    # Se o arquivo for executado diretamente, o código dentro do if será executado.
    # Se o arquivo for importado como um módulo, o código dentro do if não será executado.