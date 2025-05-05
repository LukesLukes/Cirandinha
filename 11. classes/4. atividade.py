import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor
    
    def exibir_dados(self):
        # Saída de dados
        print("Exibindo resultados...\n")
        time.sleep(1)
        print("Dados do Livro:")
        print(f"Título: {self.titulo} | Ano: {self.ano} | Autor: {self.autor.nome} | Biografia: {self.autor.biografia}")
        print("--------------------------------------------------")

# Criando uma lista de livros
lista_livros = []
QUANTIDADE_LIVROS = 3

def main(): # Definindo a função principal
    
    # Atribuindo dados ao livro
    limpar_terminal()
    for i in range(QUANTIDADE_LIVROS):
        autor = Autor(
            nome = input("Digite o nome do autor: "),
            biografia = input("Digite a biografia do autor: ")
        )
        livro = Livro(
            titulo = input("Digite o título do livro: "),
            ano = int(input("Digite o ano de publicação: ")),
            autor = autor
        )
        lista_livros.append(livro)
        print("--------------------------------------------------")
    
    # Salvando em um arquivo .txt
    nome_arquivo = "catalogo_livros_2.txt"
    with open(nome_arquivo, "a") as arquivo_livro:
        for livro in lista_livros:
            arquivo_livro.write(f"""
        Livro: {livro.titulo}
        Ano: {livro.ano}
        Autor: {livro.autor.nome}
        Biografia: {livro.autor.biografia}\n""")
            arquivo_livro.write("--------------------------------------------------\n")
    # Exibindo os dados dos livros
    limpar_terminal()
    for livro in lista_livros:
        livro.exibir_dados()

    try:
        with open (nome_arquivo, "r", encoding = "utf-8") as arquivo_livro:
            linhas = arquivo_livro.readlines()
            for linha in linhas:
                print(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado.")

if __name__ == "__main__": # Executando a função principal
    main()