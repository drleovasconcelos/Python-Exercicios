# Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email 
# cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição 
# juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email 
# e senha cadastrados antecipadamente. 
# E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.

email_cadastrado = "exemplo@gmail.com"
senha_cadastrada = "senha123"

while True:
    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")

    if email_usuario == email_cadastrado and senha_usuario == senha_cadastrada:
        print("Login realizado com sucesso!")
        break  
    else:
        print("Email ou senha incorretos. Tente novamente.")
