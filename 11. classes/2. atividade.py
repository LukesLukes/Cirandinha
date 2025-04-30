import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preco: float

    def exibir_dados(self):
        # Saída de dados
        print("Exibindo resultados...\n")
        time.sleep(1)
        print("Dados do Livro:")
        print(f"Nome do livro: {self.nome} | Autor: {self.autor} | Categoria: {self.categoria} | Preço: R${self.preco:.2f}")
        print("--------------------------------------------------")

# Criando uma lista de livros
lista_livros = []
QUANTIDADE_LIVROS = 3

def main():
    # Atribuindo dados ao livro
    limpar_terminal()
    for i in range(QUANTIDADE_LIVROS):
        livro = Livros(
            nome = input("Digite o nome do livro: "),
            autor = input("Digite o nome autor do livro: "),
            categoria = input("Digite a categoria do livro: "),
            preco = float(input("Digite o preço do livro: R$ "))
        )
        lista_livros.append(livro)
        print("--------------------------------------------------")
    
    # Salvando em um arquivo .txt
    nome_arquivo = "catalogo_livros.txt"
    with open(nome_arquivo, "a") as arquivo_livro:
        for livro in lista_livros:
            arquivo_livro.write(f"Livro: {livro.nome} | Autor: {livro.autor} | Categoria: {livro.categoria} | Preço: R${livro.preco:.2f}\n")

    # Exibindo os dados dos livros
    limpar_terminal()
    for livro in lista_livros:
        livro.exibir_dados()

if __name__ == "__main__":
    main()        