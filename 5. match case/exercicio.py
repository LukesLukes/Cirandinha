import os
os.system("cls||clear")

# Faça um algoritmo que solicite ao usuário dois números e um caractere wue calcula as operações básicas
# (+ - * /)
# Mostre os números informados pelo usuários, o operador escolhido e o resultado.



# Entrada
primeiro_numero = int(input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")
segundo_numero = int(input("Digite um número: "))

# Processamento
match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":    
        resultado = primeiro_numero - segundo_numero 
    case "*":    
        resultado = primeiro_numero * segundo_numero 
    case "/":    
        resultado = primeiro_numero / segundo_numero 

# Saída

print(f"\nPrimeiro número: {primeiro_numero}")
print(f"Operação: {operador}")
print(f"Segundo número: {segundo_numero}")
print(f"Resultado: {resultado}")










