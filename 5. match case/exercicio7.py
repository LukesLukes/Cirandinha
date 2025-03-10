import os
os.system("clear")

# O algortimo deve escrever o nome do aluno, duas notas, a média, o conceito correspondente e a mensagem 'Aprovado' se o conceito
# for A, B ou C, e 'Reprovado' se o conceito for D ou E.

nome_do_aluno = input("Digite o nome do aluno: ")
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
media = (primeira_nota + segunda_nota) / 2


if media >= 9:
   conceito = "A" 
elif media > 7.5:
   conceito = "B" 
elif media > 6:
   conceito = "C" 
elif media > 4:
   conceito = "D"
else:    
   conceito = "E"

match conceito:
   case "A" | "B" | "C":
      print(f"Conceito: {conceito}")
      print("Aprovado.")
   case "D" | "E":  
      print(f"Conceito: {conceito}")
      print("Reprovado.")
   case _:
      print("Opção Inválida.")     








