# Faça um programa que pergunte ao usuário a senha de acesso ao sistema. Enquanto a
# senha de acesso digitada não for correta, informe ao usuário que a senha está incorreta
# e pela que ele digite novamente. Para isso, defina uma variável lógica (bool) 'cadeado'
# e atribua a cadeado o valor False (quer dizer que o cadeado está fechado). A repetição
# deve acontecer enquanto o cadeado estiver fechado. Caso o usuário digite a senha
# correta, mude o valor da variável 'cadeado' para True (cadeado aberto). Ao final, exiba
# a mensagem: "Bem vindo ao sistema, usuário".
nome = 0
cadeado = False
senha_correta = "noelisde"
while not cadeado:
    senha_digitada = input("Digite a palavra chave: ")
    if senha_digitada == senha_correta:
        cadeado = True
        print("Bem-vindo ao sistema, usuário")
    else:
        print("Senha Incorreta. Tente novamente")
