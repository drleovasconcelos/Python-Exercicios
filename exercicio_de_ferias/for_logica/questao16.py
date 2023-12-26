# Faça um programa que pergunte ao usuário a palavra-chave. Enquanto o que for

# digitado pelo usuário for diferente da palavra-chave, informe ao usuário que a palavra-
# chave está incorreta e peça que ele digite novamente. Dica: defina uma variável (str) e
# guarde a palavra para fazer a verificação. Utilize laço de repetição.


palavra_chave = "noelisde"
nome = input("Digite a palavra chave:")
while nome.lower() != palavra_chave:
    print("Senha Incorreta, digite novamente")
    nome = ("Digite a palavra chave: ")
else: 
    print("Senha correta")
