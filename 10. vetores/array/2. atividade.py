import os
import time

def limpar_terminal():
    # Limpando o terminal
    os.system("cls || clear")


# Resultados com base na média.
def resultados_média(media):
    if media >= 7:
        resultado = "Você foi aprovado!"
    elif media >= 5 and media < 7:
        resultado = "Você está em recuperação."
    else:
        resultado = "Você foi reprovado."
    return resultado

def calcular_media(media):
    return sum(lista_notas) / QUANTIDADE_NOTAS

# Criando uma lista.
lista_notas = []
QUANTIDADE_NOTAS = 4

# Adicionando 4 notas na lista.
limpar_terminal()
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Soma e Média das notas.

media = calcular_media(lista_notas)
resultado = resultados_média(media)

# Exibindo resultados.
limpar_terminal()
print()
time.sleep(1)
for nota in lista_notas: # ForEach
    print(nota)
    time.sleep(1)
print(f"Média: {media}")
time.sleep(1)    
print(f"Resultado: {resultado}")    