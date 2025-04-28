import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str

# Exemplo de uso de classe
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob Marley", 25)

pet1 = Pet("Mario", 5, "American Bull")
pet2 = Pet("Chupetilson", 10, "Salsicha")



# Saída de dados
limpar_terminal()
print("Exibindo resultados...\n")
time.sleep(2)
print(f"Nome: {pessoa1.nome} | Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome} | Idade: {pessoa2.idade}\n")

print(f"Nome do Pet: {pet1.nome} | Idade: {pet1.idade} | Raça: {pet1.raca}")
print(f"Nome do Pet: {pet2.nome} | Idade: {pet2.idade} | Raça: {pet2.raca}")

