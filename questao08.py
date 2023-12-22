# 08. Suponha uma agenda de 30 contatos, contendo: código e telefone. 
# Faça um programa que permita buscar pelo código e imprimir o telefone.

dict = {}

num = int(input("Qtde: "))
for i in range (num):
    contato = int(input("Digite o contato: "))
    dict[i+1] = contato

print(dict)

