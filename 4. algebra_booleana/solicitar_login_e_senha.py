import os
os.system("clear")

# Elabore um algoritmo para solicitar ao usuário o login e a senha.
# Consisdere que os dados do usuário já estão cadastrados.
# Caso o login e senha estejam corretos, mostre a mensagem: "Bem-vindo!"
# Caso contrário, mostre a mensagem: "Login ou senha inválidos."

login_cadastrado = "jubileu21@gmail.com"
senha_cadastrado = "sambaelove21"

login = (input("Digite seu email: "))
senha = (input("Digite a sua senha: "))

if login == login_cadastrado and senha == senha_cadastrado:
   print("Bem-vindo!")
else:
   print("Login ou senha inválidos!")   












