import os
import time

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

# Lista de nomes.
lista_nomes = []

# Função para verificar se a lista está vazia.
def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        return True
    return False

# Função para adicionar.
def adicionar_nome(lista_nomes):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)
    print(f"Nome '{nome}' adicionado com sucesso!")

# Função para mostrar todos os nomes da lista.
def listar_nomes(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("A lista está vazia! Adicione um nome antes de listar.")
        return
    
    print("\n = Lista de Nomes =")
    for nome in lista_nomes:
        print(f"- {nome}")

# Função para atualizar nome.
def atualizar_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("A lista está vazia! Adicione um nome antes de atualizar.")
        return
    
    lista_nomes(lista_nomes)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_nomes:
        novo_nome = input("Digite o novo nome: ")
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        print(f"Nome '{nome_antigo}' atualizado para '{novo_nome}' com sucesso!")
    else:
        print(f"Nome '{nome_antigo}' não encontrado na lista.")

# Função para excluir.
def excluir_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("A lista está vazia! Adicione um nome antes de excluir.")
        return
    
    lista_nomes(lista_nomes)
    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover in lista_nomes:
        lista_nomes.remove(nome_remover)
        print(f"Nome '{nome_remover}' removido com sucesso!")
    else:
        print(f"Nome '{nome_remover}' não encontrado na lista.")
 
def main():
    # Mostrando menu.
    limpar_terminal()
    while True:
        print("""
    - Gerenciador de Nomes -
    1 - Adicionar Nome
    2 - Listar Nomes
    3 - Atualizar Nome
    4 - Remover Nome
    5 - Sair 
                """)
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                adicionar_nome(lista_nomes)
            case 2:
                listar_nomes(lista_nomes)
            case 3:
                    ...
            case 4:
                excluir_nome(lista_nomes)
            case 5:
                print("Saindo do programa...")
                time.sleep(1)
                limpar_terminal()
                break
            case _:
                print("Opção inválida! Tente novamente.")
                time.sleep(1)
                limpar_terminal()
        time.sleep(3)
        limpar_terminal()

if __name__ == "__main__":
    main()