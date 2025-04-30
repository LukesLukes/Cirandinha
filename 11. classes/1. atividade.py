import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

@dataclass
class Pessoa:
    # Atributos: são variáveis que pertencem à classe
    nome: str
    idade: int
    peso: float
    altura: float 

    # Método: é uma função que pertence a classe. Este método é para exibir dados do paciente.
    def exibir_dados(self):
        # Saída de dados
        print("Exibindo resultados...\n")
        time.sleep(1)
        print("Dados da Pessoa:")
        print(f"Nome: {self.nome} | Idade: {self.idade} | Peso: {self.peso} | Altura: {self.altura}")
        print("--------------------------------------------------")

# Criando uma lista de pessoas
lista_pessoas = []
QUANTIDADE_PESSOAS = 4

def main():
    # Atribuindo dados a pessoa
    limpar_terminal()
    for i in range(QUANTIDADE_PESSOAS):
        pessoa = Pessoa(
            nome = input("Digite seu nome: "),
            idade = int(input("Digite sua idade: ")),
            peso = float(input("Digite o seu peso: ")),
            altura = float(input("Digite a sua altura: "))
        )
        lista_pessoas.append(pessoa)

    # Exibindo os dados dos pacientes
    limpar_terminal()
    for pessoa in lista_pessoas:
        pessoa.exibir_dados()

if __name__ == "__main__":
    main()