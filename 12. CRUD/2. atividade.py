import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpando o terminal
    os.system("cls || clear")

# Criando lista de alunos
lista_alunos = []

# Criando classes
@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str
    estado: str

@dataclass
class Aluno:
    nome: str
    data_de_nascimento: str
    matricula: str
    curso: str
    endereco: Endereco

    def exibir_dados(self):
        print("Recebendo dados do aluno...")
        time.sleep(2)
        print("Dados recebidos com sucesso!")

# Criando o CRUD
def verificar_lista_vazia(lista_alunos):
    if not lista_alunos:
        return True
    return False

def adicionar_aluno(lista_alunos):
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    nome = input("Digite o nome do aluno: ")
    data_de_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    matricula = input("Digite a matrícula (apenas números): ")
    curso = input("Digite o curso do aluno: ")
    
    limpar_terminal()
    print("Agora digite as informações correspondentes ao endereço do aluno...\n")
    time.sleep(2)
    # Coletando dados do endereço
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    endereco = Endereco(logradouro, numero, cidade, estado)
    
    limpar_terminal()
    print("Adicionando aluno...")
    aluno = Aluno(nome, data_de_nascimento, matricula, curso, endereco)
    lista_alunos.append(aluno)
    print(f"Aluno '{nome}' adicionado com sucesso!")

def listar_alunos(lista_alunos):
    if verificar_lista_vazia(lista_alunos):
        print("A lista de alunos está vazia! Adicione um aluno antes de listar.")
        return
    
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    print("\n = Lista de Alunos =")
    for aluno in lista_alunos:
        print(f""" 
              Nome: {aluno.nome} 
              Data de Nascimento: {aluno.data_de_nascimento}
              Matrícula: {aluno.matricula} 
              Curso: {aluno.curso}\n
        
              \t - Endereço -\n 
              Logradouro: {aluno.endereco.logradouro}
              Número: {aluno.endereco.numero} 
              Cidade: {aluno.endereco.cidade} 
              Estado: {aluno.endereco.estado}""")
        print("=====================================================================")

def atualizar_aluno(lista_alunos):
    if verificar_lista_vazia(lista_alunos):
        print("A lista de alunos está vazia! Adicione um aluno antes de atualizar.")
        return
    
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    listar_alunos(lista_alunos)
    nome_antigo = input("Digite o nome do aluno que deseja atualizar: ")
    data_nascimento_antigo = input("Digite a data de nascimento do aluno que deseja atualizar (DD/MM/AAAA): ")
    matricula_antiga = input("Digite a matrícula do aluno que deseja atualizar: ")
    curso_antigo = input("Digite o curso do aluno que deseja atualizar: ")

    # Coletando dados do endereço
    logradouro_anterior = input("Digite o logradouro: ")
    numero_anterior = input("Digite o número: ")
    cidade_anterior = input("Digite a cidade: ")
    estado_anterior = input("Digite o estado: ")

    endereco = Endereco(logradouro_anterior, numero_anterior, cidade_anterior, estado_anterior)

    for aluno in lista_alunos:
        if (aluno.nome == nome_antigo and
            aluno.data_de_nascimento == data_nascimento_antigo and
            aluno.matricula == matricula_antiga and
            aluno.curso == curso_antigo):
            
            aluno.nome = input(f"Novo nome (atual: {aluno.nome}): ") or aluno.nome
            aluno.data_de_nascimento = input(f"Nova data de nascimento (atual: {aluno.data_de_nascimento}): ") or aluno.data_de_nascimento
            aluno.matricula = input(f"Nova matrícula (atual: {aluno.matricula}): ") or aluno.matricula
            aluno.curso = input(f"Novo curso (atual: {aluno.curso}): ") or aluno.curso
        print("================================")
        print(" - Endereço - ")
            # Atualizando endereço
        if (aluno.endereco.logradouro == logradouro_anterior and
            aluno.endereco.numero == numero_anterior and
            aluno.endereco.cidade == cidade_anterior and
            aluno.endereco.estado == estado_anterior):
            
            aluno.endereco.logradouro = input(f"Novo logradouro (atual: {aluno.endereco.logradouro}): ") or aluno.endereco.logradouro
            aluno.endereco.numero = input(f"Novo número (atual: {aluno.endereco.numero}): ") or aluno.endereco.numero
            aluno.endereco.cidade = input(f"Nova cidade (atual: {aluno.endereco.cidade}): ") or aluno.endereco.cidade
            aluno.endereco.estado = input(f"Novo estado (atual: {aluno.endereco.estado}): ") or aluno.endereco.estado

            print("Aluno atualizado com sucesso!")
            return
        else:
            print(f"Aluno '{nome_antigo}' não encontrado na lista.")
            return
        
def excluir_aluno(lista_alunos):
    if verificar_lista_vazia(lista_alunos):
        print("A lista de alunos está vazia! Adicione um aluno antes de excluir.")
        return
    
    limpar_terminal()
    print("Carregando...\n")
    time.sleep(2)
    limpar_terminal()
    listar_alunos(lista_alunos)
    nome_remover = input("Digite o nome do aluno que deseja remover: ")
    data_nascimento_remover = input("Digite a data de nascimento do aluno que deseja remover (DD/MM/AAAA): ")
    matricula_remover = input("Digite a matrícula do aluno que deseja remover: ")
    curso_remover = input("Digite o curso do aluno que deseja remover: ")
    logradouro_remover = input("Digite o logradouro do aluno que deseja remover: ")
    numero_remover = input("Digite o número do aluno que deseja remover: ")
    cidade_remover = input("Digite a cidade do aluno que deseja remover: ")
    estado_remover = input("Digite o estado do aluno que deseja remover: ")

    limpar_terminal()
    for aluno in lista_alunos:
        if (aluno.nome == nome_remover and
            aluno.data_de_nascimento == data_nascimento_remover and
            aluno.matricula == matricula_remover and
            aluno.curso == curso_remover and
            aluno.endereco.logradouro == logradouro_remover and
            aluno.endereco.numero == numero_remover and
            aluno.endereco.cidade == cidade_remover and
            aluno.endereco.estado == estado_remover):

            print("Removendo aluno...")
            time.sleep(2)
            print("Aluno encontrado!")

            lista_alunos.remove(aluno)
            print(f"Aluno '{nome_remover}' removido com sucesso!")
            return
        else:
            print(f"Aluno '{nome_remover}' não encontrado na lista.")

def main():
    limpar_terminal()
    print("Bem vindo(a) ao sistema de gerenciamento de dados de alunos!")
    print("Para continuar, pressione 'Enter'...")
    input()
    while True:
        limpar_terminal()
        time.sleep(2)
        menu = int(input("""
        = Menu =
                         
1 - Adicionar Novo Aluno
2 - Listar Alunos
3 - Atualizar Dados do Aluno
4 - Excluir Dados do Aluno
5 - Sair
    
    Para escolher uma opção, digite um número: """))
        if menu == 1:
            adicionar_aluno(lista_alunos)
        elif menu == 2:
            listar_alunos(lista_alunos)
            time.sleep(4)
            print("Digite 'Enter' para continuar...")
            input()
        elif menu == 3:
            atualizar_aluno(lista_alunos)
        elif menu == 4:
            excluir_aluno(lista_alunos)
        elif menu == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
        
        continuar = input("Pressione Enter para continuar...")
        limpar_terminal()

if __name__ == "__main__":
    main()