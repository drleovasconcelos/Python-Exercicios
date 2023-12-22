# Crie um programa que verifique se uma pessoa pode votar ou não, considerando que a
# idade mínima para votar é 16 anos.
# Saída de Dados (terminal):
# Digite sua idade: 20
# Você pode votar.

idade = int(input("Digite a idade: "))
if idade >= 16:
    print("Você pode Votar")
else:
    print("Você não pode votar")