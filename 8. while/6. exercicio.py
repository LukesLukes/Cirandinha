import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:    
        nota = float(input("Digite a nota do aluno: "))
    
        if nota < 0 or nota > 10:
            print("Erro. Digite novamente.")
        else:
            soma += nota
            break
        
media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "PARABÉNS! o aluno foi aprovado." 
elif media >= 5 and media <= 6.9:    
    resultado = "O aluno está em recuperação." 
elif media < 5:   
    resultado = "O aluno foi reprovado."
else:
    print("Erro.")     
        
print(f"\nMédia: {media}")               
print(f"Resultado: {resultado}")               
         
     








