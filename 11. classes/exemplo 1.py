import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

@dataclass
class Usuário:
    nome: str
    idade: int
    peso: float
    altura: float

# Uso de classe
nome1 = Usuário("Vovisclaudo", 57, 82.5, 1.81)
nome2 = Usuário("Youseff", 25, 73.2, 1.85)

# Saída de dados
limpar_terminal()
print("Exibindo resultados...\n")
time.sleep(2)
print(f"Nome: {nome1.nome} | Idade: {nome1.idade} | Peso: {nome1.peso} | Altura: {nome1.altura}")
print(f"Nome: {nome2.nome} | Idade: {nome2.idade} | Peso: {nome2.peso} | Altura: {nome2.altura}")