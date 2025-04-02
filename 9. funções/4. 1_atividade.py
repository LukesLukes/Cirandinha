# Faça uma função sem retorno com o nome: logo_senai()
# Limpando o terminal e inserido: === SENAI DENDEZEIROS ===

# Solicite ao usuário dois números
# Cada um em uma variável diferente
# Crie uma função com retorno para somar, subtrair, multiplicar e dividir os dois números informados pelo usuário.

import os

# Função sem retorno
def logo_senai ():
    os.system("cls || clear")
    print("=== SENAI DENDEZEIROS ===")

# Funções com retorno
def somar_numeros(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    return soma

def subtrair_numeros(primeira_nota, segunda_nota):
    subtrair = primeira_nota - segunda_nota
    return subtrair

def multiplicar_numeros(primeira_nota, segunda_nota):
    multiplicar = primeira_nota * segunda_nota
    return multiplicar

def dividir_numeros(primeira_nota, segunda_nota):
    dividir = primeira_nota / segunda_nota
    return dividir

# Função com retorno (Opcional)
def media_números(primeira_nota, segunda_nota):
    media = (primeira_nota + segunda_nota) / 2
    return media


# Entrada de Dados
logo_senai()
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# Processamento de Dados
logo_senai
soma = somar_numeros(primeiro_numero, segundo_numero)
subtrair = subtrair_numeros(primeiro_numero, segundo_numero)
multiplicar = multiplicar_numeros(primeiro_numero, segundo_numero)
dividir = dividir_numeros(primeiro_numero, segundo_numero)
media = media_números(primeiro_numero, segundo_numero)

# Saída de Dados
logo_senai()
print(f"Soma: {primeiro_numero} + {segundo_numero}")
print(f"Resultado da soma: {soma}\n")

print(f"Subtração: {primeiro_numero} - {segundo_numero}")
print(f"Resultado da subtração: {subtrair}\n")

print(f"Multiplicação: {primeiro_numero} * {segundo_numero}")
print(f"Resultado da multiplicação: {multiplicar}\n")

print(f"Divisão: {primeiro_numero} \ {segundo_numero}")
print(f"Resultado da Divisão: {dividir}\n")

# Dados Opcionais
print(f"Média: ({primeiro_numero} + {segundo_numero}) / 2")
print(f"Resultado da média: {media}")


