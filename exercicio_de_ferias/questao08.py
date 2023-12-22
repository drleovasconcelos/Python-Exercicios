# Faça um programa que verifique se um ano é bissexto ou não. Um ano é bissexto se for
# divisível por 4, mas não por 100, exceto se for divisível por 400.
# Saída de Dados (terminal):
# Digite um ano: 2024
# O ano é bissexto.

ano = int(input("Digite o ano: "))
if ano % 4 == 0:
    print("Ano é Bissexto")
else:
    print("Ano não é Bissexto")


