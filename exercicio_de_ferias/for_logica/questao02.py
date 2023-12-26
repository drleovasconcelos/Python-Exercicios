# Exercício 02
# Escreva um programa que calcule a média aritmética de três números digitados pelo
# usuário.
# Saída de Dados (terminal):
# Digite o primeiro número: 4.5
# Digite o segundo número: 6.2
# Digite o terceiro número: 7.8
# A média é: 6.166666666666667

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
x = (num1, num2, num3)
y = sum(x)
media = y / 3
print(f'A média é: {media}')
